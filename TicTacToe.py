# Tic Toc Toe Game
def same(a,b):
    i=0
    while i < len(a):
        if a[i] == b:
            b = input("Sorry, it has already been taken.. please select another:\n").title()
            i = -1
        i += 1
    return b
def win(table,mark):
    if table[0][0] == table[1][1] == table[2][2] == mark or table[0][2] == table[1][1] == table[2][0] == mark:
        return True
    else:
        for i in range(0,3):
            if table[i][0] == table[i][1] == table[i][2] == mark or table[0][i] == table[1][i] == table[2][i] == mark:
                return True
print("\nTIC TAC TOE GAME")
player1 = [""]
mark1 = [""]
player1[0] = input("Player 1 enter your name:\n").title()
mark1[0] = input(player1[0] + " select your mark from any keyboard character:\n").title()
player2 = input("Player 2 enter your name:\n").title()
player2 = same(player1,player2)
mark2 = input(player2 + " select your mark from any keyboard character:\n").title()
mark2 = same(mark1,mark2)
table = [3*[" "],3*[" "],3*[" "]]
taken =[]
print (type(player1))
print (type(player2))

for i in range(1,10):
    print("┌───┬───┬───┐")
    print("│ "+str(table[0][0])+" │ "+str(table[0][1])+" │ "+str(table[0][2])+" │")
    print("├───┼───┼───┤")
    print("│ "+str(table[1][0])+" │ "+str(table[1][1])+" │ "+str(table[1][2])+" │")
    print("├───┼───┼───┤")
    print("│ "+str(table[2][0])+" │ "+str(table[2][1])+" │ "+str(table[2][2])+" │")
    print("└───┴───┴───┘")
    if i % 2 != 0:
        turn = input(player1[0] + " enter your move <row><column>")
        turn = same(taken,turn)
        table[int(turn[0])-1][int(turn[1])-1] = mark1[0]
    else:
        turn = input(player2 + " enter your move <row><column>")
        turn = same(taken,turn)
        table[int(turn[0])-1][int(turn[1])-1] = mark2    
    taken.append(turn)
    if i > 4:
        if win(table,mark1[0]):
            print(player1[0], "wins !!!")
            break
        elif win(table,mark2):
            print(player2, "wins !!!")
            break
        elif i == 9:
            print("Match tied !!!")