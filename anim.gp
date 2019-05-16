reset
set key off

p [0:49][0:49]'sand_piles.dat' matrix w image

while(1){
  replot
  pause 0.3
}
