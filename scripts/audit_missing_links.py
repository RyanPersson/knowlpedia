#!/usr/bin/env python3
"""Read-only phrase/dependency audit. Findings are review candidates, not fixes."""
from __future__ import annotations

import argparse
from bisect import bisect_right
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re

from audit_dependency_graph import compiler
from interlink_content import is_plain_term, normalize_surface, plural_variant, split_frontmatter

CONTAINERS = {"document", "index", "page", "section"}
# Preserve offsets and line boundaries; masked syntax must not join nearby words.
BLOCK = re.compile(r"(?ms)^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1[^\n]*(?:\n|$)")
PROTECTED = re.compile(
    r"<!--.*?-->|`+[^`]*`+|\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$\$.*?(?<!\\)\$\$|"
    r"(?<!\\)\$(?!\$).*?(?<!\\)\$|!?\[[^\]]*\]\([^)]*\)|"
    r"!?\[[^\]]*\]\[[^\]]*\]|<[^>]+>", re.DOTALL
)
WORD = r"[^\W\d_]+(?:[-’'][^\W\d_]+)*"
WORDS = re.compile(WORD, re.UNICODE)
HEADS = set("space group ring field algebra module category functor transformation bundle manifold measure integral operator kernel topology metric norm distribution representation theorem lemma principle conjecture equation disk model map morphism action product sequence complex spectrum homology cohomology filtration form connection curvature derivative sheaf scheme variety lattice ideal quotient".split())
STOP = set("a an the this that these those is are was were be being been of on in over under for from to by with without and or as if then its it their any each every some such given let called defined defining whose which where when corresponding associated induced resulting natural particular general same other following above below also hence therefore admits has have can we our".split())


def mask(text: str, *, links: bool = True) -> str:
    def blank(match):
        return ''.join('\n' if c == '\n' else '\x00' for c in match.group())
    text = BLOCK.sub(blank, text)
    text = PROTECTED.sub(blank, text)
    if links:
        text = compiler.WIKILINK_RE.sub(blank, text)
    return text


def regions(text: str):
    """Yield prose sections with exact source offsets; exclude reference sections."""
    _, lines, start = split_frontmatter(text)
    offset = sum(map(len, lines[:start]))
    section, chunk_start, chunk = 'core', offset, []
    fenced = None
    for line in lines[start:]:
        fence = re.match(r'^\s*(`{3,}|~{3,})', line)
        if fence:
            marker = fence.group(1)
            if fenced is None:
                fenced = marker
            elif marker[0] == fenced[0] and len(marker) >= len(fenced):
                fenced = None
        heading = re.match(r'^#{1,6}\s+(.+?)\s*$', line) if fenced is None else None
        if heading:
            if section.casefold() not in {'references', 'sources', 'bibliography', 'literature'}:
                yield section, chunk_start, ''.join(chunk)
            section, chunk_start, chunk = heading.group(1), offset + len(line), []
        else:
            chunk.append(line)
        offset += len(line)
    if section.casefold() not in {'references', 'sources', 'bibliography', 'literature'}:
        yield section, chunk_start, ''.join(chunk)


def term_index(registry):
    claims = defaultdict(set)
    origins = defaultdict(set)
    for knowl in registry.values():
        if knowl.kind in CONTAINERS:
            continue
        for term, origin in [(knowl.title, 'title'), *((a, 'alias') for a in knowl.aliases)]:
            for surface, label in [(term, origin), (plural_variant(term), origin + '_plural')]:
                if surface and is_plain_term(surface, True):
                    key = normalize_surface(surface)
                    claims[key].add(knowl.id)
                    origins[key].add(label)
    return claims, origins


