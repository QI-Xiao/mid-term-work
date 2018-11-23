# -*- coding: utf-8 -*-

with open('report.txt',encoding='utf8') as report:
    scores = report.readlines()

total_score = ['姓名',0,0,0,0,0,0,0,0,0]
scores = [x.split() for x in scores]
score_title = scores[0]
score_list = scores[1:]
for line in score_list:
    sum_one = 0
    for i in line[1:]:
        sum_one += int(i)
        total_score[line.index(i)] += int(i) # 这一步
        if int(i)<60:
            # i = '不及格' # i不会return
            line[line.index(i)] = '不及格'
    avr_one = sum_one / 9
    line.append('%d' %sum_one)
    line.append('%.1f' %avr_one)
score_list = sorted(score_list, key = lambda x:x[11], reverse = True)

total_score.append(sum(total_score[1:]))
total_score = ['%.1f' %(x/len(score_list)) for x in total_score[1:]]
total_score.append('%.1f' %(float(total_score[-1])/9))
total_score.insert(0, '平均')
total_score.insert(0, '0')
score_title.insert(0, '名次')
score_title.append('总分')
score_title.append('平均分')

score_list = [['%d' %(score_list.index(x)+1)]+x for x in score_list]
score_list = [score_title] + [total_score] + score_list
result = [' '.join(x) + '\n' for x in score_list]
print(result)
with open('new_report.txt', 'w', encoding='utf8') as f:
    f.writelines(result)
