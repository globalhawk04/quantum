# --- The AI Orchestrator is the Essential Role ---
# This code shows how a classical crew orchestrates a quantum agent.

from crewai import Agent, Task, Crew, Process
# We'll use the QuantumCoprocessor from the previous example as a "tool"
# from hybrid_api import QuantumCoprocessor 

# --- Agentic Specialization is Key ---
# 1. Define the agents with their specialized roles.

# Instantiate the "tool" for our quantum agent
quantum_tool = QuantumCoprocessor(api_key="YOUR_QPU_API_KEY")

classical_researcher = Agent(
  role='Senior Computational Chemist',
  goal='Identify promising candidate molecules for a specific problem based on existing literature.',
  backstory='You are an expert in classical chemistry simulations and literature review.',
  verbose=True,
  allow_delegation=False
)

quantum_chemist = Agent(
  role='Quantum Simulation Specialist',
  goal='Calculate the precise ground state energy of candidate molecules using quantum hardware.',
  backstory='You are an AI agent that interfaces with the quantum co-processor.',
  verbose=True,
  allow_delegation=False,
  # This agent has the specialized quantum tool
  tools=[quantum_tool.calculate_ground_state_energy] 
)

# 2. Define the tasks for the crew
research_task = Task(
  description='Find the most promising molecule to act as a catalyst for nitrogen fixation, based on classical models. For this example, assume the answer is Lithium Hydride.',
  expected_output='A string representing the molecule, e.g., "Li .0 .0 .0; H .0 .0 1.5474".',
  agent=classical_researcher
)

quantum_simulation_task = Task(
  description='Take the candidate molecule from the classical researcher and calculate its quantum-accurate ground state energy.',
  expected_output='A JSON object containing the final, precise energy calculation from the QPU.',
  agent=quantum_chemist,
  # This task depends on the output of the first task
  context=[research_task] 
)

# 3. The Orchestrator assembles and kicks off the crew.
crew = Crew(
  agents=[classical_researcher, quantum_chemist],
  tasks=[research_task, quantum_simulation_task],
  process=Process.sequential
)

# --- Kick off the orchestrated workflow ---
# result = crew.kickoff() 
# print(result)
