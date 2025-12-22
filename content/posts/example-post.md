---
title: "Example Post: Testing Features"
date: 2025-12-21
summary: "A test post demonstrating math, code blocks, knowls, and more."
---

This post tests various features of the blog.

## Mathematics

Let's start with some inline math: the Euler identity $e^{i\pi} + 1 = 0$ is often called the most beautiful equation in mathematics.

Here's a display equation—the Cauchy-Schwarz inequality in a {{< knowl id="hilbert-space" text="Hilbert space" >}}:

$$|\langle x, y \rangle|^2 \leq \langle x, x \rangle \cdot \langle y, y \rangle$$

And a more complex example, the definition of the operator norm in a {{< knowl id="banach-space" text="Banach space" >}}:

$$\|T\| = \sup_{\|x\| \leq 1} \|Tx\| = \sup_{x \neq 0} \frac{\|Tx\|}{\|x\|}$$

## Code Blocks

### Python

```python
import numpy as np
from scipy.linalg import norm

def gram_schmidt(vectors):
    """Orthonormalize a set of vectors using Gram-Schmidt."""
    basis = []
    for v in vectors:
        w = v - sum(np.dot(v, b) * b for b in basis)
        if norm(w) > 1e-10:
            basis.append(w / norm(w))
    return np.array(basis)

# Example: orthonormalize R^3 vectors
V = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]], dtype=float)
Q = gram_schmidt(V)
print(Q @ Q.T)  # Should be approximately identity
```

### Lean 4

```lean
/-- A vector space over a field K -/
class VectorSpace (K : Type*) (V : Type*) [Field K] extends AddCommGroup V, Module K V

/-- The dual space of a vector space -/
def DualSpace (K : Type*) (V : Type*) [Field K] [AddCommGroup V] [Module K V] :=
  V →ₗ[K] K

theorem dual_dual_iso (K : Type*) (V : Type*) [Field K] [AddCommGroup V] [Module K V]
    [FiniteDimensional K V] :
    FiniteDimensional.finrank K (DualSpace K (DualSpace K V)) = FiniteDimensional.finrank K V := by
  simp [DualSpace, LinearMap.finrank_linearMap]
```

## Circular Knowl Test

Here's a test of circular references between knowls. Click through and see how deep you can go:

- {{< knowl id="concept-a" text="Concept A" >}} references B and C
- {{< knowl id="concept-b" text="Concept B" >}} references C and A
- {{< knowl id="concept-c" text="Concept C" >}} references A and B

The knowl system should handle this gracefully—each click opens a new panel, and you can nest arbitrarily deep even with circular references.

## Lorem Ipsum

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
