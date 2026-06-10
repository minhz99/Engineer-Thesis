with open('diff_since_last_commit.diff', 'r') as f:
    lines = f.readlines()

in_chunk = False
extracted = ""
for line in lines:
    if "fig:process_flow" in line:
        pass
    if line.startswith("+++"):
        continue
    if "fig:oil_refining" in line or "fig:process_flow" in line:
        pass # just to check where it is

with open('diff_since_last_commit.diff', 'r') as f:
    content = f.read()

import re
# Find fig:process_flow block
m1 = re.search(r'(\+.*?\\begin\{tikzpicture\}.*?\\label\{fig:process_flow\})', content, re.DOTALL)
if m1:
    print("Found process_flow!")
    # clean the pluses
    clean_text = "\n".join([line[1:] if line.startswith('+') else line for line in m1.group(1).split('\n')])
    with open('process_flow_extracted.tex', 'w') as f:
        f.write(clean_text)

m2 = re.search(r'(\+.*?\\begin\{tikzpicture\}.*?\\label\{fig:oil_refining\})', content, re.DOTALL)
if m2:
    print("Found oil_refining!")
    clean_text = "\n".join([line[1:] if line.startswith('+') else line for line in m2.group(1).split('\n')])
    with open('oil_refining_extracted.tex', 'w') as f:
        f.write(clean_text)

