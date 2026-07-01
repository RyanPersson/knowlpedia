+++
id = "fiber-bundles/ehresmann-connection"
title = "Ehresmann connection"
kind = "knowl"
summary = "A choice of horizontal subspaces complementary to the vertical tangent spaces of a fibered manifold."
aliases = ["ehresmann-connection", "Ehresmann connection"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/ehresmann-connection.md"
+++

Let $\pi:E\to M$ be a surjective submersion between smooth manifolds (a fibered manifold). The map $\pi$ is a [[fiber-bundles/smooth-map|smooth map]], so it has a differential $d\pi:TE\to TM$ between the [[fiber-bundles/tangent-bundle|tangent bundles]].

Define the **vertical subbundle**
\[
VE:=\ker(d\pi)\subset TE.
\]

**Definition.** An Ehresmann connection on $\pi:E\to M$ is a choice of a [[fiber-bundles/horizontal-subbundle|horizontal subbundle]] $HE\subset TE$ such that, as vector bundles over $E$,
\[
TE = HE \oplus VE.
\]
Equivalently, it is a smooth splitting of the short exact sequence
\[
0 \longrightarrow VE \longrightarrow TE \xrightarrow{d\pi} \pi^*TM \longrightarrow 0,
\]
or, equivalently again, a smooth projection $K:TE\to VE$ with $K|_{VE}=\mathrm{id}$ (so that $HE=\ker K$).

An Ehresmann connection determines horizontal lifts and hence [[fiber-bundles/parallel-transport|parallel transport]] along curves. On a [[fiber-bundles/principal-g-bundle|principal G-bundle]], every [[fiber-bundles/principal-connection|principal connection]] induces an Ehresmann connection whose horizontal spaces are $G$-equivariant.

## Examples
1. **Product bundle.** For $E=M\times F$ with $\pi(x,f)=x$, the vertical bundle is $0\oplus TF$, and the choice $HE:=TM\oplus 0$ defines an Ehresmann connection (the “product connection”).
2. **Connection on a vector bundle induces horizontals on the total space.** A linear connection on a vector bundle $E\to M$ canonically defines horizontal subspaces in $TE$ (viewed as “directions of infinitesimal parallel translation of vectors in the fiber”).
3. **From principal connections.** If $P\to M$ is a principal $G$-bundle with principal connection, the horizontal subspaces are the kernels of the connection 1-form at each point, giving an Ehresmann connection on $P\to M$.
