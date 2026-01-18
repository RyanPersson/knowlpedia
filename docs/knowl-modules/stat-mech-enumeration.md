# Statistical Mechanics & Thermodynamics — 500-level Knowl Enumeration (High Granularity)

## Prerequisite Modules

### Measure & Integration (probability-ready)

- Equality almost everywhere (a.e. equality)
- Measurable real-valued function integrable in the Lebesgue sense (Lebesgue integrable function)
- Lebesgue integral of a nonnegative measurable function
- Lebesgue integral of an integrable function
- Integrable function on a measure space (L^1 function)
- Essentially bounded function (L^∞ function)
- Essential supremum
- L^p norm (‖·‖_p)
- L^p space (L^p(Ω,𝔽,μ))
- Convergence almost everywhere
- Convergence in measure
- Convergence in L^p
- Uniform integrability
- Product measure (μ×ν)
- Pushforward measure (image measure)
- Change of variables formula for pushforward measures (measure-theoretic substitution)
- Monotone Convergence Theorem (Beppo Levi)
- Fatou's Lemma
- Dominated Convergence Theorem
- Tonelli's Theorem (nonnegative Fubini)
- Fubini's Theorem (integrable Fubini)
- Jensen's inequality (integral form)
- Minkowski inequality (L^p triangle inequality)
- Radon–Nikodym theorem
- Radon–Nikodym derivative as density (dν/dμ)
- Absolutely continuous measures (ν≪μ)
- Singular measures (ν⊥μ)

### Probability Theory & Information

- Probability measure (measure with total mass 1)
- Probability space (Ω,𝔽,ℙ)
- Event (measurable subset of Ω)
- Random variable (measurable map X:Ω→ℝ or X:Ω→S)
- Random vector (measurable map X:Ω→ℝ^d)
- Distribution (law) of a random variable (ℙ∘X^{-1})
- Expectation (𝔼[X])
- Expectation of a function of a random variable (𝔼[f(X)])
- Conditional expectation (𝔼[X|𝒢])
- Conditional probability (ℙ(A|𝒢))
- Independence of events
- Independence of σ-algebras
- Independence of random variables
- Identically distributed random variables
- IID sequence (independent and identically distributed)
- Variance (Var(X))
- Covariance (Cov(X,Y))
- Correlation coefficient
- Moment (𝔼[X^n])
- Moment generating function (MGF)
- Characteristic function (Fourier transform of law)
- Cumulant generating function (log MGF)
- Cumulant (κ_n)
- Markov inequality
- Chebyshev inequality
- Chernoff bound (exponential Markov inequality)
- Weak Law of Large Numbers
- Strong Law of Large Numbers
- Central Limit Theorem (CLT)
- Shannon entropy of a discrete distribution
- Differential entropy (continuous Shannon entropy)
- Relative entropy (Kullback–Leibler divergence)
- Gibbs inequality (nonnegativity of relative entropy)
- Total variation distance
- Pinsker inequality (TV bound by KL) (optional core prerequisite)
- Maximum entropy principle (information-theoretic form)

### Large Deviations (stat mech interface)

- Large deviation principle (LDP)
- Rate function
- Good rate function (compact level sets)
- Exponential tightness
- Log moment generating function (Λ(θ))
- Legendre transform of Λ (Cramér transform)
- Laplace principle (asymptotic integral principle)
- Varadhan's Lemma
- Cramér's Theorem (IID sums LDP)
- Sanov's Theorem (empirical measure LDP)
- Gärtner–Ellis Theorem
- Contraction principle

### Convex Duality & Thermodynamic Legendre Structure

- Convex conjugate (Fenchel conjugate) f*
- Legendre transform (smooth strictly convex case)
- Legendre–Fenchel transform (extended-real convex conjugate)
- Biconjugate f**
- Closed convex function (lower semicontinuous convex function)
- Subdifferential ∂f(x)
- Subgradient
- Supporting hyperplane to a convex function
- Fenchel–Young inequality
- Fenchel–Moreau theorem (f = f** for proper lsc convex f)
- Convex duality (primal/dual problems) (basic template)

### Asymptotics & Combinatorics (used constantly)

- Stirling's approximation (log n! asymptotics)
- Entropy of multinomial coefficients (Stirling + combinatorics)
- Laplace's method (finite-dimensional steepest descent)
- Saddle-point method (stationary phase for real exponentials)
- Method of types (empirical distribution counting) (optional prerequisite)

