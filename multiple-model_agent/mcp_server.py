from fastapi import FastAPI
from pydantic import BaseModel
from tools import speech_to_text, moondream_vision, validate_modalities

app = FastAPI()

class MCPRequest(BaseModel):
    tool_name: str
    input: dict


@app.post("/execute")
def execute_tool(req: MCPRequest):

    if req.tool_name == "speech_to_text":
        return {"result": speech_to_text(req.input["audio_path"])}

    elif req.tool_name == "image_analysis":
        return {"result": moondream_vision(req.input["image_path"])}

    elif req.tool_name == "validate":
        return {
            "result": validate_modalities(
                req.input["audio_text"],
                req.input["image_text"]
            )
        }

    return {"error": "Unknown tool"}