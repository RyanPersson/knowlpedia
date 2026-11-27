# riemann2 orchestration state (orchestrator's notes)

Branches: knowlpedia + knowlpedia-content on `riemann2` (from main 46b29f2 / 1097de8f).
Guide: documents/riemann2/GUIDE.md ; areas: areas.tsv ; prompts/<area>.md
Maintenance lock: background `navier-job -- sleep 7100` (re-arm when it exits).

## Pipeline
1. Phase 1 (running): 42 area agents read Lean, write proof knowls to content/proofs/grh/<area>/ with placeholders
   `[[?c:concept|..]]` and `[[?lean:Name|..]]`, sidecars concepts/<area>.tsv, reports/<area>.md.
2. Merge concepts -> cross-check corpus -> reserve IDs (registry.tsv) -> subject knowl writers.
3. Audit new subject knowls for unlinked/missing deps.
4. Resolve placeholders in proofs/grh (script), fill prerequisites, root page proofs/grh, proofs section page.
5. Compiler: `proof = true` home-page section "Proofs"; build; check rendering; commit both repos.

## Agents launched (area -> agentId)
reduction-zeros ac5511e24482ff9f1
reduction-main a14da122d5f55d14a
derivatives-divisibility acebff8af9f646565
derivatives-vacuum acc6db768458469bc
upper-objects a7e10792501f57a5b
upper-seesaw aecec739a643f3f01
upper-divisibility a90202279627a07d2
upper-elementary-divisors a0d7741b65214eebf
spanning-core afe0da48371d3d3fc
spanning-unfolding-a ad1d53910a7a72d95
spanning-unfolding-b af8c29f130ebc114d
spanning-mainterm abd8dc31912299c72
spanning-remaining-a a0949409682e112a6
spanning-remaining-b aae24fbb75a896b0c
spanning-frames-a a6bedb9a58dfa12a9
spanning-frames-b ae63169cb96740b89
determinant-exchange a3ff9426e9f1ba414
determinant-chain ac5d3936215eb8c9c
onelift-comparison a1e43e977cceaece9
onelift-values ade5b667c752b5f5f

Concurrency limit: 20 subagents. PENDING launch (in this order): congruences-first-order, congruences-selmer,
congruences-lifting, appendix-discrete-series, then all lib-* areas in areas.tsv order.
Launch prompt: "Your complete assignment is in the file .../prompts/<area>.md . Read that file first and carry it out exactly. Work only inside /home/codex/code/knowlpedia-root."

## 2026-11-26 01:15 — quota burnt by the 20-agent fan-out; user says: work SINGLE-THREADED from now on,
task will span several days / 5-hour windows. All 20 agents stopped mid-work (rate limit), their context is
saved; resume ONE AT A TIME with SendMessage("continue; finish sidecar + report + area page") in argument
order: reduction-zeros, reduction-main, derivatives-*, upper-*, spanning-*, determinant-*, onelift-*, then
launch the never-started ones (congruences-*, appendix, lib-*) one at a time.
On disk at stop: ~218 draft proof knowls under content/proofs/grh/<area>/, no concept sidecars yet,
spanning-frames-a / spanning-remaining-a,b have 0 knowls. Nothing committed. Compiler Proofs-section change
is uncommitted in knowlpedia (tests pass).