### Discrete Structures for Lattice Models

- Graph (vertex set and edge set)
- Finite graph
- Lattice ℤ^d as a graph (nearest-neighbor edges)
- Finite box Λ⊂ℤ^d (finite-volume region)
- Boundary of a finite region ∂Λ (graph boundary)
- Nearest-neighbor relation on ℤ^d
- Finite-range interaction on a lattice
- Translation-invariant interaction

### Quantum Structures (finite-dimensional baseline)

- Complex Hilbert space (finite-dimensional convention)
- Bounded operator on a Hilbert space
- Self-adjoint operator (observable)
- Spectrum of a self-adjoint operator (finite-dimensional)
- Trace of an operator
- Density operator (density matrix)
- Pure state (rank-one density operator)
- Mixed state
- Partial trace (reduced density matrix)
- Von Neumann entropy (S(ρ) = −Tr(ρ log ρ))
- Quantum relative entropy (Umegaki relative entropy)
- Golden–Thompson inequality (trace inequality)

## Core Definitions (atomic)

### Thermodynamic systems and processes

- Thermodynamic system
- Surroundings (environment)
- System boundary
- Isolated system
- Closed system
- Open system
- Thermodynamic state
- State variable (thermodynamic variable)
- State function
- Path function
- Thermodynamic process (path in state space)
- Quasistatic process
- Reversible process (thermodynamically reversible)
- Irreversible process
- Cyclic process
- Thermodynamic equilibrium state
- Mechanical equilibrium
- Thermal equilibrium
- Chemical equilibrium
- Zeroth-law equivalence relation (thermal equilibrium relation)
- Thermal reservoir (heat bath)
- Work reservoir (mechanical reservoir)
- Adiabatic wall
- Diathermal wall

### Thermodynamic quantities

- Internal energy (U)
- Heat (Q) as inexact differential δQ
- Work (W) as inexact differential δW
- Sign convention for work (work done by system vs on system)
- Entropy (thermodynamic entropy S)
- Temperature (T)
- Absolute temperature scale
- Pressure (P)
- Volume (V)
- Particle number (N)
- Chemical potential (μ)
- Enthalpy (H = U + PV)
- Helmholtz free energy (F = U − TS)
- Gibbs free energy (G = U + PV − TS)
- Grand potential (Ω = U − TS − μN) (Landau potential)
- Intensive variable
- Extensive variable
- Specific quantity (per particle) (e.g. u = U/N)
- Density (number density n = N/V)
- Energy density (ε = U/V)
- Entropy density (s = S/V)
- Heat capacity at constant volume (C_V)
- Heat capacity at constant pressure (C_P)
- Isothermal compressibility (κ_T)
- Adiabatic compressibility (κ_S)
- Thermal expansion coefficient (α_P)
- Response function (linear response coefficient)

### Thermodynamic structure

- Equation of state
- Fundamental relation (entropy representation S = S(U,V,N,…))
- Fundamental relation (energy representation U = U(S,V,N,…))
- Homogeneous function of degree 1 (extensivity axiom template)
- Euler relation for extensive systems (thermodynamic Euler equation)
- Gibbs–Duhem relation (constraint among intensives)
- Maxwell relation (cross-derivative identity)
- Thermodynamic stability (local stability notion)
- Concavity of entropy in extensive variables (stability form)
- Convexity of energy in entropy representation (stability form)
- Thermodynamic limit (N,V→∞ with N/V fixed)
- Thermodynamic limit of a state function (density limit)

### Classical statistical mechanics: microstates and measures

