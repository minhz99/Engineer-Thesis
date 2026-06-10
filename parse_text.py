import re
with open('extracted_edits.txt', 'r') as f:
    text = f.read()

# Replace encoded newlines and quotes to make it easier to search
text = text.replace('\\n', '\n').replace('\\"', '"').replace('\\\\', '\\')

m = re.findall(r'\\begin\{figure\}.*?\\end\{figure\}', text, re.DOTALL)
for i, fig in enumerate(m):
    with open(f'figure_{i}.tex', 'w') as f:
        f.write(fig)
        print(f"Saved figure_{i}.tex")
