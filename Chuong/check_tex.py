import os
import re

for file in os.listdir('.'):
    if file.endswith('.tex'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check braces
        open_b = content.count('{')
        close_b = content.count('}')
        if open_b != close_b:
            print(f"{file} has mismatched braces: {open_b} vs {close_b}")
            
        # Check environments
        begins = re.findall(r'\\begin\{([^\}]+)\}', content)
        ends = re.findall(r'\\end\{([^\}]+)\}', content)
        
        counts = {}
        for b in begins:
            counts[b] = counts.get(b, 0) + 1
        for e in ends:
            counts[e] = counts.get(e, 0) - 1
            
        for env, diff in counts.items():
            if diff != 0:
                print(f"{file} has mismatched env '{env}': {diff}")

