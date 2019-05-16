#include<stdio.h>
#include<stdlib.h>
#include<assert.h>

#define N 50
#define MPH 4

int grid[50][50] = {0};
FILE *outfile;

void add_sand(int x, int y);
void topple_sand(void);
void wrt_to_file(void);
void update(int sweeps);

int main(void){
  while(1){
    update(1);
  }
  return 0;
}

void update(int sweeps){
  int k;
  for(k=0;k<sweeps;k++){
    add_sand((int)(N/2.), (int)(N/2.));
    topple_sand();
  }
  wrt_to_file();
}

void add_sand(int x, int y){
  grid[x][y] += 1;
}

void topple_sand(void){
  int i ,j, cnt=0;
  int all_toppled = 0;
  while(all_toppled == 0){
    for(i=0;i<N;i++){
      for(j=0;j<N;j++){
        if (grid[i][j] >= MPH){
          cnt += 1;
          grid[i][j] -= MPH;
          grid[(i+1+N)%N][j] += 1;
          grid[(i-1+N)%N][j] += 1;
          grid[i][(j+1+N)%N] += 1;
          grid[i][(j+1+N)%N] += 1;
        }
      }
    }
    if(cnt == 0){
      all_toppled = 1;
    }
  }
}

void wrt_to_file(void){
  int i, j;
  outfile = fopen("sand_piles.dat", "w");
  for(i=0;i<N;i++){
    for(j=0;j<N;j++){
      fprintf(outfile, "%d%s", grid[i][j], (j == N-1) ? "\n":" ");
      }
    }
  fclose(outfile);
}