DONE: reduction-zeros (59 knowls, 47 full/2 outline; sidecar 62 lines). Doubts: bridge integer->real x in OneSidedBound; Lean names New.entireL/quadTwist/chiK/chowlaSelbergConst unchecked; complex Gamma knowl needed. Next: reduction-main (resumed).
DONE: reduction-main (51 knowls, 23 full/5 outline; sidecar 56). Integer->real bridge settled (in one-sided-bound Step 2). Gaps: Data/Existence.lean partly unread; ~19 unchecked ?lean names (see report); 3 knowls bundle several defs. Next: derivatives-divisibility (resumed).
DONE: derivatives-divisibility (39 knowls, 26 full/1 outline; sidecar 43). Issues: merged declarations per knowl; 3 'setting' knowls with lean=[] may duplicate other areas; ~9 inferred ?lean names. Next: derivatives-vacuum (resumed).
DONE: derivatives-vacuum (95 knowls; lemmas 38 full/12 outline, theorems 13 full/10 outline; sidecar 35). 102 external ?lean names. Power series written R[\![X]\!] to avoid [[ collision -> CHECK other areas for literal [[ in math. Next: upper-objects (resumed).
DONE (partial depth): upper-objects (61 knowls; 12 full/21 outline/4 statement; sidecar 41). SECOND PASS NEEDED: Kernels/* (3 files), JetConjugatesAndBounds, ThetaLiftGauge, DefiniteKernelSize read head-only; Parameters(330+), Columns, Rows, RowChain, PoincareMap, CharactersAtLevel proofs skimmed. Doubts: HCParam.HasGap normalisation; own formula in chains-kill-ramified-source-forms part 4. Next: upper-seesaw (resumed).
DONE (thin reading): upper-seesaw (48 knowls; 13 full/26 outline; sidecar 46). Read with tactic lines filtered out except AdmissibleCombinations<640 and 3 main proofs -> SECOND PASS: NeighbourVacuum, AdmissibleEvaluation, UnfoldingStages, GoodDatum, Cut, SeesawIdentity, NeighbourLattice(2nd half). ~78 unchecked external ?lean names. Next: upper-divisibility (resumed). NOTE to self: tell agents economy != dropping proof lines.

2026-11-26 morning (new window). Lock re-armed (bp08z0h28).
DONE: upper-divisibility (60 knowls; 7 full/42 outline; all 15 files read in full incl. tactics; sidecar 46). Outlines could be upgraded with Magnitudes/Sizes open. Next: SECOND PASS upper-seesaw (resumed aecec73), then second pass upper-objects, then upper-elementary-divisors onward.
upper-seesaw 2nd pass: now 25 full/14 outline; 3 first-pass ERRORS found+fixed (thin reading produces wrong math -> never accept comment-only reading). Remaining verbatim: AdmissibleCombinations 640-907, StandardLines, EdgePairEvaluation, IntegralAsCosetSum, LevelIdeles, Frequency, NeighbourLattice 1-617 (third pass sent).
DONE (verbatim complete): upper-seesaw now 51 knowls, 35 full/7 outline. Next: SECOND PASS upper-objects (resumed a7e1079).
DONE (verbatim complete): upper-objects now 64 knowls, 16 full/14 outline; 4 first-pass errors fixed. Next: upper-elementary-divisors (resumed a0d7741), then spanning-core afe0da4, spanning-unfolding-a ad1d539, -b af8c29f, spanning-remaining-a a094940, -b aae24fb, spanning-mainterm abd8dc3, spanning-frames-a a6bedb9, -b ae63169, determinant-exchange a3ff942, determinant-chain ac5d393, onelift-comparison a1e43e9, onelift-values ade5b66.
STANDARD RESUME MESSAGE = 'depth terms' (verbatim reading incl. tactics, no filter, no subagents, stop in import order if short).
DONE: upper-elementary-divisors (67 knowls; 44 full/1 outline; sidecar 44). Gap: ElementaryDivisorTheorem.lean 476-612 statements only (consequences-of-large-degree outline). Scratchpad k.sh collision early on -> check spanning-core ids. Next: spanning-core (resumed afe0da4).
PARTIAL: spanning-core 52 knowls (22 full/11 outline; sidecar 67). REMAINING unread: Bessel/{Average,OpenCellBound,OpenCellPairing,LargeFunction,CutTailBound,SchurBound,FillingData} (continuation sent to afe0da4).
Window 3 (after 1pm 11-26): spanning-core continuation was cut by limit mid-Bessel; resumed afe0da4. Lock re-armed.
DONE: spanning-core 66 knowls (25 full/17 outline; sidecar 78), all 17 files verbatim. Next: spanning-unfolding-a (ad1d539).
DONE: spanning-unfolding-a 81 knowls (62 full/5 outline; sidecar 62). Folder has 19 files (not 22): a took first 11; b must take ONLY last 8: Setup, BesselLevelStructure, SquareExpansion, MomentBounds, Moments, Terms, Link, TermStructure. ~240 external ?lean names, some are structure fields. Next: spanning-unfolding-b (af8c29f).
REVIEW: friend's audit on origin/riemann2-review merged into riemann2 (reviews/riemann2-audit/: README, findings.tsv 353 findings (29 high/172 med/152 low), areas/<area>.md, lean-references.md (35 wrong ?lean names), structural-checks.md). PLAN: after current agent, send each finished area's author its areas/<area>.md to verify against Lean and apply; high first.
DONE: spanning-unfolding-b 89 knowls (61 full/1 outline; sidecar 47), 8 files verbatim. NOW: audit-fix passes, one author at a time in order: reduction-zeros ac5511e, reduction-main a14da12, derivatives-divisibility acebff8, derivatives-vacuum acc6db7, upper-objects a7e1079, upper-seesaw aecec73, upper-divisibility a902022, upper-elementary-divisors a0d7741, spanning-core afe0da4. Then forward: spanning-remaining-a...
AUDIT-FIX DONE: reduction-zeros (19/19 accepted). Next audit-fix: reduction-main (a14da12) incl. note: grh knowl should not claim DirichletLNonvanishingRightOfHalf.
AUDIT-FIX DONE: reduction-main (22/22 accepted). Next: derivatives-divisibility (acebff8); hint: chosen-places-and-characters finding answered by reduction-main/field-e-properties part 6.
AUDIT-FIX DONE: derivatives-divisibility (20/20; field-setting deleted; 38 knowls). Next: derivatives-vacuum (acc6db7).
Window 4 (after 10pm 11-26): derivatives-vacuum audit-fix cut by limit; resumed acc6db7.
REVIEW UPDATES merged (content HEAD 32adcbe6): reviews/riemann2-audit/updates/{b4aa180e,9712a76c}/ — verified 61 fixes resolved; NEW findings: spanning-core 26, spanning-unfolding-a 69, spanning-unfolding-b 53(+7 old open), derivatives-divisibility 8, reduction-main 2. prompt-audit.md now tells authors to read updates/*. Always `git fetch` + merge origin/riemann2-review at window start.
AUDIT QUEUE: derivatives-vacuum (running), upper-objects, upper-seesaw, upper-divisibility, upper-elementary-divisors, spanning-core, spanning-unfolding-a, spanning-unfolding-b, then re-touch derivatives-divisibility (8) + reduction-main (2). Then forward: spanning-remaining-a...
