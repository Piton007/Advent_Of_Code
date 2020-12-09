airplane = [0  for i in range(128) ]
for i in range(len(airplane)):
    airplane[i] = [0 for j in range(8)]

ids = {}

def my_seat():

    for i in range(len(airplane)):
        for j in range(len(airplane[i])):
            my_id = i * 8 + j
            front,back  = my_id + 1 , my_id - 1

            if airplane[i][j] == 0 and front in ids and back in ids:
                return my_id

def id(encoded):
    last_row_inst = ''
    last_column_inst = '' 
    row_pivots = [0,127]
    column_pivots = [0,7]

    for c in encoded:
        if c == "B" or c == "F":
            mid = (row_pivots[1] + row_pivots[0] )//2
            if c == "F":
                row_pivots = [row_pivots[0], mid]
            if c == "B":
                row_pivots = [mid + 1 , row_pivots[1]]
            last_row_inst = c
        if c == "R" or c == "L":
            mid = (column_pivots[1] + column_pivots[0] )//2
            if c == "L":
                column_pivots = [column_pivots[0], mid ]
            if c == "R":
                column_pivots = [mid + 1, column_pivots[1]]
            last_column_inst = c

    row = row_pivots[0] if last_row_inst == "B" else row_pivots[1]
    column = column_pivots[1] if last_column_inst == "R" else column_pivots[0]
    airplane[row][column] = 1
    return row,column

with open("ex5.txt","r") as file:
 
    for line in file:
        row,column = id(line)
        ids[row * 8 + column ] = True
    print(my_seat())
    file.close()
