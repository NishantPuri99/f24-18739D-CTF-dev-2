#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//referred from https://play.picoctf.org/practice/challenge/258 (accessed November 28,2024)
void win() {
    printf("Congratulations! You have called the win() function.\n");
    char buf[64];
    FILE *f = fopen("./flag.txt","r");
    if (f == NULL) {
        printf("%s %s", "Please create 'flag.txt' in this directory with your",
                        "own debugging flag.\n");
        exit(0);
    }
    fgets(buf,64,f);
    printf(buf);
    fflush(stdout);
    fclose(f);
}

void vuln() {
    char buffer[32];
    printf("Enter some input: ");
    gets(buffer);
    printf("You entered: %s\n", buffer);
    fflush(stdout);
}
int main() {
    // setvbuf(stdout, NULL, _IONBF, 0); 
    printf("Welcome to this simple ret2win challenge!\n");
    fflush(stdout);
    vuln();
    return 0;
}
