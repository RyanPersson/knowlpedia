+++
id = "thermodynamics/clausius-statement-second-law"
title = "Clausius statement of the second law"
kind = "knowl"
summary = "No cyclic device can transfer heat from a colder body to a hotter body without external work."
aliases = ["clausius-statement-second-law", "Clausius statement of the second law"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/clausius-statement-second-law.md"
+++

The Clausius statement is an operational form of the [[thermodynamics/second-law-thermodynamics|second law]]:

> It is impossible to construct a device operating in a cycle whose sole net effect is to transfer heat from a colder body to a hotter body.

In other words, a refrigerator or heat pump cannot move heat “uphill in [[thermodynamics/temperature-thermo|temperature]]” without consuming work from a [[thermodynamics/work-reservoir|work source]].

## Physical interpretation

When two bodies are placed in thermal contact through a [[thermodynamics/diathermal-wall|diathermal wall]], heat flows spontaneously from higher temperature to lower temperature until [[thermodynamics/thermal-equilibrium|thermal equilibrium]] is reached. The Clausius statement asserts that reversing this natural direction requires compensating changes elsewhere—most simply, an input of work.

## Key relations

- **Refrigerator energy balance.** In a cyclic refrigerator exchanging heats with a cold reservoir ($Q_c$ extracted) and a hot reservoir ($Q_h$ delivered), the [[thermodynamics/first-law-thermodynamics|first law]] gives
  $$
  Q_h = Q_c + W_{\text{in}},
  $$

  so moving heat from cold to hot requires positive work input $W_{\text{in}}>0$.

- **Equivalence to other statements.** The Clausius statement is equivalent to the [[thermodynamics/kelvin-planck-statement|Kelvin–Planck statement]]: if either were false, one could combine devices to violate the other. Both are summarized quantitatively by the [[thermodynamics/clausius-inequality|Clausius inequality]].

- **Entropy viewpoint.** For a closed system exchanging heat with reservoirs, the Clausius statement reflects that total [[thermodynamics/thermodynamic-entropy|entropy]] production is nonnegative, so spontaneous heat flow increases the entropy of the combined “system + reservoirs.”
