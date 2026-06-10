import re

# --- Figure for Chuong 3 ---
fig_3 = r"""
\begin{figure}[htbp]
\centering
\scalebox{0.9}{%
\begin{tikzpicture}[
    proc/.style={
        draw=gray!70, thick, rounded corners=3pt,
        fill=#1, minimum width=2.4cm, minimum height=0.85cm,
        font=\footnotesize, align=center,
    },
    proc/.default={white},
    side/.style={
        draw=gray!50, rounded corners=3pt,
        fill=gray!10, minimum width=2.0cm, minimum height=0.75cm,
        font=\scriptsize, align=center,
    },
    arr/.style={-{Stealth[length=5pt,width=3.5pt]}, thick, #1},
    arr/.default={gray!65},
    lbl/.style={font=\scriptsize, black!60},
]
\node[proc=orange!25]  (raw)  at (0, 0)    {Dầu thô\\nhiệt phân};
\node[proc=blue!15]    (dist) at (0,-1.5)  {Chưng cất\\phân đoạn};
\node[proc=red!10]     (acid) at (0,-3.0)  {Tinh chế axit\\\ce{H2SO4} đặc};
\node[proc=teal!15]    (base) at (0,-4.5)  {Rửa kiềm\\\ce{NaOH} 3\%};
\node[proc=yellow!15]  (clay) at (0,-6.0)  {Hấp phụ đất sét\\hoạt tính};
\node[proc=gray!20]    (filt) at (0,-7.5)  {Lọc ép tinh};
\node[proc=green!25]   (out)  at (0,-9.0)  {Dầu diesel\\thành phẩm};

\draw[arr] (raw)  -- (dist);
\draw[arr] (dist) -- (acid) node[lbl, midway, right=2pt] {Dầu nhẹ (80\%)};
\draw[arr] (acid) -- (base);
\draw[arr] (base) -- (clay);
\draw[arr] (clay) -- (filt);
\draw[arr] (filt) -- (out);

\node[side] (heavy) at (-3.2,-1.5) {Dầu nặng 15\%\\$\rightarrow$ hồi lưu lò};
\node[side] (gasr)  at ( 3.2,-1.5) {Khí 5\%\\$\rightarrow$ hồi lưu đốt};
\draw[arr=orange!60] (dist.west) -- (heavy.east);
\draw[arr=blue!50]   (dist.east) -- (gasr.west);

\node[side] (acid_w) at (3.2,-3.0) {Cặn axit\\(trung hòa)};
\node[side] (base_w) at (3.2,-4.5) {Nước thải kiềm\\(xử lý)};
\node[side] (clay_w) at (3.2,-6.0) {Đất sét thải\\(xử lý)};
\draw[arr=gray!45] (acid.east) -- (acid_w.west);
\draw[arr=gray!45] (base.east) -- (base_w.west);
\draw[arr=gray!45] (clay.east) -- (clay_w.west);

\end{tikzpicture}%
}
\caption{Quy trình chưng cất và tinh chế hóa học nâng cấp chất lượng dầu}
\label{fig:oil_refining}
\end{figure}
"""

with open('Chuong/3_Chuong_3.tex', 'r', encoding='utf-8') as f:
    text3 = f.read()

target3 = r"Quá trình này giúp loại bỏ hợp chất chứa lưu huỳnh, nhựa không bão hòa và cải thiện độ màu."
text3 = text3.replace(target3, target3 + "\n" + fig_3)

with open('Chuong/3_Chuong_3.tex', 'w', encoding='utf-8') as f:
    f.write(text3)


# --- Figure for Chuong 2 ---
fig_2 = r"""
\begin{figure}[htbp]
\centering
\scalebox{0.9}{%
\begin{tikzpicture}[
    proc/.style={
        draw=gray!65, thick, rounded corners=4pt,
        fill=#1, minimum width=2.8cm, minimum height=1.05cm,
        font=\footnotesize, align=center,
    },
    proc/.default={white},
    side/.style={
        draw=gray!55, rounded corners=3pt,
        fill=#1, minimum width=2.3cm, minimum height=0.8cm,
        font=\scriptsize, align=center,
    },
    side/.default={gray!15},
    arr/.style={-{Stealth[length=6pt,width=4pt]}, thick, #1},
    arr/.default={gray!70},
    lbl/.style={font=\scriptsize, fill=white, draw=none, inner sep=1.5pt},
]
\node[proc=green!25]                        (A) at ( 0.0, 0) {CTRSH tươi\\120\,t/ngày};
\node[proc=orange!20]                       (B) at ( 3.4, 0) {Phân loại\\sơ bộ};
\node[proc=red!15, draw=red!50]             (C) at ( 6.8, 0) {Lò nhiệt phân quay\\$350$--$600^{\circ}$C};
\node[proc=blue!18]                         (D) at (10.2, 0) {Ngưng tụ\\thu hồi dầu};
\node[proc=cyan!20]                         (E) at (13.6, 0) {Chưng cất\\+ Tinh chế};
\node[proc=teal!22]                         (F) at (17.0, 0) {Động cơ diesel};
\node[proc=yellow!30, draw=yellow!65!black] (G) at (20.4, 0) {Điện};

\draw[arr] (A) -- (B);
\draw[arr] (B) -- (C)
    node[lbl, midway, above=20pt] {Cháy được (RDF)};
\draw[arr] (C) -- (D)
    node[lbl, midway, above=20pt] {Dầu + hơi};
\draw[arr] (D) -- (E)
    node[lbl, midway, above=20pt] {Dầu thô};
\draw[arr] (E) -- (F)
    node[lbl, midway, above=20pt] {Dầu diesel};
\draw[arr] (F) -- (G);

\node[side=gray!20] (Bw) at (3.4, -2.0) {Lò cacbon hóa\\(hữu cơ 62,56\%)};
\node[side=gray!30] (Cc) at (6.8, -2.0) {Than carbon\\(25\%)};

\draw[arr=gray!60] (B.south) -- (Bw.north);
\draw[arr=gray!60] (C.south) -- (Cc.north);

\node[side=blue!10, draw=blue!45] (Gr) at (8.5, 2.0) {Khí hồi lưu (30\%)};
\draw[arr=blue!55] (D.north) |- (Gr.east);
\draw[arr=blue!50, dashed] (Gr.west) -| (C.north);

\node[side=orange!20, draw=orange!55] (Hr) at (11.9, -2.0) {Dầu nặng hồi lưu};
\draw[arr=orange!60] (E.south) |- (Hr.east);
\draw[arr=orange!50, dashed] (Hr.south) -- ++(0,-0.3) -| (C.south west);

\end{tikzpicture}%
}
\caption{Sơ đồ công nghệ tổng thể: tiền xử lý -- nhiệt phân -- tinh chế -- phát điện}
\label{fig:process_flow}
\end{figure}
"""

with open('Chuong/2_Chuong_2.tex', 'r', encoding='utf-8') as f:
    text2 = f.read()

target2 = r"Cấu hình này phù hợp với mục tiêu ưu tiên thu dầu nhiệt phân và kiểm soát ổn định quá trình trong điều kiện rác đầu vào biến động."
text2 = text2.replace(target2, target2 + "\n" + fig_2)

with open('Chuong/2_Chuong_2.tex', 'w', encoding='utf-8') as f:
    f.write(text2)

print("Figures inserted successfully.")
