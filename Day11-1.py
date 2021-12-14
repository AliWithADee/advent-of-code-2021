def read_input(path):
    octos = []
    with open(path, "r") as file:
        line = file.readline()
        while line:
            row = []
            for c in line.strip("\n"):
                row.append(int(c))
                
            octos.append(row)
            line = file.readline()

    return octos
            
octos = read_input("test.txt")
print("Initial")
for row in octos:
    print(row)
print()

def get_neighbours(r, c):
    neighbours = []
    row = octos[r]

    # NESW
    if r != 0:# North
        neighbours.append([r-1, c])
    if c != len(row) - 1: # East
        neighbours.append([r, c+1])
    if r != len(octos) - 1: # South
        neighbours.append([r+1, c])
    if c != 0: # West
        neighbours.append([r, c-1])
        
    # Diagonals
    if r != 0 and c != 0: # North West
        neighbours.append([r-1, c-1])
    if r != 0 and c != len(row) - 1: # North East
        neighbours.append([r-1, c+1])
    if r != len(octos) - 1 and c != len(row) - 1: # South East
        neighbours.append([r+1, c+1])
    if r != len(octos) - 1 and c != 0: # South West
        neighbours.append([r+1, c-1])
    
    return neighbours
    

for step in range(1):
    for r in range(len(octos)):
        row = octos[r]
        for c in range(len(row)):
            octos[r][c] += 1

    print("Step {}".format(step+1))
    for row in octos:
        print(row)
    print()
    
    for r in range(len(octos)):
        row = octos[r]
        for c in range(len(row)):
            energy = octos[r][c]

            # If > 9
            if energy > 9:

                neighbours = get_neighbours(r, c)
                for n in neighbours:
                    octos[n[0]][n[1]] += 1
                        
                new_neighbours = neighbours

                while new_neighbours != []:
                    new_neighbours = []
                    for n in neighbours:
                        if octos[n[0]][n[1]] > 9:
                            new_neighbours.append(get_neighbours(n[0], n[1]))
                    
                    for n in new_neighbours:
                        octos[n[0]][n[1]] += 1
                    
                    neighbours = new_neighbours
                    
                    
