+++
id = "fiber-bundles/vertical-vector-field"
title = "Vertical vector field"
kind = "knowl"
summary = "A vector field on the total space of a fibered manifold that is tangent to every fiber."
aliases = ["vertical-vector-field", "Vertical vector field"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/vertical-vector-field.md"
+++

Let \(\pi:E\to M\) be a [[fiber-bundles/fibered-manifold|fibered manifold]]. A [[fiber-bundles/vector-field|vector field]] \(X\) on \(E\) is **vertical** if for every \(e\in E\),
\[
X_e\in V_eE\quad\text{equivalently}\quad d\pi_e(X_e)=0,
\]
where \(V_eE\) is the [[fiber-bundles/vertical-tangent-space|vertical tangent space]] at \(e\).

Equivalently, \(X\) is a smooth section of the [[fiber-bundles/vertical-subbundle|vertical subbundle]] \(VE\subset TE\). Any integral curve of a vertical vector field lies entirely inside a single fiber \(E_x\). Consequently, wherever the local flow of \(X\) is defined, it yields fiberwise local [[fiber-bundles/diffeomorphism|diffeomorphisms]] of \(E\) covering \(\mathrm{id}_M\); in particular, each time-\(t\) map is a [[fiber-bundles/fiber-preserving-map|fiber-preserving map]] over \(\mathrm{id}_M\).

## Examples
1. **Product projection:** on \(M\times F\to M\), any field of the form \(X_{(x,f)}=(0,Y_{(x,f)})\) (no component along \(M\)) is vertical; for instance \(X(x,f)=(0,Y_f)\) for a fixed vector field \(Y\) on \(F\).
2. **Principal bundles:** on a [[fiber-bundles/principal-g-bundle|principal G-bundle]] \(P\to M\), each \(\xi\) in the [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\) defines a vertical fundamental vector field \(\xi_P\) generating the right \(G\)-action.
3. **Vector bundles:** on a [[fiber-bundles/vector-bundle|vector bundle]] \(E\to M\), the Euler (radial) vector field that differentiates fiberwise scalar multiplication \(t\cdot e\) is vertical.
