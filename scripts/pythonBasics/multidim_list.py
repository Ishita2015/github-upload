rooms = [[[False for r in range(20)] for f in range(15)] for b in range (3)]

# second building, on the tenth floor, room 14
rooms[1][9][13] = True

# release the second room on the fifth floor located in the first building
rooms [0][4][1] = False

# Check if there are any vacancies on the 15th floor of the third building
rooms[2][14][2] = True
vacancy = 0
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
print(vacancy)
