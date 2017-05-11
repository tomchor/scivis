reset
set terminal epslatex standalone monochrome font "cmr" 10 size 6,4
set encoding iso_8859_1
set output "v2_phi_std_stable.tex"
set datafile separator ","
set grid
set format y "$10^{%+T}$"
set format x "$10^{%+T}$"
set xlabel "$\\zeta$"
set log xy
set multiplot
set size .5, .5
c="../../data/phi_c.csv"
theta="../../data/phi_theta.csv"
q="../../data/phi_q.csv"
w="../../data/phi_w.csv"
set key samplen 2

phi_s(x) = 2
phi_w(x) = 1.25

set label "a)" at screen 0.12, 0.915
set label "b)" at screen 0.62, 0.915
set label "c)" at screen 0.12, 0.415
set label "d)" at screen 0.62, 0.415

set xrange [0.01:10]
set yrange [0.5:1000]
#set xtics 100

set origin 0.0, 0.5
plot phi_s(x) with lines lw 4 lc rgb "red" t "$\\phi_c$",\
c u ($2):3 with points pt 6 ps .7 lw 3 lc rgb "blue" t "$\\phi_c^*$"

set origin 0.5, 0.5
plot phi_s(x) with lines lw 4 lc rgb "red" t "$\\phi_\\theta$",\
theta u ($2):3 with points pt 6 ps .7 lw 3 lc rgb "blue" t "$\\phi_\\theta^*$"

set origin 0.0, 0.0
plot phi_s(x) with lines lw 4 lc rgb "red" t "$\\phi_q$",\
q u ($2):3 with points pt 6 ps .7 lw 3 lc rgb "blue" t "$\\phi_q^*$"

set origin 0.5, 0.0
plot phi_w(x) with lines lw 4 lc rgb "red" t "$\\phi_w$",\
w u ($2):3 with points pt 6 ps .7 lw 3 lc rgb "blue" t "$\\phi_w^*$"

