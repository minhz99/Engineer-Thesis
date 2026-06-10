import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace \resizebox{...}{!}{ or \resizebox*{...}{!}{ with \scalebox{0.9}{
    # Be careful with the `%` if it's there
    content = re.sub(r'\\resizebox\{[^\}]+\}\s*\{[^\}]+\}\s*\{', r'\\scalebox{0.9}{', content)
    
    # 2. Add \scalebox{0.9}{ around \begin{tabular} ... \end{tabular} if not preceded by \scalebox
    # We will use a regex to find \begin{tabular}...\end{tabular}
    # and wrap it if we don't see \scalebox{...} right before it (ignoring whitespaces and %)
    # This is slightly tricky, let's just do a simple string replacement for all \begin{tabular}
    # But wait, \begin{tabular} has arguments like \begin{tabular}{|c|c|}.
    # We can split the text by \begin{table} and \end{table} or \begin{figure} and \end{figure}
    
    # Let's iterate through all occurrences of \begin{tabular}
    # A safer way: match \begin{tabular} ... \end{tabular}
    def wrap_tabular(match):
        text = match.group(0)
        # Check if the text before the match ends with \scalebox{0.9}{ (with optional spacing/newlines/%)
        # It's easier to check the whole content, or just wrap it and then clean up double scaleboxes
        return '\\scalebox{0.9}{\n' + text + '%\n}'
        
    def wrap_tikz(match):
        text = match.group(0)
        return '\\scalebox{0.9}{\n' + text + '%\n}'

    # First, let's unwrap any existing \scalebox{0.9}{ around tabulars and tikzpictures so we can re-wrap them uniformly
    # Actually, it's safer to just replace \begin{tabular} with \scalebox{0.9}{\n\begin{tabular} and \end{tabular} with \end{tabular}\n}
    # BUT we need to avoid double wrapping.
    pass

def process_file_v2(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace \resizebox{...}{...}{ with \scalebox{0.9}{
    content = re.sub(r'\\resizebox\{[^\}]+\}\s*\{[^\}]+\}\s*\{', r'\\scalebox{0.9}{', content)

    # Let's find environments
    envs = ['tabular', 'tikzpicture']
    
    for env in envs:
        # regex to find environment block
        # note: tabular might have \begin{tabularx} but we only care about tabular and tikzpicture
        # The user requested scalebox for "những hình/bảng chưa có scalebox".
        
        pattern = r'(\\begin\{' + env + r'\}(?:\[.*?\])?(?:\{.*?\})?.*?\\end\{' + env + r'\})'
        
        def replacer(match):
            block = match.group(1)
            return '\\scalebox{0.9}{\n' + block + '%\n}'
            
        # We temporarily replace all environments
        # But wait, python's re module doesn't support overlapping or variable length lookbehind.
        # So we just do a findall and manual replace.
        
        matches = list(re.finditer(pattern, content, flags=re.DOTALL))
        # reverse iterate to not mess up indices
        for m in reversed(matches):
            start, end = m.span()
            block = content[start:end]
            
            # Check if there is \scalebox{...}{ before it
            # Let's look at the text before `start`
            prefix = content[:start]
            
            # If the prefix ends with \scalebox{...}{ (ignoring whitespaces and %)
            if re.search(r'\\scalebox\{[^\}]+\}\s*\{[\s\%]*$', prefix):
                # already wrapped!
                continue
                
            # If there's \resizebox... we already replaced it with \scalebox
            
            new_block = '\\scalebox{0.9}{\n' + block + '%\n}'
            content = content[:start] + new_block + content[end:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


for file in os.listdir('.'):
    if file.endswith('.tex'):
        process_file_v2(file)
        print(f"Processed {file}")

