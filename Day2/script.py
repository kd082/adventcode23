with open('Day2\Input\sample') as file:
    games = file.read().strip().split('\n')


ValidGames = []
v_total = 0
power=0

for game in games:
    blues=[]
    greens=[]
    reds=[]

    results = game.split()
    flag = True

    for i, score in enumerate(results):
        if 'blue' in score:
            blues.append(int(results[i - 1]))
            if int(results[i - 1]) > 14:
                flag = False

        elif 'green' in score:
            greens.append(int(results[i - 1]))
            if int(results[i - 1]) > 13:
                flag = False

        elif 'red' in score:
            reds.append(int(results[i - 1]))
            if int(results[i - 1]) > 12:
                flag = False


    if flag == True:
        ValidGames.append(results[1][0:-1])
        v_total += int(results[1][0:-1])

    power+=max(blues)*max(greens)*max(reds)

print(v_total)
print(power)