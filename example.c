#include <stdio.h>

int main() {
    int x = 0;
    if(x = 5){ // Assignment instead of comparison (Cppcheck should warn)
    printf("X is five\n");
    }
return 0;
}
