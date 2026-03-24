from crewai import Agent
from crewai.tools import tool
from crewai import LLM
from mcp_client import call_tool

llm = LLM(
    model="ollama/phi3",
    base_url="http://127.0.0.1:11434",  
    api_key="NA",  # required placeholder
    timeout=300
)

# MCP Tools

@tool("SpeechToText")
def audio_tool(audio_path: str) -> str:
    """Convert audio file to text using MCP server."""
    return call_tool("speech_to_text", {"audio_path": audio_path})



@tool("ImageAnalyzer")
def vision_tool(image_path: str) -> str:
    """Analyze image and extract factual information using MCP."""
    return call_tool("image_analysis", {"image_path": image_path})


@tool("Validator")
def validation_tool(input_data: dict) -> str:
    """Validate consistency between audio and image outputs."""
    return call_tool("validate", input_data)

# Agents
audio_agent = Agent(
    role="Audio Extractor",
    goal="Extract transcript",
    backstory="Expert in speech recognition and audio processing.",
    tools=[audio_tool],
    llm=llm,
    verbose=True
)

vision_agent = Agent(
    role="Vision Extractor",
    goal="Extract visual facts",
    backstory="Expert in analyzing images and extracting factual details.",
    tools=[vision_tool],
    llm=llm,
    verbose=True
)

validation_agent = Agent(
    role="Consistency Checker",
    goal="Detect conflicts",
    backstory="Specialist in validating multimodal data consistency.",
    tools=[validation_tool],
    llm=llm,
    verbose=True
)

reasoning_agent = Agent(
    role="Grounded Reasoner",
    goal="Answer with verified facts only",
    backstory="Careful reasoner that avoids hallucinations.",
    llm=llm,
    verbose=True
)