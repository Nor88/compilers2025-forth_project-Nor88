import sys

# Ensure that the script gets the input filename as an argument
if len(sys.argv) < 2:
    print("Usage: python3 compiler_to_c.py <input.forth>")
    sys.exit(1)

input_file = sys.argv[1]

# Read the Forth-like input file
with open(input_file, "r") as f:
    tokens = f.read().split()

# Begin C output
c_code = []
c_code.append("#include <stdio.h>")
c_code.append("int stack[1024];")
c_code.append("int sp = -1;")
c_code.append("void push(int value) { stack[++sp] = value; }")
c_code.append("int pop() { return stack[sp--]; }")
c_code.append("int top() { return stack[sp]; }")
c_code.append("int main() {")

# Token translation
i = 0
while i < len(tokens):
    tok = tokens[i]
    if tok.isdigit():
        c_code.append(f"    push({tok});")
    elif tok == "+":
        c_code.append("    push(pop() + pop());")
    elif tok == "-":
        c_code.append("    { int b = pop(); int a = pop(); push(a - b); }")
    elif tok == "*":
        c_code.append("    push(pop() * pop());")
    elif tok == "/":
        c_code.append("    { int b = pop(); int a = pop(); push(a / b); }")
    elif tok == "dup":
        c_code.append("    push(top());")
    elif tok == ".":
        c_code.append('    printf("%d\\n", pop());')
    elif tok == "if":
        c_code.append("    if (pop()) {")
    elif tok == "else":
        c_code.append("    } else {")
    elif tok == "endif":
        c_code.append("    }")
    i += 1

# Add final print of top of stack for debug visibility (optional)
c_code.append('    printf("Top of stack: %d\\n", top());')
c_code.append("    return 0;")
c_code.append("}")

# Write the generated C code to output.c
with open("output.c", "w") as f:
    f.write("\n".join(c_code))

print("C code generated in output.c")

