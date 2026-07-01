+++
id = "real-analysis/newton-leibniz-formula"
title = "Newton–Leibniz formula"
kind = "knowl"
summary = "If F is an antiderivative of f, then the integral of f equals F(b)-F(a)"
aliases = ["newton-leibniz-formula", "Newton–Leibniz formula"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/newton-leibniz-formula.md"
+++

Let $f:[a,b]\to\mathbb{R}$ be [[real-analysis/continuity-on-a-set|continuous]] and let $F:[a,b]\to\mathbb{R}$ satisfy $F'(x)=f(x)$ for all $x\in(a,b)$.

**Corollary (Newton–Leibniz)**:
$
\int_a^b f(x)\,dx = F(b)-F(a).
$

This is the standard evaluation rule for definite integrals using [[real-analysis/antiderivative|antiderivatives]].

**Connection to parent theorem**:
This is the [[real-analysis/fundamental-theorem-of-calculus-i|fundamental theorem of calculus]] (Part II).
