import re
import os

for file in os.listdir('.'):
    if file.endswith('.tex'):
        with open(file, 'r') as f:
            content = f.read()
        
        # Replace \resizebox{...}{!}{ with \scalebox{0.9}{
        new_content = re.sub(r'\\resizebox\s*\{[^\}]+\}\s*\{[^\}]+\}\s*\{', r'\\scalebox{0.9}{', content)
        
        if new_content != content:
            with open(file, 'w') as f:
                f.write(new_content)
            print(f"Fixed resizebox in {file}")

