#include <stdio.h>
#include <time.h>

int main() {
    FILE *f = fopen("system.log", "a");
    if (!f) return 1;

    time_t now = time(NULL);
    fprintf(f, "%s ERROR Connection timeout\n", ctime(&now));
    fclose(f);

    return 0;
}
