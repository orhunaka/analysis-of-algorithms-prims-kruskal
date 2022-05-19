with open("graph.txt") as f:
    lines = f.read()
    numberOfNodes = lines.split('\n', 1)[0]

variable_name = "1: 3 4"
char = variable_name.split(':')
print(char)