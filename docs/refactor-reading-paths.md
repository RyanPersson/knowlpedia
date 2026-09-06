# Refactor reading paths

This note records two small end-to-end exercises used while reviewing the
functional-analysis and ring foundations. They test whether prerequisite links
form a usable route, whether conventions remain stable as a reader follows the
route, and where the route still depends on material outside this batch.

## Functional path

Read `linear-algebra/vector-space` → `linear-algebra/inner-product` →
`linear-algebra/inner-product-space` → `linear-algebra/hilbert-space`, then
continue to `linear-algebra/banach-space` and
`topology/complete-metric-space`.

Exercise: explain why the polynomial space on `[0,1]` is an inner-product
space but is not complete for its induced norm, while `L²(X, μ)` is a Hilbert
space after identifying functions equal almost everywhere. As a check, state
which scalar convention is being used at each step: vector spaces are over an
arbitrary field, while the normed and inner-product path specializes to `R` or
`C`; inner products are linear in the first argument and
conjugate-linear in the second; the GNS form is `φ(b* a)` with the same
linearity convention.

The operator-algebra continuation is `operator-algebras/cstar-algebra` →
`operator-algebras/positive-linear-functional` →
`operator-algebras/gns-construction`, with `linear-algebra/hilbert-space` as
the ambient space. Exercise: for point evaluation on `C(X)`, identify the
null space, quotient, cyclic vector, and resulting one-dimensional
representation. This checks that the convention remains `⟨[a],[b]⟩ =
φ(b* a)` all the way through the construction.

The review checked the following boundaries: `vector-space` depends on the
field/set/function foundations; `inner-product-space` depends on both the
underlying vector space and inner product; completeness is supplied by the
metric-space path; and `L²` is an almost-everywhere quotient. The remaining
boundary assumptions are the definitions of Cauchy and metric spaces, the
measure-theory construction of `L²`, and the theorem that polynomial
functions are dense in the relevant continuous-function spaces. Those are
deliberately outside this focused batch.

Substantive references checked: Hunter, *An Introduction to Analysis*,
Chapter 6 (normed and Hilbert spaces),
[PDF](https://www.math.ucdavis.edu/~hunter/book/ch6.pdf); and Gressman's
UPenn notes, “Advanced Analysis,” Sections 1–5 of the Hilbert-space chapter,
[HTML](https://www2.math.upenn.edu/~gressman/analysis/10-hilbertspaces.html).

## Ring path

Read `shared-foundations/binary-operation` → `algebra-groups/group` →
`algebra-groups/abelian-group` → `algebra-rings/ring` → `algebra-rings/unital-ring` → `algebra-rings/field`,
then branch from `algebra-rings/ring` to `algebra-rings/ideal`.

Exercise: identify where the identity element first becomes an assumption,
and say why a field must be unital even though the repository's general ring
definition permits nonunital rings. On the branch, explain why an ideal is
defined without requiring the ambient ring to be commutative or unital.

The review checked the repository's conventions: rings may be nonunital;
ring homomorphisms need not preserve an identity; `unital-ring` adds the
identity; and `field` therefore depends on the unital variant. The remaining
boundary assumptions include the linked monoid and unit definitions and later
quotient-ring theorems. The direct binary-operation, group, abelian-group, and
left/right/two-sided ideal definitions were read in this batch.

The ring manifest records the substantive text actually checked: Jonathan D.
H. Smith, *Introduction to Abstract Algebra* (2015), Definition 6.1 and
Remarks 6.2–6.3 (book pp. 129–130; PDF pp. 142–143) for the nonunital,
unital, and commutative ring conventions; §6.4 (book pp. 137–140; PDF
pp. 150–153) for unital versus nonunital homomorphisms; and Definition 6.26
and Proposition 6.27 (book pp. 139–140; PDF pp. 152–153) for ideals and
kernels. [Accessible PDF](https://ece.uprm.edu/~domingo/inel8396/Smith,%20Jonathan%20D.%20H%20-%20Introduction%20to%20abstract%20algebra%20(2015).pdf).
The text explicitly supports the repository's convention, while its
unital-homomorphism convention is recorded as a deliberate boundary choice
in the knowl. The field knowl also scopes its ideal characterization to
commutative unital nonzero rings; without those hypotheses, the statement
would be false for the repository's general nonunital rings.
