import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace \resizebox{...}{!}{ with \scalebox{0.9}{
    content = re.sub(r'\\resizebox\s*\{[^\}]+\}\s*\{[^\}]+\}\s*\{', r'\\scalebox{0.9}{', content)
    
    # We want to wrap \begin{tabular} and \begin{tikzpicture} with \scalebox{0.9}{ ... }
    # if they are not already preceded by \scalebox
    
    # Let's split the text using \begin{tabular} and \begin{tikzpicture}
    envs = ['tabular', 'tikzpicture']
    for env in envs:
        pattern = r'(\\begin\{' + env + r'\}.*?\\end\{' + env + r'\})'
        parts = re.split(pattern, content, flags=re.DOTALL)
        
        # parts will be [text_before, match1, env1, text_between, match2, env2, ...]
        new_content = ""
        for i in range(0, len(parts)):
            if i % 3 == 0:
                new_content += parts[i]
            elif i % 3 == 1:
                match = parts[i]
                text_before = parts[i-1]
                # Check if text_before ends with \scalebox{...}{
                # We can strip trailing whitespace and % and see if it ends with {
                # Then check if there's \scalebox
                cleaned = re.sub(r'[\s\%]*$', '', text_before)
                if re.search(r'\\scalebox\s*\{[^\}]+\}\s*\{$', cleaned):
                    # already wrapped
                    new_content += match
                else:
                    new_content += '\\scalebox{0.9}{\n' + match + '%\n}'
            else:
                # the captured env name, ignore
                pass
        content = new_content

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for file in os.listdir('.'):
    if file.endswith('.tex'):
        process_file(file)
