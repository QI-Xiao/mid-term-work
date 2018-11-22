# -*- coding:utf-8 -*-

def load_blocked():
    with open('words2.txt',encoding = 'utf8') as f:
        global blocked_words
        blocked_words = [l.strip() for l in f.readlines() if f]

def words_filter(text, symbol = '*'):
    for w in blocked_words:
        text = text.replace(w, symbol * len(w))
    return text

if __name__ == '__main__':
    load_blocked()
    while True:
        t= input ('输入文字（直接回车退出）：\n')
        if not t:
            break
        print (words_filter(t))