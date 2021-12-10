def read_bingo(path):
    numbers = []
    boards = []
    with open(path, "r") as file:
        line = file.readline()
        numbers_str = line.strip("\n").split(",")
        for n in numbers_str: numbers.append(int(n))
        
        while line:
            line = file.readline()
            if line != "\n":
                board = []
                for i in range(5):
                    row = []
                    for n in line.strip("\n").split(" "):
                        if n != "":
                            row.append(int(n))
                            
                    board.append(row)
                    line = file.readline()
                    
                boards.append(board)
                
    return numbers, boards

numbers, boards = read_bingo("day 4.txt")

MARKED = "MARKED"

boards_marked = []
for i in range(len(boards)):
    board = []
    for j in range(5):
        board.append([None, None, None, None, None])
    boards_marked.append(board)

result = 0
for n in range(len(numbers)):
    if len(boards) <= 0: break

    drawn_num = numbers[n]
    
    for b in range(len(boards)):
        for r in range(5):
            for c in range(5):
                num = boards[b][r][c]
                
                if num == drawn_num:
                    boards_marked[b][r][c] = MARKED
    
    to_remove = []
    for b in range(len(boards_marked)):
        bingo = False  
        for r in range(5):
            row = boards_marked[b][r]
            if None not in row:
                bingo = True
                break

        for c in range(5):
            if bingo: break

            column = []
            for i in range(5):
                column.append(boards_marked[b][i][c])
                
            if None not in column:
                bingo = True
                break

        if bingo:
            if len(boards) == 1:
                board_sum = 0
                for r in range(5):
                    for c in range(5):
                        if boards_marked[b][r][c] == None:
                            board_sum += boards[b][r][c]
                            
                result = board_sum * drawn_num

            board = boards[b]
            marked = boards_marked[b]
            to_remove.append([board, marked])
            
    for remove in to_remove:
        boards.remove(remove[0])
        boards_marked.remove(remove[1])

print(result)