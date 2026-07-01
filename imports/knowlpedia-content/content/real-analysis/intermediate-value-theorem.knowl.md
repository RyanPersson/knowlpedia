+++
id = "real-analysis/intermediate-value-theorem"
title = "Intermediate value theorem"
kind = "knowl"
summary = "A continuous function on an interval takes all values between its endpoint values."
aliases = ["intermediate-value-theorem", "Intermediate value theorem"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/intermediate-value-theorem.md"
+++

**Intermediate value theorem:** Let $f:[a,b]\to\mathbb{R}$ be continuous on $[a,b]$. If $y$ is any number between $f(a)$ and $f(b)$ (that is, $\min\{f(a),f(b)\}\le y\le \max\{f(a),f(b)\}$), then there exists $c\in[a,b]$ such that
$$
f(c)=y.
$$

This is one of the basic consequences of being a [[topology/continuous-map|continuous map]] on an [[real-analysis/interval|interval]]. A notable application is [[real-analysis/darboux-theorem|Darboux's theorem]], which shows that derivatives also satisfy an intermediate value property.
