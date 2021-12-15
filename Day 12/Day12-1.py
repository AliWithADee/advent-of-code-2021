def read_input(path):
    neighbours = {}
    with open(path, "r") as file:
        line = file.readline()
        while line:

            # The Connection:
            # List of two caves that are connected
            connection = line.strip("\n").split("-")

            # Add 2nd cave of the connection to list of neighbours for 1st cave
            if connection[0] in neighbours:
                n_list = neighbours[connection[0]]
                n_list.append(connection[1])
                neighbours[connection[0]] = n_list
            else:
                neighbours[connection[0]] = [connection[1]]
            
            # Add 1st cave of the connection to list of neighbours for 2nd cave
            if connection[1] in neighbours:
                n_list = neighbours[connection[1]]
                n_list.append(connection[0])
                neighbours[connection[1]] = n_list
            else:
                neighbours[connection[1]] = [connection[0]]
            
            line = file.readline()
    
    return neighbours

neighbours = read_input("day 12.txt")
for cave in neighbours:
    print("{}: {}".format(cave, neighbours[cave]))

# Start by looking at the neighbours of "end" and work backwards from there?