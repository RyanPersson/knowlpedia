---
title: "$L$-Group and Satake Parameter"
description: "The semidirect product and the conjugacy class encoding unramified local data"
---

For a split reductive $G$ over a field with Galois/Weil group $\Gamma$, the **$L$-group** is a semidirect product ${}^LG:=\Gamma\ltimes \widehat G$, where $\Gamma$ acts on $\widehat G$ via pinned automorphisms (see {{< knowl id="pinned-automorphisms" section="langlands-letter/knowls" text="pinning" >}}).

In the letter, $\Gamma=\mathrm{Gal}(K/k)$ and ${}^LG$ is written as $\Gamma\ n_\delta\ cG$.

At an unramified prime $p$, a Hecke eigencharacter gives a **Satake parameter** $\alpha_p$: a semisimple conjugacy class in ${}^LG$ whose projection to $\Gamma$ is (a choice of) {{< knowl id="frobenius-unramified" section="langlands-letter/knowls" text="Frobenius" >}}.

Given a complex representation $\pi:{}^LG\to \mathrm{GL}(V)$, the associated local factor is
$
L_p(s,\pi,\phi)=\det(1-\pi(\alpha_p)\,p^{-s})^{-1}.
$
