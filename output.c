#include <stdio.h>
int stack[1024];
int sp = -1;
void push(int value) { stack[++sp] = value; }
int pop() { return stack[sp--]; }
int top() { return stack[sp]; }
int main() {
    push(3);
    push(4);
    push(pop() + pop());
    printf("%d\n", pop());
    push(5);
    push(pop() * pop());
    printf("%d\n", pop());
    push(10);
    push(5);
    push(1);
    printf("%d\n", pop());
    push(0);
    printf("%d\n", pop());
    printf("Top of stack: %d\n", top());
    return 0;
}