# measure_digital_market_state.py

import qiskit
from qiskit_aer import AerSimulator

def create_market_snapshot_circuit():
    """
    Creates a conceptual quantum circuit representing a digital market.

    - Superposition: Represents the infinite possibilities of the market before analysis.
    - Entanglement: Represents the interconnectedness of competitors.
    - Measurement: Represents our app taking a snapshot, collapsing possibilities into one reality.
    """
    
    # 1. THE SYSTEM: Define a quantum circuit with 3 qubits.
    #    Each qubit represents a major competitor's potential ranking (e.g., High=1, Low=0).
    #    With 3 qubits, we have 2^3 = 8 possible market states (from 000 to 111).
    circuit = qiskit.QuantumCircuit(3, 3) # 3 quantum bits, 3 classical bits for measurement

    # 2. SUPERPOSITION: Apply the Hadamard (H) gate to each qubit.
    #    This is the core of the quantum analogy. Before measurement, the market exists
    #    in a superposition of ALL 8 possible states at the same time. It has no
    #    definite state, only a cloud of probabilities.
    print(" -> Placing market into a superposition of all possible states...")
    for qubit in range(3):
        circuit.h(qubit)

    # 3. ENTANGLEMENT: Apply Controlled-NOT (CNOT) gates.
    #    This represents the fact that competitors are not independent. The strategy of
    #    Competitor 0 can influence the outcome of Competitor 1, and so on. This
    #    entanglement shifts the probabilities, making some market outcomes more likely.
    print(" -> Entangling competitors to simulate market influences...")
    circuit.cx(0, 1)  # Competitor 0's state now influences Competitor 1
    circuit.cx(1, 2)  # Competitor 1's state now influences Competitor 2
    
    # Add a barrier for visualization purposes, separating setup from measurement
    circuit.barrier()

    # 4. MEASUREMENT: The act of running our application.
    #    This collapses the superposition of all 8 possibilities into a single,
    #    definite, classical outcome. We observe the system, and it is forced
    #    to "choose" one state.
    print(" -> Measuring the market state (Running our app's analysis)...")
    circuit.measure([0, 1, 2], [0, 1, 2]) # Measure each qubit into its classical bit

    return circuit

def run_simulation(circuit, shots=1024):
    """
    Executes the quantum circuit on a simulator.
    'shots' represents running our analysis multiple times to see the probability distribution.
    """
    simulator = AerSimulator()
    compiled_circuit = qiskit.transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=shots)
    result = job.result()
    counts = result.get_counts(compiled_circuit)
    return counts

def interpret_results(counts):
    """
    Translates the quantum results (binary strings) into a human-readable format.
    """
    # Let's define what each of our 8 possible states represents.
    competitor_rankings = {
        '000': "Dominance by Competitor A, B, and C are weak.",
        '001': "Surge by Competitor C, A and B are stable.",
        '010': "Aggressive ad spend from Competitor B.",
        '011': "Competitors B and C form a market alliance.",
        '100': "Competitor A launches a disruptive new product.",
        '101': "Competitors A and C engage in a price war.",
        '110': "Market consolidation between A and B.",
        '111': "High market volatility, all competitors are strong.",
    }

    print("\n--- Market Analysis Snapshot ---")
    print(f"Out of 1024 simulations, the following market states were observed:")
    
    # Sort the results by the number of times each state was observed
    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

    for state, count in sorted_counts:
        # The quantum state is read from right to left (q2, q1, q0)
        # So we reverse the string to match our circuit layout (q0, q1, q2)
        readable_state = state[::-1] 
        description = competitor_rankings.get(readable_state, "An unknown market event.")
        percentage = (count / 1024) * 100
        print(f"- State '{readable_state}': Observed {count} times ({percentage:.2f}%)")
        print(f"  Interpretation: {description}")

    # Explain the state shift
    most_likely_state = sorted_counts[0][0][::-1]
    print("\n--- The State Shift Explained ---")
    print(f"The most probable outcome in this measurement was '{most_likely_state}'.")
    print("If we were to run this analysis again (another 'measurement'), we might get a different outcome.")
    print("This is the 'state shift'. Our app's job is to take these classical snapshots over time to understand the deep, underlying dynamics of the market's quantum-like state.")


if __name__ == '__main__':
    # Build the circuit representing the market
    market_circuit = create_market_snapshot_circuit()
    
    # Optional: Print the circuit diagram to see what it looks like
    print("\nQuantum Circuit Diagram:")
    print(market_circuit)

    # Run the simulation
    results = run_simulation(market_circuit)
    
    # Interpret and display the results
    interpret_results(results)
