# write your code here

def three_in_row(field):
    winner = ""
    if field[0][0] == field[0][1] == field[0][2] == "X":
        winner += "X"
    if field[1][0] == field[1][1] == field[1][2] == "X":
        winner += "X"
    if field[2][0] == field[2][1] == field[2][2] == "X":
        winner += "X"
    if field[0][0] == field[1][0] == field[2][0] == "X":
        winner += "X"
    if field[0][1] == field[1][1] == field[2][1] == "X":
        winner += "X"
    if field[0][2] == field[1][2] == field[2][2] == "X":
        winner += "X"
    if field[0][0] == field[1][1] == field[2][2] == "X":
        winner += "X"
    if field[2][0] == field[1][1] == field[0][2] == "X":
        winner += "X"
    if field[0][0] == field[0][1] == field[0][2] == "O":
        winner += "O"
    if field[1][0] == field[1][1] == field[1][2] == "O":
        winner += "O"
    if field[2][0] == field[2][1] == field[2][2] == "O":
        winner += "O"
    if field[0][0] == field[1][0] == field[2][0] == "O":
        winner += "O"
    if field[0][1] == field[1][1] == field[2][1] == "O":
        winner += "O"
    if field[0][2] == field[1][2] == field[2][2] == "O":
        winner += "O"
    if field[0][0] == field[1][1] == field[2][2] == "O":
        winner += "O"
    if field[2][0] == field[1][1] == field[0][2] == "O":
        winner += "O"
    return winner


field = input("Enter cells: ")
n = 0
field_list = [[1,2,3],[4,5,6],[7,8,9]]
for j in range(3):
    for i in range(3):
        field_list[j][i] = field[n]
        n += 1
print("---------")
print("|", field[0], field[1], field[2], "|")
print("|", field[3], field[4], field[5], "|")
print("|", field[6], field[7], field[8], "|")
print("---------")

win = three_in_row(field_list)

if len(field) > 9 or field.count("X") - field.count("O") >= 2\
        or field.count("O") - field.count("X") >= 2\
        or ("X" in win and "O" in win):
    print("Impossible")
elif win == "" and "_" in field:
    print("Game not finished")
elif win == "":
    print("Draw")
elif "X" in win:
    print("X wins")
elif "O" in win:
    print("O wins")
