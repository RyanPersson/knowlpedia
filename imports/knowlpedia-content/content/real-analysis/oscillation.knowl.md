+++
id = "real-analysis/oscillation"
title = "Oscillation"
kind = "knowl"
summary = "The amount a function varies on a set or interval."
aliases = ["oscillation"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/oscillation.md"
+++

An **oscillation** of a bounded function $f$ on a set $A\subseteq\mathbb R$ is the number
\[
\operatorname{osc}(f;A)=\sup\{|f(x)-f(y)|:x,y\in A\}.
\]
If $A$ is an interval, this equals $\sup\{f(x):x\in A\}-\inf\{f(x):x\in A\}$.

Oscillation is used in the [[real-analysis/oscillation-criterion|oscillation criterion]] for [[real-analysis/riemann-integrable-function|Riemann integrability]], and it also detects continuity: $x$ is a [[real-analysis/discontinuity-point|discontinuity point]] exactly when the oscillation over shrinking intervals around $x$ fails to go to $0$.

**Examples:**
- For $f(x)=x$ on $[0,1]$, one has $\operatorname{osc}(f;[0,1])=1$.
- If $f$ is the indicator function of $\mathbb Q\cap[a,b]$, then on every nontrivial subinterval $I\subseteq[a,b]$ one has $\operatorname{osc}(f;I)=1$.