- Microstate (classical)
- Macrostate (macroscopic specification)
- Phase space Γ (classical phase space)
- Hamiltonian function H:Γ→ℝ (classical energy)
- Phase-space volume element (Liouville measure)
- Density of states g(E)
- Microcanonical shell (energy surface H=E)
- Microcanonical measure (uniform on energy shell)
- Canonical ensemble (Gibbs measure at fixed β)
- Grand canonical ensemble (Gibbs measure at fixed β,μ)
- Isothermal–isobaric ensemble (NPT ensemble)
- Generalized Gibbs ensemble (multiple constraints)
- Partition function (canonical) Z_N(β,V)
- Grand partition function Ξ(β,μ,V)
- Isothermal–isobaric partition function (Δ_N(β,P))
- Boltzmann entropy (microcanonical) S_B = k_B log Ω(E)
- Gibbs entropy (Shannon form) S_G = −k_B∫ρ log ρ
- Free energy (statistical) F = −k_B T log Z
- Pressure from partition function (p = (1/β) ∂_V log Z) (definition-as-formula)
- Ensemble average ⟨A⟩
- Fluctuation (centered observable A−⟨A⟩)
- Variance of an observable in an ensemble
- Covariance of two observables in an ensemble
- Correlation function (two-point function)
- Connected correlation function (cumulant / truncated correlation)
- Correlation length (definition via exponential decay rate)
- Susceptibility (derivative of order parameter w.r.t. field)
- Specific heat (fluctuation form template)

### Lattice statistical mechanics (spin systems)

- Spin space (single-site state space)
- Spin configuration (σ:Λ→S)
- Configuration space S^Λ
- Lattice Hamiltonian (finite-volume energy function)
- Interaction potential (Φ) (specification by finite subsets)
- Finite-range interaction
- Translation-invariant interaction
- External field (coupling term)
- Boundary condition (fixed boundary spins / periodic / free)
- Finite-volume Gibbs measure (DLR finite-volume measure)
- Partition function for a lattice system (finite-volume)
- Pressure (lattice) (free energy density with sign convention)
- Thermodynamic limit of pressure (lattice)
- Gibbs specification (family of conditional kernels)
- DLR equation (consistency condition)
- Infinite-volume Gibbs measure (DLR Gibbs state)
- Extremal Gibbs measure
- Mixture (convex combination) of Gibbs measures
- Pure phase (extremal translation-invariant Gibbs state)
- Phase transition (non-uniqueness of infinite-volume Gibbs measures)
- Spontaneous magnetization
- Spontaneous symmetry breaking
- Order parameter (general definition)
- Ising model (nearest-neighbor ±1 spins)
- Ferromagnetic Ising model (J≥0)
- Antiferromagnetic Ising model (J≤0)
- Potts model (q-state generalization)
- XY model (planar rotor model)
- Heisenberg model (O(3) spins)
- Lattice gas (occupation variables)
- Random-cluster model (Fortuin–Kasteleyn representation) (optional core)

### Quantum statistical mechanics (finite-volume baseline)

- Quantum system (Hilbert space + Hamiltonian)
- Quantum Hamiltonian (self-adjoint operator)
- Observable algebra (bounded operators on Hilbert space)
- Quantum microstate (pure state vector)
- Density operator (state)
- Gibbs state (quantum canonical state) ρ_β = e^{−βH}/Z
- Quantum partition function Z = Tr(e^{−βH})
- Quantum expectation value ⟨A⟩ = Tr(ρA)
- KMS condition (finite-dimensional version)
- Quantum correlation function (imaginary-time correlation)

## Core Axioms / Conventions

- Zeroth Law of Thermodynamics (thermal equilibrium defines temperature)
- First Law of Thermodynamics (energy conservation: dU = δQ − δW with convention)
- Second Law of Thermodynamics (entropy nondecrease for isolated systems)
- Clausius inequality (∮ δQ/T ≤ 0) (as postulate/axiom form)
- Kelvin–Planck statement of the second law (impossibility of 100% heat-to-work cycle)
- Clausius statement of the second law (no spontaneous heat flow cold→hot)
- Third Law of Thermodynamics (Nernst: entropy approaches constant as T→0) (convention/axiom)
- Extensivity postulate (U,S,V,N scale linearly in system size for short-range systems)
- Additivity postulate (weakly coupled subsystems add U,S,V,N)
- Boltzmann constant k_B (units convention)
- Inverse temperature β = 1/(k_B T) (notation convention)
- Natural units convention (k_B = 1) (optional)
- Logarithm convention (natural log ln)
- Thermodynamic limit convention (N,V→∞ with fixed density)
- Boundary condition convention for lattice limits (free vs periodic) (explicit)
- Canonical ensemble convention (fixed N,V,T)
- Grand canonical ensemble convention (fixed μ,V,T)
- Sign convention for pressure–volume work (δW = P dV vs −P dV)
- Chemical work convention (μ dN term placement)
- Entropy normalization convention (additive constant)

