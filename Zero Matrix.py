import random

row_number = 5
column_number = 5
num_zero = 3

array = []

for index in range(0, column_number):
    temp = []
    for value in range(0, row_number):
        temp.append(1)
    array.append(temp)
        
zero_coords = []

for index in range(0, num_zero):
    zero_coords.append([random.randint(0, row_number-1), random.randint(0, column_number-1)])

for coords in zero_coords:
    array[coords[0]][coords[1]] = 0

coordinates_array = []

for row in range(0, row_number):
    for column in range(0, column_number):
        if (array[row][column] == 0):
            coordinates_array.append([row, column])
            
for row in range(0, row_number):
    print(array[row])
print(coordinates_array)

for coordinates in coordinates_array:
    row_cord = coordinates[0]
    col_cord = coordinates[1]
    for row in range(0, row_number):
        if(row == row_cord):
            for value in range(0, len(array[row])):
                array[row][value] = 0
        if(col_cord <= row_number):
            array[row][col_cord] = 0

for row in range(0, row_number):
    print(array[row])

