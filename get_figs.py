with open('/Users/minhz/.gemini/antigravity/brain/4b5fd153-66d8-42b6-be22-9852c44baa6d/.system_generated/logs/transcript.jsonl', 'r') as f:
    text = f.read()

import re
matches = re.findall(r'\\begin\{figure\}.*?\\end\{figure\}', text, re.DOTALL)
count = 0
for m in set(matches):
    m_clean = m.replace('\\n', '\n').replace('\\\\', '\\').replace('\\"', '"').replace('\\t', '\t')
    if "tikzpicture" in m_clean:
        with open(f"recovered_fig_{count}.tex", "w") as out:
            out.write(m_clean)
        print(f"Saved recovered_fig_{count}.tex")
        count += 1
