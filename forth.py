import sys

class ForthInterpreter:
    def __init__(self):
        self.stack = []
        self.words = {}

    def run(self, code):
        tokens = code.strip().split()
        i = 0

        while i < len(tokens):
            token = tokens[i].upper()

            if token == ':':
                # Begin word definition
                i += 1
                word_name = tokens[i].upper()
                i += 1
                word_body = []
                while tokens[i] != ';':
                    word_body.append(tokens[i])
                    i += 1
                self.words[word_name] = word_body
            elif token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                self.stack.append(int(token))
            elif token in self.words:
                # Expand user-defined word
                self.run(' '.join(self.words[token]))
            elif token == '+':
                self.stack.append(self.stack.pop() + self.stack.pop())
            elif token == '-':
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a - b)
            elif token == '*':
                self.stack.append(self.stack.pop() * self.stack.pop())
            elif token == '/':
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a // b)
            elif token == 'DUP':
                self.stack.append(self.stack[-1])
            elif token == 'DROP':
                self.stack.pop()
            elif token == 'SWAP':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(a)
                self.stack.append(b)
            elif token == '.':
                print(self.stack.pop())
            else:
                print(f"Unknown word: {token}")
            i += 1

def main():
    if len(sys.argv) < 2:
        print("Usage: python forth.py <file.frt>")
        return

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        code = f.read()

    interpreter = ForthInterpreter()
    interpreter.run(code)

if __name__ == '__main__':
    main()

