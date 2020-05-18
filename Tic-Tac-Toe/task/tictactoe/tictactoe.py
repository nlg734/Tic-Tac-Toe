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


field_list = [[1,2,3],[4,5,6],[7,8,9]]
for j in range(3):
    for i in range(3):
        field_list[j][i] = " "
print("---------")
print("|", field_list[0][0], field_list[0][1], field_list[0][2], "|")
print("|", field_list[1][0], field_list[1][1], field_list[1][2], "|")
print("|", field_list[2][0], field_list[2][1], field_list[2][2], "|")
print("---------")
turn = 0
end = False
while not end:
    end_turn = False
    while not end_turn:
        try:
            x, y = input("Enter the coordinates: ").split()
            x = int(x)
            y = int(y)
            if x > 3 or y > 3:
                print("Coordinates should be from 1 to 3!")
                continue
            elif field_list[3 - y][x - 1] != " ":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                field_list[3 - y][x - 1] = "X"
                print("---------")
                print("|", field_list[0][0], field_list[0][1], field_list[0][2], "|")
                print("|", field_list[1][0], field_list[1][1], field_list[1][2], "|")
                print("|", field_list[2][0], field_list[2][1], field_list[2][2], "|")
                print("---------")
                end_turn = True
        except ValueError:
            print("You should enter numbers!")
            continue
        except EOFError:
            print("Enter two numbers!")
            continue
    turn += 1
    win = three_in_row(field_list)

    if "X" in win:
        print("X wins")
        end = True
        break
    elif "O" in win:
        print("O wins")
        end = True
        break
    elif win == "" and turn == 9:
        print("Draw")
        end = True
        break
    end_turn = False
    while not end_turn:
        try:
            x, y = input("Enter the coordinates: ").split()
            x = int(x)
            y = int(y)
            if x > 3 or y > 3:
                print("Coordinates should be from 1 to 3!")
                continue
            elif field_list[3 - y][x - 1] != " ":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                field_list[3 - y][x - 1] = "O"
                print("---------")
                print("|", field_list[0][0], field_list[0][1], field_list[0][2], "|")
                print("|", field_list[1][0], field_list[1][1], field_list[1][2], "|")
                print("|", field_list[2][0], field_list[2][1], field_list[2][2], "|")
                print("---------")
                end_turn = True
        except ValueError:
            print("You should enter numbers!")
            continue
        except EOFError:
            print("Enter two numbers!")
            continue
    turn += 1

    win = three_in_row(field_list)
    if "X" in win:
        print("X wins")
        end = True
    elif "O" in win:
        print("O wins")
        end = True
