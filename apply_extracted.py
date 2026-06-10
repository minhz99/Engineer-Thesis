import json

with open('extracted_edits.txt', 'r') as f:
    lines = f.readlines()

current_file = None
current_json = ""
for line in lines:
    if line.startswith('--- EDIT IN'):
        if current_file and current_json:
            try:
                chunks = json.loads(current_json)
                with open(current_file, 'r', encoding='utf-8') as tf:
                    tlines = tf.readlines()
                
                # Apply chunks in reverse order
                for chunk in sorted(chunks, key=lambda x: x['StartLine'], reverse=True):
                    sl = chunk['StartLine'] - 1
                    el = chunk['EndLine']
                    rc = chunk['ReplacementContent']
                    if not rc.endswith('\n'):
                        rc += '\n'
                    tlines[sl:el] = [rc]
                
                with open(current_file, 'w', encoding='utf-8') as tf:
                    tf.writelines(tlines)
                print(f"Applied to {current_file}")
            except Exception as e:
                print(f"Error applying to {current_file}: {e}")
                
        current_file = line.split('"')[1]
        current_json = ""
    else:
        current_json += line

if current_file and current_json:
    try:
        chunks = json.loads(current_json)
        with open(current_file, 'r', encoding='utf-8') as tf:
            tlines = tf.readlines()
        for chunk in sorted(chunks, key=lambda x: x['StartLine'], reverse=True):
            sl = chunk['StartLine'] - 1
            el = chunk['EndLine']
            rc = chunk['ReplacementContent']
            if not rc.endswith('\n'):
                rc += '\n'
            tlines[sl:el] = [rc]
        with open(current_file, 'w', encoding='utf-8') as tf:
            tf.writelines(tlines)
        print(f"Applied to {current_file}")
    except Exception as e:
        print(f"Error applying to {current_file}: {e}")

