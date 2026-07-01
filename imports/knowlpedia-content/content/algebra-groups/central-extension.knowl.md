+++
id = "algebra-groups/central-extension"
title = "Central Extension"
kind = "knowl"
summary = "An extension whose kernel lies in the center of the total group"
aliases = ["central-extension", "Central Extension"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/central-extension.md"
+++

An extension
$$
1 \to A \xrightarrow{\iota} E \xrightarrow{\pi} Q \to 1
$$

is a **central extension** if $\iota(A)$ is contained in the [[algebra-groups/center-of-group|center]] $Z(E)$. Equivalently, the kernel $A$ commutes with every element of $E$.

Central extensions are a special case of [[algebra-groups/group-extension|group extensions]] in which the "added part" sits centrally. In particular, $A$ is necessarily [[algebra-groups/abelian-group|abelian]], since every subgroup of the center is abelian.

**Examples:**
- The quaternion group fits into a central extension $1\to \{\pm 1\}\to Q_8\to Q_8/\{\pm1\}\to 1$.
- If $E$ is abelian, then every extension $1\to A\to E\to Q\to 1$ is central.
- For any group $G$, the quotient map $G\to G/Z(G)$ exhibits $G$ as a central extension of $G/Z(G)$ by $Z(G)$.