## Core Constructions / Objects

- Construction: entropy maximization for thermal contact (maximize S_total at fixed U_total)
- Construction: definition of temperature from entropy (1/T = ∂S/∂U) (construction-as-definition link)
- Construction: definition of pressure from entropy (P/T = ∂S/∂V)
- Construction: definition of chemical potential from entropy (−μ/T = ∂S/∂N)
- Construction: Legendre transform from S(U,V,N) to F(T,V,N)
- Construction: Legendre transform from U(S,V,N) to H(S,P,N)
- Construction: Legendre transform from U(S,V,N) to G(T,P,N)
- Construction: Legendre transform from F(T,V,N) to Ω(T,V,μ)
- Construction: canonical partition function from Hamiltonian (Z = ∫ e^{−βH} dλ)
- Construction: grand canonical partition function (Ξ = ∑_N e^{βμN} Z_N)
- Construction: free energy from partition function (F = −(1/β) log Z)
- Construction: thermodynamic observables as derivatives of log Z (E, P, N, …)
- Construction: fluctuation formulas from second derivatives of log Z (variance/covariance)
- Construction: cumulant generating function of an observable (log ⟨e^{tA}⟩)
- Construction: connected correlations as cumulants (derivatives of log generating function)
- Construction: microcanonical entropy from density of states (S(E)=k_B log g(E)ΔE) (discrete/continuous care)
- Construction: canonical measure as exponential tilt of microcanonical weights (heuristic-to-rigorous bridge)
- Construction: DLR specification from finite-volume Hamiltonians (conditional probabilities)
- Construction: infinite-volume Gibbs measure via weak limits of finite-volume measures
- Construction: transfer matrix for 1D nearest-neighbor models
- Construction: mean-field (variational) approximation via product measures
- Construction: Bogoliubov variational free-energy bound (trial Hamiltonian method)
- Construction: cluster expansion (polymer representation) (high-temperature construction)
- Construction: Mayer expansion for a classical gas (virial/cluster integrals) (optional core)
- Construction: reduced density matrix by partial trace (quantum subsystems)
- Construction: quantum thermal correlation via imaginary-time evolution (Kubo–Martin–Schwinger kernel)

## Core Theorems

### Thermodynamics

- Carnot theorem (maximum efficiency depends only on reservoir temperatures)
- Carnot efficiency formula (η_C = 1 − T_c/T_h) (as theorem)
- Clausius theorem (existence of entropy state function for reversible heat flow)
- Equivalence of Kelvin–Planck and Clausius statements (second law equivalence)
- Maxwell relations theorem (from exactness of differentials of thermodynamic potentials)
- Euler relation theorem for extensive systems (homogeneity implies Euler equation)
- Gibbs–Duhem theorem (differential constraint among intensive variables)
- Stability theorem: concavity of entropy implies thermodynamic stability inequalities
- Third law consequence: unattainability of absolute zero (formulation variant) (if included)

### Classical statistical mechanics

- Liouville's theorem (phase-space volume preservation under Hamiltonian flow)
- Equipartition theorem (quadratic degrees of freedom contribute (1/2)k_BT)
- Canonical identities: ⟨H⟩ = −∂_β log Z (energy derivative identity)
- Canonical identities: Var(H) = ∂_β^2 log Z (energy fluctuation identity)
- Pressure identity: P = (1/β) ∂_V log Z (canonical pressure theorem)
- Gibbs variational principle (free energy as inf over probability measures)
- Maximum entropy principle with constraints (Gibbs distribution solves constrained max entropy)
- Legendre duality theorem: free energy is Legendre–Fenchel transform of entropy density (under regularity)
- Equivalence of ensembles theorem (microcanonical vs canonical macrostate equivalence under strict concavity)
- Large-deviation formulation of equilibrium (canonical measure concentrates at entropy maximizers)

### Lattice systems (equilibrium)

- Existence of thermodynamic limit of pressure for finite-range translation-invariant interactions (subadditivity theorem)
- Existence of infinite-volume Gibbs measures for finite-range interactions (DLR existence theorem)
- Variational principle for pressure (Gibbs variational principle for lattice systems)
- Dobrushin uniqueness theorem (high-temperature uniqueness of Gibbs state)
- Exponential decay of correlations in the uniqueness region (high-temperature clustering theorem)
- Peierls argument (phase transition for 2D ferromagnetic Ising at low temperature)
- Griffiths inequalities (monotonicity/correlation inequalities for ferromagnets)
- FKG inequality (positive association under lattice condition)
- GKS inequalities (Griffiths–Kelly–Sherman inequalities) (optional core)
- Lee–Yang circle theorem (zeros of partition function for ferromagnetic Ising in complex field) (optional core)

