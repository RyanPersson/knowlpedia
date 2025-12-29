---
title: "Totally bounded iff every sequence has a Cauchy subsequence"
description: "A metric set admits finite ε-nets for all ε>0 exactly when sequences have Cauchy subsequences"
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $E\subseteq X$.

The set $E$ is **{{< knowl id="totally-bounded-set" text="totally bounded" >}}** if for every $\varepsilon>0$ there exist points $x_1,\dots,x_N\in X$ such that
$
E\subseteq \bigcup_{j=1}^N {{< knowl id="open-ball" text="$B$" >}}(x_j,\varepsilon).
$

**Proposition**: $E$ is totally bounded if and only if every sequence in $E$ has a {{< knowl id="cauchy-sequence" text="Cauchy" >}} {{< knowl id="subsequence" text="subsequence" >}}.

This proposition is the "sequential form" of total boundedness and is the key step in proving that {{< knowl id="compact-iff-complete-totally-bounded" text="complete + totally bounded implies compact" >}}.

**Proof sketch**:
($\Rightarrow$) Let $(x_n)$ be a sequence in $E$. Cover $E$ by finitely many balls of radius $1$, so one ball contains infinitely many terms; pick a subsequence in that ball. Then cover $E$ by finitely many balls of radius $1/2$ and refine to a further subsequence inside one of those balls. Continue with radii $1/2^k$. The diagonal subsequence $(x_{n_k})$ satisfies $d(x_{n_k},x_{n_\ell})<2^{-k+1}$ for all $\ell\ge k$, hence is Cauchy.

($\Leftarrow$) If $E$ is not totally bounded, there exists $\varepsilon>0$ such that no finite collection of $\varepsilon$-balls covers $E$. Construct a sequence $(x_n)$ inductively by choosing $x_{n+1}\in E\setminus\bigcup_{j=1}^n B(x_j,\varepsilon)$. Then $d(x_n,x_m)\ge \varepsilon$ for $n\neq m$, so no subsequence can be Cauchy.
