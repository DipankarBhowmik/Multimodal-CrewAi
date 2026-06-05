from crewai import Agent, LLM
from crewai.tools import tool
from mcp_client import call_tool

# ── LLM CONFIG ────────────────────────────────────────────────────────────────
# ORIGINAL: model="ollama/phi3"   — text-only 3.8B model
# NOW:      model="ollama/gemma4:e2b" — same vision model used in tools.py
#           One model handles both image understanding AND text reasoning
llm = LLM(
    model="ollama/gemma4:e2b",
    base_url="http://127.0.0.1:11434",
    api_key="NA",
    timeout=300,
)


# ── MCP TOOLS (function names unchanged — mcp_server routes by name) ──────────

@tool("SpeechToText")
def audio_tool(audio_path: str) -> str:
    """Convert audio file to text using Whisper via MCP server."""
    return call_tool("speech_to_text", {"audio_path": audio_path})


@tool("ImageAnalyzer")
def vision_tool(image_path: str) -> str:
    """Analyze image using gemma4:e2b vision encoder via MCP server."""
    return call_tool("image_analysis", {"image_path": image_path})


#@tool("Validator")
#def validation_tool(input_data: dict) -> str:
#    """Validate consistency between audio and image outputs via MCP server."""
#    return call_tool("validate", input_data)

@tool("Validator")
def validation_tool(audio_text: str, image_text: str) -> str:
    """Validate consistency between audio transcript and image description."""
    return call_tool("validate", {
        "audio_text": audio_text,
        "image_text": image_text,
    })


# ── AGENTS (roles, goals, backstories unchanged from original) ─────────────────

audio_agent = Agent(
    role="Audio Extractor",
    goal="Extract transcript",
    backstory="Expert in speech recognition and audio processing.",
    tools=[audio_tool],
    llm=llm,
    verbose=True,
)

vision_agent = Agent(
    role="Vision Extractor",
    goal="Extract visual facts",
    backstory=(
        "Expert in analyzing images using gemma4:e2b's native vision encoder. "
        "Extracts only factual, observable details — no assumptions."
    ),
    tools=[vision_tool],
    llm=llm,
    verbose=True,
)

validation_agent = Agent(
    role="Consistency Checker",
    goal="Detect conflicts",
    backstory="Specialist in validating multimodal data consistency.",
    tools=[validation_tool],
    llm=llm,
    verbose=True,
)

# ORIGINAL: reasoning_agent used phi3 — text-only, never saw the image
# NOW:      reasoning_agent uses gemma4:e2b — the same model that processed
#           the image, so its reasoning is grounded in visual understanding
reasoning_agent = Agent(
    role="Grounded Reasoner",
    goal="Answer with verified facts only",
    backstory=(
        "Careful reasoner powered by gemma4:e2b. "
        "Synthesizes audio, image, and validation outputs into a structured response. "
        "Never introduces information not present in prior task outputs."
    ),
    llm=llm,
    verbose=True,
)
