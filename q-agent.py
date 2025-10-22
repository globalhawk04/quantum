### Code Block 2: The Multi-Agent Method for Validation
# This code shows how agents could collaborate to make and validate a prediction.
# Prerequisites: pip install crewai

from crewai import Agent, Task, Crew

# --- Mock Tools ---
# In a real scenario, these would be complex tools accessing APIs and databases.
def mock_llm_prediction(perturbation: str) -> str:
    print(f"\n[Predictor] Running prediction for: {perturbation}")
    if "caffeine on liver cell" in perturbation:
        return "Prediction: Cell will differentiate into a neuronal-like phenotype."
    return "Prediction: No significant change."

def mock_knowledge_base_check(prediction: str) -> bool:
    print(f"[Validator] Checking prediction: '{prediction}'")
    # Rule: A liver cell (hepatocyte) cannot transdifferentiate into a neuron.
    if "liver" in "liver cell" and "neuronal" in prediction:
        print("[Validator] RESULT: Fails biological plausibility check!")
        return False
    print("[Validator] RESULT: Plausible.")
    return True

# --- Agent Definitions ---
predictor_agent = Agent(
  role='Predictive Biologist',
  goal='Use the Cell2Sentence model to predict cellular responses to stimuli.',
  backstory='An AI agent that interfaces directly with the foundational model to generate raw hypotheses.',
  verbose=True,
  allow_delegation=False
)

validator_agent = Agent(
  role='Computational Biologist',
  goal='Validate AI-generated hypotheses against known biological principles.',
  backstory='An AI agent with access to vast biological databases and textbooks, tasked with ensuring predictions are not nonsensical.',
  verbose=True,
  allow_delegation=False
)

# --- Task Definitions ---
# The task for the predictor is simply to run the model
prediction_task = Task(
  description="Predict the effect of applying caffeine on a liver cell.",
  expected_output="A string describing the predicted cellular state.",
  agent=predictor_agent,
  # This is a conceptual way to link the agent to its tool
  tool_function=lambda: mock_llm_prediction("caffeine on liver cell")
)

# The task for the validator takes the output of the first task as context
validation_task = Task(
  description="Validate the biological plausibility of the prediction from the Predictive Biologist.",
  expected_output="A boolean flag (True for plausible, False for non-sensical).",
  agent=validator_agent,
  context=[prediction_task], # Use the result of the previous task
  tool_function=lambda: mock_knowledge_base_check(prediction_task.output.raw)
)


# --- Create and run the Crew ---
biology_crew = Crew(
  agents=[predictor_agent, validator_agent],
  tasks=[prediction_task, validation_task],
  verbose=2
)

# result = biology_crew.kickoff()
# print("\n--- FINAL RESULT ---")
# print(result)
