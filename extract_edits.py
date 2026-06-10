import json

with open('/Users/minhz/.gemini/antigravity/brain/4b5fd153-66d8-42b6-be22-9852c44baa6d/.system_generated/logs/transcript.jsonl', 'r') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('type') == 'PLANNER_RESPONSE' or data.get('type') == 'TOOL_CALL':
                if 'tool_calls' in data:
                    for tc in data['tool_calls']:
                        if tc['name'] == 'multi_replace_file_content':
                            print(f"--- EDIT IN {tc['args']['TargetFile']} ---")
                            print(tc['args']['ReplacementChunks'])
        except Exception as e:
            pass
