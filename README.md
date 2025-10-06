# Quantum Market Simulation ⚛️

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Qiskit](https://img.shields.io/badge/Qiskit-0.45+-blue?logo=qiskit)
![License](https://img.shields.io/badge/License-MIT-green)

This project uses **Qiskit**, IBM's quantum computing SDK, to create a conceptual model of a digital market. It's not a literal simulation, but a powerful **analogy** that uses the principles of quantum mechanics to represent the complex, probabilistic, and interconnected nature of a competitive landscape.

The core idea is to frame a market analysis tool not as a simple data query, but as an act of **measurement** that collapses a "quantum-like" state of infinite market possibilities into a single, observable reality.

---

### The Analogy Explained

This script models a market with three main competitors, using a 3-qubit quantum circuit. The process mirrors the transition from market uncertainty to a concrete market snapshot.

#### 1. The Market in Superposition (`H` Gate)
-   **Quantum Concept:** A qubit can exist as both 0 and 1 simultaneously. The Hadamard (H) gate puts a qubit into an equal superposition of both states.
-   **Market Analogy:** Before we run our analysis, the market exists in a state of pure potential. All outcomes are possible. Is Competitor A strong or weak? Is Competitor C launching a new product? In this model, the market is in a superposition of **all 8 possible states at once**, representing total uncertainty.

#### 2. Competitors Are Entangled (`CX` Gate)
-   **Quantum Concept:** Entanglement is a phenomenon where the state of one qubit becomes intrinsically linked to the state of another, no matter the distance between them.
-   **Market Analogy:** Competitors are never independent. An aggressive ad campaign from one company directly affects the market share of another. We use Controlled-NOT (CNOT/CX) gates to **entangle** our competitor qubits, simulating these market influences and shifting the probabilities of certain outcomes.

#### 3. Analysis as Measurement (`Measure` Operation)
-   **Quantum Concept:** The act of measuring a qubit collapses its superposition into a definite classical state (either 0 or 1).
-   **Market Analogy:** Running our market intelligence application is an act of measurement. We take a "snapshot" of the market at a single point in time. This act forces the cloud of possibilities to collapse into **one single, observable reality**. The script simulates this measurement 1024 times to reveal the underlying probability distribution of the different market states.

---

### How to Run the Simulation

#### Prerequisites
You need to have Python and Qiskit installed.
```bash
pip install qiskit qiskit-aer```

#### Execution
Simply run the Python script from your terminal:
```bash
python qit.py
