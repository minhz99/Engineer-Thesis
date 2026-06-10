import re
import os
import subprocess

def get_recent_commits():
    pass

# We don't have git. Let's just find \scalebox{0.9}{ in all files and see what surrounds it.
for file in os.listdir('.'):
    if file.endswith('.tex'):
        with open(file, 'r') as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if '\\scalebox{0.9}{' in line:
                print(f"--- {file}:{i+1} ---")
                start = max(0, i-2)
                end = min(len(lines), i+3)
                for j in range(start, end):
                    print(lines[j].rstrip())