### Quantum statistical mechanics (finite volume / basic)

- Gibbs state satisfies the KMS condition (finite-dimensional theorem)
- KMS condition implies Gibbs form for finite-dimensional systems (finite-volume converse)
- Golden–Thompson inequality (trace inequality used in free-energy bounds)

## Core Lemmas

- Exact differential criterion (closed 1-form + simply connected domain ⇒ exact) (thermo use)
- Integrating factor lemma for δQ (thermo entropy construction template)
- Fekete lemma (subadditive sequences: limit of a_n/n exists)
- Subadditivity lemma for log partition functions (finite-range interactions)
- Superadditivity lemma for entropy (additive subsystems)
- Stirling's formula (log n! = n log n − n + o(n))
- Laplace principle lemma (log ∫ e^{n f(x)} ≈ n sup f)
- Saddle-point lemma for sums (log ∑ e^{n a_i} ≈ n max a_i)
- Jensen inequality lemma (expectation form) (⟨e^{X}⟩ ≥ e^{⟨X⟩})
- Gibbs inequality lemma (KL ≥ 0) (variational principle backbone)
- Chernoff bounding lemma (tail bound via exponential moments)
- Peierls–Bogoliubov inequality (free-energy upper bound via trial Hamiltonian)
- Golden–Thompson lemma (Tr e^{A+B} ≤ Tr(e^A e^B))
- Cluster expansion convergence criterion (Kotecký–Preiss condition) (if cluster expansions included)
- Griffiths monotonicity lemma (∂⟨σ⟩/∂h ≥ 0 in ferromagnets) (if inequalities included)

## Core Propositions

### Thermodynamic identities and stability

- Proposition: entropy maximization yields equality of temperatures at equilibrium
- Proposition: entropy maximization yields equality of pressures at mechanical equilibrium
- Proposition: entropy maximization yields equality of chemical potentials at diffusive equilibrium
- Proposition: Legendre transform swaps natural variables (e.g. F(T,V,N) natural variables T,V,N)
- Proposition: Maxwell relations from equality of mixed partial derivatives of potentials
- Proposition: positivity of C_V as stability condition (canonical ensemble)
- Proposition: compressibility positivity as stability condition
- Proposition: convexity of free energy in temperature/inverse temperature
- Proposition: concavity of entropy in energy (microcanonical stability)
- Proposition: equivalence between response functions and variances (fluctuation–response identities)

### Canonical / grand-canonical derivative identities

- Proposition: ⟨N⟩ = ∂_{(βμ)} log Ξ (grand canonical particle number identity)
- Proposition: Var(N) = ∂_{(βμ)}^2 log Ξ (number fluctuation identity)
- Proposition: Cov(H,N) = −∂_β∂_{(βμ)} log Ξ (mixed fluctuation identity)
- Proposition: susceptibility equals β times variance of magnetization (Ising with field)
- Proposition: connected correlations are derivatives of log generating functional

### Lattice Gibbs structure

- Proposition: DLR consistency implies Markov property for finite-range interactions (informal-to-formal)
- Proposition: extremal Gibbs measures are ergodic under translations (standard setting)
- Proposition: phase coexistence implies non-differentiability of pressure in field (first-order signature) (setting-dependent)

### Quantum equilibrium

- Proposition: von Neumann entropy is concave on density operators
- Proposition: quantum relative entropy is monotone under partial trace (data processing inequality) (optional core)

## Core Corollaries

- Corollary: reversible adiabatic process has constant entropy (isentropic process)
- Corollary: Carnot theorem implies absolute temperature scale uniqueness (up to scale)
- Corollary: Maxwell relations imply standard response identities (e.g. ∂S/∂V|_T = ∂P/∂T|_V)
- Corollary: canonical energy fluctuations scale like C_V (Var(E) = k_B T^2 C_V)
- Corollary: in the thermodynamic limit, relative energy fluctuations vanish for stable short-range systems (self-averaging)
- Corollary: uniqueness region implies analyticity of pressure (no phase transition) (setting-dependent)
- Corollary: high-temperature uniqueness implies exponential decay of correlations (clustering)
- Corollary: multiple Gibbs measures imply symmetry breaking (with symmetric Hamiltonian + field=0) (setting-dependent)
- Corollary: KMS condition yields periodicity in imaginary time (finite-temperature correlation periodicity)

