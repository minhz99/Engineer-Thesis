import json

with open('/Users/minhz/.gemini/antigravity/brain/4b5fd153-66d8-42b6-be22-9852c44baa6d/.system_generated/logs/transcript.jsonl', 'r') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('type') == 'CODE_ACTION':
                content = data.get('content', '')
                if 'diff_block_start' in content:
                    diffs = content.split('[diff_block_start]')[1:]
                    for diff in diffs:
                        diff = diff.split('[diff_block_end]')[0].strip()
                        if 'fig:process_flow' in diff:
                            with open('clean_3.patch', 'w') as out:
                                out.write("--- a/Chuong/2_Chuong_2.tex\n+++ b/Chuong/2_Chuong_2.tex\n" + diff + "\n")
                        elif 'fig:oil_refining' in diff:
                            with open('clean_4.patch', 'w') as out:
                                out.write("--- a/Chuong/3_Chuong_3.tex\n+++ b/Chuong/3_Chuong_3.tex\n" + diff + "\n")
        except:
            pass
