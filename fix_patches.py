with open('clean_3.patch', 'r') as f:
    text3 = f.read()

import re
text3 = re.sub(r'\+.*?<truncated 192 bytes>.*?\+.*?inh chế\};',
               r'+\\node[proc=red!15, draw=red!50]             (C) at ( 6.8, 0) {Lò nhiệt phân quay\\\\$350$--$600^{\\circ}$C};\n' + 
               r'+\\node[proc=blue!18]                         (D) at (10.2, 0) {Ngưng tụ\\\\thu hồi dầu};\n' +
               r'+\\node[proc=cyan!20]                         (E) at (13.6, 0) {Chưng cất\\\\+ Tinh chế};', text3, flags=re.DOTALL)
with open('clean_3_fixed.patch', 'w') as f:
    f.write(text3)

with open('clean_4.patch', 'r') as f:
    text4 = f.read()
text4 = re.sub(r'\\node\[proc=orange!25\]  \(raw\)  at \(0, 0\)    \{Dầu thô\\\\.*?hiệt phân\};', r'\\node[proc=orange!25]  (raw)  at (0, 0)    {Dầu thô\\\\nhiệt phân};', text4, flags=re.DOTALL)
text4 = re.sub(r'\\node\[proc=red!10\].*?\\ce\{H2SO4\} đặc\};', r'\\node[proc=red!10]     (acid) at (0,-3.0)  {Tinh chế axit\\\\\\ce{H2SO4} đặc};', text4, flags=re.DOTALL)
text4 = re.sub(r'\\node\[proc=teal!15\].*?\\ce\{NaOH\} 3\\%\};', r'\\node[proc=teal!15]    (base) at (0,-4.5)  {Rửa kiềm\\\\\\ce{NaOH} 3\\%};', text4, flags=re.DOTALL)
text4 = re.sub(r'\\node\[proc=yellow!15\].*?hoạt tính\};', r'\\node[proc=yellow!15]  (clay) at (0,-6.0)  {Hấp phụ đất sét\\\\hoạt tính};', text4, flags=re.DOTALL)
text4 = re.sub(r'\\node\[proc=green!25\].*?hành phẩm\};', r'\\node[proc=green!25]   (out)  at (0,-9.0)  {Dầu diesel\\\\thành phẩm};', text4, flags=re.DOTALL)
with open('clean_4_fixed.patch', 'w') as f:
    f.write(text4)

