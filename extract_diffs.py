import re
with open('/Users/minhz/.gemini/antigravity/brain/4b5fd153-66d8-42b6-be22-9852c44baa6d/.system_generated/logs/transcript.jsonl', 'r') as f:
    text = f.read()

diff_blocks = re.findall(r'\[diff_block_start\].*?\[diff_block_end\]', text, re.DOTALL)
for i, b in enumerate(diff_blocks):
    with open(f"diff_action_{i}.diff", "w") as out:
        out.write(b)
        print(f"Saved diff_action_{i}.diff")