## Core Equivalences (TFAE packages)

- TFAE: Second law formulations — classical thermodynamics
  - Condition: Kelvin–Planck statement holds (no 100% heat→work cycle)
  - Condition: Clausius statement holds (no spontaneous cold→hot heat flow)
  - Condition: Clausius inequality ∮ δQ/T ≤ 0 holds for cycles
  - Condition: Existence of entropy state function S with dS ≥ δQ_rev/T (entropy axiom form)
  - Condition: Carnot efficiency bound η ≤ 1 − T_c/T_h holds for all engines

- TFAE: Thermodynamic stability for simple compressible systems — equilibrium criterion package
  - Condition: entropy S(U,V,N) is concave in (U,V,N) (appropriate variables)
  - Condition: energy U(S,V,N) is convex in (S,V,N)
  - Condition: heat capacity C_V ≥ 0 (at fixed V,N)
  - Condition: isothermal compressibility κ_T ≥ 0 (at fixed T,N)
  - Condition: Hessian definiteness of the relevant potential (e.g. F(T,V,N) convex in T, concave/convex in V depending on sign conventions)

- TFAE: Legendre duality between entropy density and free energy density — thermodynamic limit setting
  - Condition: free energy density f(β) equals Legendre–Fenchel transform of entropy density s(e)
  - Condition: entropy density s(e) equals (minus) Legendre–Fenchel transform of f(β)
  - Condition: canonical equilibrium energy e(β) satisfies β ∈ ∂s(e)
  - Condition: microcanonical and canonical ensembles are equivalent at energy e (macrostate equivalence)

- TFAE: Gibbs measure characterizations — lattice spin systems (short-range, standard setting)
  - Condition: μ satisfies the DLR equations for the interaction Φ
  - Condition: μ is consistent with the Gibbs specification (conditional kernels)
  - Condition: μ minimizes free energy density among translation-invariant measures (variational principle)
  - Condition: μ has the correct local conditional probabilities (quasilocality + specification)

- TFAE: Phase transition indicators — lattice equilibrium (model-dependent)
  - Condition: non-uniqueness of infinite-volume Gibbs measures at given (β,h)
  - Condition: discontinuity of an order parameter as h→0± (symmetry breaking signature)
  - Condition: non-analyticity (non-differentiability) of pressure/free energy in a control parameter
  - Condition: long-range order (non-decaying correlations) in an extremal Gibbs state (setting-dependent)

- TFAE: Finite-dimensional quantum equilibrium — β-equilibrium package
  - Condition: ρ is a Gibbs state ρ ∝ e^{−βH}
  - Condition: ρ satisfies the β-KMS condition for the Heisenberg dynamics α_t(A)=e^{itH}Ae^{−itH}
  - Condition: ρ minimizes (Tr(ρH) − (1/β)S_vN(ρ)) over density operators (free-energy variational principle)

## Standard Examples / Counterexamples

- Ideal gas (classical) as canonical ensemble example
- Sackur–Tetrode entropy formula (ideal gas entropy) (as example result-object)
- Van der Waals gas (phenomenological equation of state) (phase transition example)
- Two-level system (paramagnet) (negative temperature example)
- Classical harmonic oscillator (equipartition example)
- Quantum harmonic oscillator (Bose occupation example)
- Einstein solid (collection of quantum oscillators) (heat capacity example)
- Debye model (phonon gas) (low-temperature C_V ∼ T^3 example) (optional core)
- Curie–Weiss (mean-field Ising) model (mean-field phase transition example)
- 1D Ising model (no phase transition at finite T) (counterexample to naive expectations)
- 2D Ising model (phase transition) (standard example)
- Lattice gas ↔ Ising mapping (example of ensemble equivalence/inequivalence contexts)
- Long-range interaction model (ensemble inequivalence example) (e.g. mean-field with constraints)
- Microcanonical negative heat capacity example (self-gravitating systems) (extension/counterexample)
- Bose–Einstein condensation in ideal Bose gas (common extension example)
- Degenerate Fermi gas (Sommerfeld expansion example) (common extension example)

