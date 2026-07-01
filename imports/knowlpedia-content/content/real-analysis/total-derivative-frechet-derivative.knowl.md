+++
id = "real-analysis/total-derivative-frechet-derivative"
title = "Total derivative (Fréchet derivative in ℝ^k)"
kind = "knowl"
summary = "The linear map Df(a) giving the best first-order approximation f(a+h)=f(a)+Df(a)h+o(‖h‖)."
aliases = ["total-derivative-frechet-derivative", "Total derivative (Fréchet derivative in ℝ^k)"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/total-derivative-frechet-derivative.md"
+++

Let $U\subseteq\mathbb{R}^k$ be [[topology/open-set|open]] and let $f:U\to\mathbb{R}^m$. The function $f$ is **(Fréchet) differentiable at $a\in U$** if there exists a [[linear-algebra/linear-map|linear map]] $A:\mathbb{R}^k\to\mathbb{R}^m$ such that
$$
\lim_{h\to 0}\frac{\|f(a+h)-f(a)-A h\|_2}{\|h\|_2}=0.
$$

The map $A$ is uniquely determined when it exists and is called the **(total) derivative** of $f$ at $a$, denoted $Df(a)$.

This definition captures the best linear approximation of $f$ near $a$. In coordinates, $Df(a)$ is represented by the [[real-analysis/jacobian-matrix|Jacobian matrix]] $J_f(a)$ when $f$ has continuous [[real-analysis/partial-derivative|partial derivatives]].

**Examples:**
- If $f(x)=Ax+b$ is affine (with $A$ an $m\times k$ matrix), then $Df(a)=A$ for all $a$.
- If $f:\mathbb{R}^2\to\mathbb{R}$, $f(x,y)=x^2+y^2$, then $Df(a)$ is the linear map $h\mapsto 2\langle a,h\rangle$ (equivalently, gradient dot $h$).
- Existence of all partial derivatives at $a$ does not necessarily imply existence of $Df(a)$ (Fréchet differentiability).
