#main.py
from crewai import Crew
from agents import audio_agent, vision_agent, validation_agent, reasoning_agent, llm
from tasks import create_tasks
from mcp_client import call_tool



# INPUT FILES
image_path = "inputs/earth.jpg"
audio_path = "inputs/moon.wav"

# Create tasks
task1, task2, task3, task4 = create_tasks(image_path, audio_path)

# Assign agents
task1.agent = audio_agent
task2.agent = vision_agent
task3.agent = validation_agent
task4.agent = reasoning_agent

# CRITICAL: pass context between tasks
task4.context = [task1, task2, task3]


# Create crew
crew = Crew(
    agents=[audio_agent, vision_agent, validation_agent, reasoning_agent],
    tasks=[task1, task2, task3, task4],
    verbose=True
)

# Run system
result = crew.kickoff()

print("\n\n===== FINAL OUTPUT =====\n")
print(result)

print("\n\n===== DEBUG OUTPUTS =====\n")
print("Audio Transcript:\n", task1.output)
print("\nImage Description:\n", task2.output)
print("\nValidation Report:\n", task3.output)