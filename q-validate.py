# --- Verification is Paramount ---
# Add a Validator agent to our crew to build trust.

def run_classical_approximation(molecule_string: str) -> float:
    """A mock tool for a less-accurate but trusted classical model."""
    print(f"[Classical Approx] Calculating energy for '{molecule_string}'")
    # This model is faster but has a known error margin.
    return -7.86 

validator_agent = Agent(
  role='Results Validation Analyst',
  goal='Verify that the quantum result is plausible by comparing it against established classical approximations.',
  backstory='You are a skeptical AI. You trust classical, well-understood models and flag any quantum result that deviates significantly from them.',
  verbose=True,
  tools=[run_classical_approximation]
)

validation_task = Task(
    description="""Take the JSON output from the Quantum Chemist. 
    Extract the molecule string and the quantum energy. 
    Separately, run a classical approximation for the same molecule. 
    Compare the two results. If they are within a 5% tolerance, approve the result. Otherwise, flag it as a potential anomaly.""",
    expected_output="A final report stating whether the quantum result is 'VALIDATED' or 'ANOMALY FLAGGED'.",
    agent=validator_agent,
    context=[quantum_simulation_task] # Depends on the quantum result
)

# The new crew now includes the vital verification step.
# validated_crew = Crew(
#   agents=[classical_researcher, quantum_chemist, validator_agent],
#   tasks=[research_task, quantum_simulation_task, validation_task],
#   process=Process.sequential
# )
