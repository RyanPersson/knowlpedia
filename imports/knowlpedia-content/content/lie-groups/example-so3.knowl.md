+++
id = "lie-groups/example-so3"
title = "Example: and rotations"
kind = "knowl"
summary = "The Lie algebra of consists of real skew-symmetric matrices; exponentials are rotation matrices."
aliases = ["example-so3", "Example: and rotations"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/example-so3.md"
+++

Let [[lie-groups/special-orthogonal-group|$SO(3)$]] be the rotation group. Its Lie algebra is [[lie-groups/orthogonal-lie-algebra|$\mathfrak{so}(3)$]], the real skew-symmetric $3\times 3$ matrices with bracket $[A,B]=AB-BA$.

## A concrete basis and bracket computation
Set
\[
A_1=\begin{pmatrix}0&0&0\\0&0&-1\\0&1&0\end{pmatrix},\quad
A_2=\begin{pmatrix}0&0&1\\0&0&0\\-1&0&0\end{pmatrix},\quad
A_3=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&0\end{pmatrix}.
\]
Direct multiplication gives the familiar relations
\[
[A_1,A_2]=A_3,\qquad [A_2,A_3]=A_1,\qquad [A_3,A_1]=A_2.
\]
Thus $\mathfrak{so}(3)$ is 3-dimensional and simple as a real Lie algebra (and closely related to [[lie-groups/example-su2|$SU(2)$]] via a covering).

Equivalently, identifying $(a_1,a_2,a_3)\in\mathbb R^3$ with $a_1A_1+a_2A_2+a_3A_3$ turns the Lie bracket into the cross product on $\mathbb R^3$.

## Exponential = rotations (explicit)
For $\theta\in\mathbb R$, consider $\theta A_3$. Since $A_3$ acts as an infinitesimal rotation in the $(x,y)$-plane, the [[lie-groups/exponential-map-lie-group|exponential map]] yields
\[
\exp(\theta A_3)=
\begin{pmatrix}
\cos\theta & -\sin\theta & 0\\
\sin\theta & \cos\theta & 0\\
0&0&1
\end{pmatrix},
\]
the rotation about the $z$-axis by angle $\theta$. Similar formulas hold for $\exp(\theta A_1)$ and $\exp(\theta A_2)$.

## Topology note
$SO(3)$ is connected but not simply connected. Its universal cover is [[lie-groups/example-su2|$SU(2)$]], with a 2-to-1 covering homomorphism (see [[lie-groups/covering-lie-group|covering Lie groups]] and [[lie-groups/spin-group|$\mathrm{Spin}(3)$]]).