## Common Extensions

### Definitions

- Microcanonical entropy density s(e) (thermodynamic limit definition)
- Pressure (thermodynamic) as log partition function density
- Surface tension (interface free energy per area)
- Metastable state (local free-energy minimum notion)
- Large-deviation rate function for empirical magnetization (Curie–Weiss)
- Mean-field approximation (product-measure variational ansatz)
- Landau free energy functional (order-parameter functional)
- Spontaneous symmetry breaking (group action on state space)
- Continuous symmetry (O(n) invariance) in spin systems
- Critical point (endpoint of first-order line)
- Critical exponent (α,β,γ,ν,η,δ, …)
- Scaling relation between critical exponents (Rushbrooke/Josephson/etc.) (as definition object)
- Renormalization group transformation (RG map on couplings)
- Fixed point of RG (critical fixed point)
- Universality class (same critical exponents/scaling limits)
- Kosterlitz–Thouless transition (topological transition definition)
- Topological defect (vortex) in XY-type models
- Correlation function in momentum space (structure factor)
- Ornstein–Zernike form (definition of correlation-length extraction)
- Virial coefficients (B_2, B_3, …)
- Cluster integrals (Mayer coefficients)
- Canonical ensemble equivalence breakdown (nonconcave entropy region) (definition object)
- Nonequilibrium steady state (NESS) (basic definition)
- Detailed balance (Markov process equilibrium condition)
- Markov chain (discrete-time) (if stochastic dynamics included)
- Markov semigroup (continuous-time) (if stochastic dynamics included)
- Master equation (Kolmogorov forward equation)
- Boltzmann equation (kinetic equation definition)
- H-functional (Boltzmann H) (definition object)
- Fluctuation theorem (Crooks relation definition)
- Jarzynski equality (definition-as-identity object)
- Work distribution in nonequilibrium protocols (definition)
- Free energy difference (ΔF) from nonequilibrium work (object)

### Theorems / Results

- Onsager solution of the 2D Ising model (exact free energy) (optional, instructor-dependent)
- Mermin–Wagner theorem (no continuous-symmetry breaking in d≤2 for short-range) (optional)
- Kosterlitz–Thouless theorem (vortex unbinding transition mechanism) (optional)
- Pirogov–Sinai theory (low-temperature phase diagrams) (advanced extension)
- Cluster expansion theorem (analyticity at high temperature/low activity) (extension)
- Virial expansion convergence theorem (gas phase) (extension)
- Lee–Yang theorem extensions (other ferromagnetic models) (extension)
- Central limit theorem for fluctuations in high-temperature Gibbs states (extension)
- Donsker–Varadhan large deviations for empirical measures (extension)
- Hydrodynamic limit theorem (microscopic → macroscopic PDE) (extension)
- Boltzmann H-theorem (entropy production for Boltzmann equation) (extension)
- Green–Kubo relations (transport coefficients as time-correlation integrals) (extension)
- Fluctuation–dissipation theorem (linear response) (extension)
- Kubo formula (linear response) (extension)
- Jarzynski equality theorem (nonequilibrium work relation) (extension)
- Crooks fluctuation theorem (forward/reverse work distributions) (extension)

### TFAE packages

- TFAE: Ensemble equivalence vs nonequivalence — long-range / nonconcave entropy setting
  - Condition: entropy density is concave (supporting line exists everywhere)
  - Condition: microcanonical and canonical Legendre duality is involutive (no gap)
  - Condition: canonical equilibrium macrostates match microcanonical ones (no forbidden energies)
  - Condition: no negative heat capacity region in microcanonical description

- TFAE: Detailed balance and equilibrium for Markov dynamics (if stochastic processes included)
  - Condition: π(x)P(x,y)=π(y)P(y,x) (reversibility)
  - Condition: π is stationary and generator is self-adjoint in L^2(π)
  - Condition: entropy production rate is zero in stationarity

- TFAE: Linear response formulations (if included)
  - Condition: Kubo formula for response coefficient holds
  - Condition: fluctuation–dissipation relation links response to equilibrium correlations
  - Condition: susceptibility equals integrated time-correlation (Green–Kubo form)
