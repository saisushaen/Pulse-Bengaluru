import json
from flask import Request
from pulse_bengaluru_agent.agent import root_agent
from vertexai.preview import reasoning_engines

def pulse_entry(request: Request):
    try:
        request_json = request.get_json(force=True)
    except Exception as e:
        return {"error": "Invalid JSON payload", "details": str(e)}, 400

    response = reasoning_engines.run(root_agent, request=request_json)
    return json.dumps(response), 200, {'Content-Type': 'application/json'}
