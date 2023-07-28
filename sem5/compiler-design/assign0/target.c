#include <stdio.h>

void add(int a, int b) { printf("Sum: %d\n", a + b); }

int main()
{
  int x = 2;
  int y = 3;

  add(x, y);
  return 0;
}
