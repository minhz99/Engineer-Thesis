import json

with open('/Users/minhz/.gemini/antigravity/brain/4b5fd153-66d8-42b6-be22-9852c44baa6d/.system_generated/logs/transcript.jsonl', 'r') as f:
    lines = f.readlines()

for line in lines:
    try:
        data = json.loads(line, strict=False)
        if 'tool_calls' in data:
            for tc in data['tool_calls']:
                if tc['name'] == 'multi_replace_file_content':
                    file_path = tc['args']['TargetFile'].strip('"')
                    chunks = tc['args']['ReplacementChunks']
                    if isinstance(chunks, str):
                        try:
                            chunks = json.loads(chunks, strict=False)
                        except:
                            try:
                                import ast
                                chunks = ast.literal_eval(chunks)
                            except:
                                print("Failed to parse chunks")
                                continue
                    
                    if '1_Chuong_1.tex' in file_path or '2_Chuong_2.tex' in file_path or '3_Chuong_3.tex' in file_path:
                        with open(file_path, 'r', encoding='utf-8') as tf:
                            tlines = tf.readlines()
                        
                        try:
                            for chunk in sorted(chunks, key=lambda x: x['StartLine'], reverse=True):
                                sl = chunk['StartLine'] - 1
                                el = chunk['EndLine']
                                rc = chunk['ReplacementContent']
                                if not rc.endswith('\n'):
                                    rc += '\n'
                                tlines[sl:el] = [rc]
                            
                            with open(file_path, 'w', encoding='utf-8') as tf:
                                tf.writelines(tlines)
                            print(f"Applied chunk to {file_path}")
                        except Exception as inner_e:
                            print(f"Failed to apply to {file_path}: {inner_e}")
    except Exception as e:
        pass
