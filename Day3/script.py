def handle_digit(val, digit):
    digit = digit * 10 + int(val)
    return digit

def sym_check(i, j, games, has_symbol):
    result = has_symbol
    for x in range(-1,2):
        for y in range(-1,2):
            # chack all the neighbour
            row = i+x
            col = j+y
            if row>=0 and row<len(games) and col>=0 and col<len(game):
                # Check for valid rows only
                if not(games[row][col].isalnum()) and not(games[row][col] == '.') :
                    # True when it a symbol
                    result = True
    return result

with open('Day3\Input\input') as file:
    games=file.read().split('\n');

game_point=0
game_result=[]

for i, game in enumerate(games):
    global digit, has_symbol 
    
    digit = 0
    has_symbol = False
    
    for j, val in enumerate(game):
        if(val.isdigit()):
            digit = handle_digit(val, digit)
            has_symbol = sym_check(i, j, games, has_symbol)
        else:
            if has_symbol==True:
                game_point+=digit
                game_result.append(digit)

            digit = 0
            has_symbol = False


print(f"Total points are {game_point}")
print(f"Valid Numbers are {game_result}")
