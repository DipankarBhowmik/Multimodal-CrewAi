#tasks.py
from crewai import Task

def create_tasks(image_path, audio_path):

    task1 = Task(
        description=f"Transcribe audio file: {audio_path}",
        expected_output="Clean transcript text",
        agent=None  # assigned later
    )

    task2 = Task(
        description=f"Analyze image: {image_path}",
        expected_output="List of visible facts",
        agent=None
    )

    task3 = Task(
        description="""
        Compare audio transcript and image description.
        Identify:
        - contradictions
        - missing information
        - uncertainty
        """,
        expected_output="Validation report",
        agent=None
    )

    task4 = Task(
        description="""
        Use outputs from previous tasks:

        - Audio transcript (Task 1)
        - Image description (Task 2)
        - Validation report (Task 3)

        Generate final structured output.

        IMPORTANT:
        - Include FULL audio transcript
        - Include image description

        Output format:
        {
            "answer": "...",
            "audio_transcript": "...",
            "image_description": "...",
            "confidence": 0-1,
            "evidence": [...],
            "uncertainty": "..."
        }
        """,
        context=[],  # set in main.py
        expected_output="Structured JSON output",
        agent=None
)

    return task1, task2, task3, task4