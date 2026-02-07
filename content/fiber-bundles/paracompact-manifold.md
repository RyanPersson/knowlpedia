---
title: "Paracompact manifold"
description: "A smooth manifold whose underlying topological space is paracompact, enabling global constructions via partitions of unity."
---

A {{< knowl id="smooth-manifold" text="smooth manifold" >}} $M$ is called **paracompact** if its underlying topological space is {{< knowl id="paracompact-topological-space" text="paracompact" >}} (and, in the usual manifold conventions, Hausdorff).

Paracompactness is the standard condition that guarantees the existence of smooth partitions of unity and allows one to globalize local data (metrics, connections, differential forms defined on charts, and so on).

## Key consequence
On a paracompact manifold, every open cover admits a {{< knowl id="partition-of-unity-subordinate-to-an-open-cover" text="smooth partition of unity subordinate to that cover" >}}.

In many texts, paracompactness is built into the definition of a smooth manifold (often via second countability), precisely to ensure this consequence.

## Examples
1. **Euclidean spaces and standard manifolds.**  
   $\mathbb R^n$, spheres, tori, and any manifold obtained by gluing finitely or countably many charts in the usual way are paracompact.

2. **Compact manifolds.**  
   Every compact manifold is paracompact (compactness implies paracompactness at the topological level).

3. **A standard nonexample (topological).**  
   The long line is a 1-dimensional topological manifold that is not second countable and is not paracompact; it illustrates why paracompactness (or a countability hypothesis) is not automatic for all manifolds.