def audit(package: Path, profile='production', min_sources=3, seeds=()):
    package = package.resolve()
    knowls, _ = compiler.discover_package_knowls(package, compiler.read_toml(package / 'knowlpack.toml'), compiler.BUILD_PROFILES[profile])
    registry, validation = compiler.build_registry(knowls)
    claims, origins = term_index(registry)
    seed_terms = {normalize_surface(s) for s in seeds if s.strip()}
    terms = sorted(claims.keys() | seed_terms, key=lambda s: (-len(s), s))
    buckets = defaultdict(list)
    for term in terms:
        first = re.match(r'\w+', term)
        if first:
            buckets[first.group().casefold()].append(re.escape(term).replace(r'\ ', r'(?:[^\S\n]+|[^\S\n]*\n(?![^\S\n]*\n)[^\S\n]*)'))
    patterns = {key: re.compile(r'(?<![\w-])(?:'+'|'.join(values)+r')(?![\w-])', re.I) for key, values in buckets.items()}

    def matches(prose):
        consumed = 0
        for word in re.finditer(r'\w+', prose):
            if word.start() < consumed:
                continue
            pattern = patterns.get(word.group().casefold())
            match = pattern.match(prose, word.start()) if pattern else None
            if match:
                consumed = match.end()
                yield match

    findings, gaps, inventory = [], defaultdict(list), []
    for knowl in sorted(registry.values(), key=lambda k: k.id):
        text = knowl.source_path.read_text()
        digest = hashlib.sha256(text.encode()).hexdigest()
        inventory.append({'id': knowl.id, 'source_sha256': digest, 'path': str(knowl.source_path.relative_to(package)), 'kind': knowl.kind})
        if knowl.kind in CONTAINERS:
            continue
        line_starts = [0] + [m.end() for m in re.finditer('\n', text)]
        def record(kind, section, offset, surface, **extra):
            line_index = bisect_right(line_starts, offset) - 1
            item = dict(kind=kind, source_id=knowl.id, source_path=str(knowl.source_path.relative_to(package)), source_sha256=digest,
                        section=section, line=line_index + 1, column=offset - line_starts[line_index] + 1,
                        surface=surface, context=text[max(0, offset-90):offset+len(surface)+120], **extra)
            item['candidate_id'] = hashlib.sha256(json.dumps(item, sort_keys=True).encode()).hexdigest()[:24]
            return item
        for target in knowl.prerequisites:
            canonical = compiler.split_target(compiler.canonical_target(registry, target))[0]
            if canonical not in registry:
                findings.append(record('missing_prerequisite_target', 'metadata', 0, target, targets=[canonical]))
        for section, base, body in regions(text):
            link_text = mask(body, links=False)
            linked = set()
            for match in compiler.WIKILINK_RE.finditer(link_text):
                target = compiler.split_target(compiler.canonical_target(registry, match.group(1)))[0]
                linked.add(target)
                if target not in registry:
                    findings.append(record('broken_link', section, base+match.start(), body[match.start():match.end()], targets=[target]))
            prose = mask(body)
            seen = set()
            occupied = []
            for match in matches(prose):
                key = normalize_surface(match.group())
                targets = sorted(claims.get(key, set()))
                occupied.append(match.span())
                if knowl.id in targets or key in seen:
                    continue
                seen.add(key)
                if not targets:
                    gaps[key].append(record('possible_missing_definition', section, base+match.start(), match.group(), signal='seed'))
                    continue
                if len(targets) == 1 and targets[0] in linked:
                    continue
                findings.append(record('ambiguous_phrase' if len(targets)>1 else 'unlinked_phrase', section, base+match.start(), match.group(),
                                       targets=targets, origins=sorted(origins[key]),
                                       priority='core' if section=='core' else 'supporting',
                                       single_word=len(key.split())==1))
            # Discovery independent of the registry: short noun phrases ending in a
            # mathematical head. Frequency is evidence for review, not concept identity.
            tokens = list(WORDS.finditer(prose))
            for end, token in enumerate(tokens):
                if token.group().casefold() not in HEADS:
                    continue
                for size in (2, 3):
                    start = end-size+1
                    if start < 0:
                        continue
                    window = tokens[start:end+1]
                    if any(t.group().casefold() in STOP for t in window):
                        continue
                    if any(not re.fullmatch(r'\s+', prose[a.end():b.start()]) or '\n\n' in prose[a.end():b.start()] for a,b in zip(window,window[1:])):
                        continue
                    a,b = window[0].start(), token.end()
                    if any(x <= a and b <= y for x,y in occupied):
                        continue
                    surface = prose[a:b]
                    key = normalize_surface(surface)
                    if key in seen or key in claims:
                        continue
                    seen.add(key)
                    gaps[key].append(record('possible_missing_definition', section, base+a, surface, signal='noun_phrase'))
    gap_groups = []
    for phrase, occurrences in gaps.items():
        sources = len({o['source_id'] for o in occurrences})
        if sources >= min_sources or phrase in seed_terms:
            related = sorted({target for term, targets in claims.items()
                              if len(term.split()) > 1 and (phrase in term or term in phrase)
                              for target in targets})
            gap_groups.append(dict(phrase=phrase, source_count=sources, core_source_count=len({o['source_id'] for o in occurrences if o['section']=='core'}),
                                   related_targets=related[:12], related_target_count=len(related), occurrences=occurrences))
    gap_groups.sort(key=lambda g: (-g['core_source_count'], -g['source_count'], g['phrase']))
    counts = dict(Counter(f['kind'] for f in findings))
    for kind in ('unlinked_phrase', 'ambiguous_phrase', 'broken_link', 'missing_prerequisite_target'):
        counts.setdefault(kind, 0)
    counts['core_multiword_unlinked'] = sum(f['kind']=='unlinked_phrase' and f['section']=='core' and not f['single_word'] for f in findings)
    counts.update(canonical_knowls=len(inventory), eligible_knowls=sum(i['kind'] not in CONTAINERS for i in inventory), possible_missing_definitions=len(gap_groups))
    return dict(version=1, profile=profile, counts=counts, inventory=inventory, findings=findings, possible_missing_definitions=gap_groups,
                validation=[vars(v) for v in validation], parameters=dict(min_sources=min_sources, seed_terms=sorted(seed_terms)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--content-package', type=Path, required=True)
    parser.add_argument('--profile', choices=compiler.PROFILE_NAMES, default='production')
    parser.add_argument('--min-sources', type=int, default=3)
    parser.add_argument('--seeds', type=Path, help='One phrase per line; discover explicitly reported rare gaps too.')
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    if args.min_sources < 1:
        parser.error('--min-sources must be positive')
    seeds = [s.strip() for s in args.seeds.read_text().splitlines() if s.strip() and not s.lstrip().startswith('#')] if args.seeds else []
    report = audit(args.content_package, args.profile, args.min_sources, seeds)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(report['counts'], indent=2))


if __name__ == '__main__':
    main()
