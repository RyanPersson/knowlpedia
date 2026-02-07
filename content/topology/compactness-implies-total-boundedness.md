---
title: "Compactness implies total boundedness"
description: "In a metric space, every compact set can be covered by finitely many small balls."
---

**Compactness implies total boundedness:** Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $K\subseteq X$ be {{< knowl id="compact-set" text="compact" >}}. Then $K$ is {{< knowl id="totally-bounded-set" text="totally bounded" >}}: for every $\varepsilon>0$ there exists a finite set $F\subseteq K$ such that
\[
K\subseteq \bigcup_{x\in F} B(x,\varepsilon),
\]
where $B(x,\varepsilon)$ denotes the {{< knowl id="open-ball" text="open ball" >}}.

This is one half of the standard metric characterization {{< knowl id="compact-iff-complete-totally-bounded" text="compact iff complete and totally bounded" >}}, complementing {{< knowl id="compactness-implies-completeness" text="compactness implies completeness" >}} and closely related to the existence of finite {{< knowl id="epsilon-net" text="epsilon-nets" >}}.
