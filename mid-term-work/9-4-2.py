# -*- coding: utf-8 -*-

with open('guess number.txt',encoding='utf8') as guess_number:
    report = guess_number.readlines()

nickname = input('请输入姓名：\n')
report = [x.split() for x in report]
score = {}
for i in report:
    score[i[0]] = i[1:]
if nickname in score:
    game_time = int(score[nickname][0])
    game_total_round = int(score[nickname][1])
    game_avr_round = float(score[nickname][2])
    game_best_round = int(score[nickname][3])
    print('欢迎回来，%s' %nickname)
else:
    [game_time,game_total_round, game_avr_round, game_best_round] = [0,0,0,float('inf')]
    print('欢迎新玩家，%s' %nickname)

import random

while True:
    guess_round = 0
    game_time += 1
    num = random.randint(1,100)
    while True:
        try:
            ans = int(input('猜1-100\n'))
            guess_round += 1
            if ans < num:
                print('小了')
            elif ans > num:
                print('大了')
            else:
                print('猜对了')
                print('猜了%d次' % guess_round)
                game_total_round = game_total_round + guess_round
                game_avr_round = game_total_round/game_time
                game_best_round = min(guess_round,game_best_round)
                print('共猜%d局，平均%.1f次猜中' % (game_time, game_avr_round))
                print('最好成绩%d' % game_best_round)
                score[nickname] = [str(game_time), str(game_total_round), str(game_avr_round), str(game_best_round)]
                break
        except:
            continue
    go_again = input('go again?\n')
    if go_again == 'go':
        continue
    else:
        break

report = [' '.join([x]+score[x])+'\n' for x in score]
with open('guess number.txt','w',encoding='utf8') as f:
    f.writelines(report)

print(report)
