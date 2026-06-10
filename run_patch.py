import re
import os

for i, fname in enumerate(["diff_action_3.diff", "diff_action_4.diff"]):
    with open(fname, 'r') as f:
        content = f.read()
    
    # Remove the markers and unescape newlines
    content = content.replace('[diff_block_start]\\n', '').replace('\\n[diff_block_end]', '').replace('\\n', '\n')
    
    # Add the file header for patch
    if i == 0:
        patch_text = "--- a/Chuong/2_Chuong_2.tex\n+++ b/Chuong/2_Chuong_2.tex\n" + content
    else:
        patch_text = "--- a/Chuong/3_Chuong_3.tex\n+++ b/Chuong/3_Chuong_3.tex\n" + content
        
    with open(f"clean_{i}.patch", "w") as f:
        f.write(patch_text)
    
    os.system(f"patch -p1 < clean_{i}.patch")
