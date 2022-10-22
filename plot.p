set terminal png size 600
set output "reporte.png"
set title "Grupo 25"
set size ratio 0.6
set grid y
set xlabel "Nro Peticiones"
set ylabel "Tiempo de respuesta (ms)"
plot "output.csv" using 9 smooth sbezier with lines title "Peticiones"
