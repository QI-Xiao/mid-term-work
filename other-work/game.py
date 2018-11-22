from random import randint

name = input('名字：')

f = open('game.txt')
lines = f.readlines()
f.close()

scores = {}
for l in lines:
    s = l.split()
    scores[s[0]] = s[1:]
score = scores.get(name)
if score is None:
    score = [0, 0, 0]

game_times = int(score[0])
min_times = int(score[1])
total_time = int(score[2])
if game_times > 0:
    avg_times = float(total_time)/game_times
else:
    avg_times = 0
print('%s,你已经玩了%d,最少%d猜出答案，平均%.2f轮猜出答案' %(name, game_times, min_times, avg_times))

num = randint(1,100)
times = 0
print('guess')
bingo = False
while bingo == False:
    times += 1
    answer = int(input())
    if answer < num:
        print('too small')
    if answer > num:
        print('too big')
    if answer == num:
        print('bingo')
        bingo = True

if game_times == 0 or times < min_times:
    min_times = times
total_time += times
game_times += 1

scores[name] = [str(game_times), str(min_times), str(total_time)]
result = ''
for n in scores:
    line = n + ' ' + ' '.join(scores[n]) + '\n'
    result += line

f = open('game.txt','w')
f.write(result)
f.close()