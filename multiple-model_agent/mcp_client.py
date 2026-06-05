import requests

MCP_URL = "http://localhost:9000/execute"

def call_tool(tool_name, payload):
    response = requests.post(
        MCP_URL,
        json={
            "tool_name": tool_name,
            "input": payload
        }
    )
    return response.json()["result"]