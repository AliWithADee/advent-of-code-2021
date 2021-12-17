def read_input(path):
    template = None
    insertions = []
    with open(path, "r") as file:
        template = file.readline().strip("\n")
        line = file.readline()
        line = file.readline()
        while line:
            insertions.append(line.strip("\n").split(" -> "))
            line = file.readline()

    return template, insertions

template, insertions = read_input("test.txt")
polymer = template
print(polymer)

for step in range(1):
    todo = []
    for rule in insertions:
        for c in range(len(polymer) - 1):
            pair = polymer[c] + polymer[c+1]

            if rule[0] == pair:
                todo.append([c+1, rule[1]])
    
    for insert in todo:
        i = insert[0]
        polymer = polymer[:i] + insert[1] + polymer[i:]

    print(polymer)