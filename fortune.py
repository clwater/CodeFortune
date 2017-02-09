import random


def getAotu():


    a1 = random.random()
    a2 = random.random()
    a3 = random.random()
    b1 = random.random()
    b2 = random.random()
    b3 = random.random()

    if a1 > 0.5:
        a1 = 1
    else :
        a1 = 0
    if a2 > 0.5:
        a2 = 1
    else:
        a2 = 0
    if a3 > 0.5:
        a3 = 1
    else:
        a3 = 0

    if b1 > 0.5:
        b1 = 1
    else:
        b1 = 0
    if b2 > 0.5:
        b2 = 1
    else:
        b2 = 0
    if b3 > 0.5:
        b3 = 1
    else:
        b3 = 0

    a = a1 * 4 + a2 * 2 + a3
    b = b1 * 4 + b2 * 2 + b3

    getDivination(a , b)

def getDvinationBase():
    base64gua = ['乾' , '坤' , '屯' , '蒙' , '需' , '讼' , '师' , '比' ,
                 '小畜' , '履' , '泰' , '否' , '同人' , '大有' , '谦' , '豫' ,
                 '随', '蛊', '临', '观', '噬嗑', '贲', '剥', '复',
                 '无妄', '大畜', '颐', '大过', '坎', '离', '咸', '恒',
                 '遯', '大壮', '晋', '明夷', '家人', '睽', '蹇', '解',
                 '损', '益', '夬', '姤', '萃', '升', '困', '井',
                 '革', '鼎', '震', '艮', '渐', '归妹', '丰', '旅',
                 '巽', '兑', '涣', '节', '中孚', '小过', '既济', '未济'
                 ]
    _dvinationList = []

    i = 0
    while i < 64:
        _dvination = []
        _dvination.append(i)
        _dvination.append(base64gua[i])
        _dvinationList.append(_dvination)
        i = i + 1

    return _dvinationList



def getDivination(a , b):
    _dvinationList = getDvinationBase()

    dvination  = 0
    # 0 000 坤
    # 1 001 艮
    # 2 010 坎
    # 3 011 巽
    # 4 100 震
    # 5 101 离
    # 6 110 兑
    # 7 111 乾

    if a == 0:
        if b == 0:
            dvination = 1
        elif b == 1:
            dvination = 22
        elif b == 2:
            dvination = 8
        elif b == 3:
            dvination = 19
        elif b == 4:
            dvination = 15
        elif b == 5:
            dvination = 34
        elif b == 6:
            dvination = 44
        elif b == 7:
            dvination = 12
    elif a == 1 :
        if b == 0:
            dvination = 14
        elif b == 1:
            dvination = 51
        elif b == 2:
            dvination = 38
        elif b == 3:
            dvination = 52
        elif b == 4:
            dvination = 61
        elif b == 5:
            dvination = 55
        elif b == 6:
            dvination = 30
        elif b == 7:
            dvination = 32
    elif a == 2 :
        if b == 0:
            dvination = 6
        elif b == 1:
            dvination = 3
        elif b == 2:
            dvination = 28
        elif b == 3:
            dvination = 58
        elif b == 4:
            dvination = 39
        elif b == 5:
            dvination = 63
        elif b == 6:
            dvination = 46
        elif b == 7:
            dvination = 5
    elif a == 3 :
        if b == 0:
            dvination = 45
        elif b == 1:
            dvination = 17
        elif b == 2:
            dvination = 47
        elif b == 3:
            dvination = 56
        elif b == 4:
            dvination = 31
        elif b == 5:
            dvination = 49
        elif b == 6:
            dvination = 27
        elif b == 7:
            dvination = 43
    elif a == 4 :
        if b == 0:
            dvination = 23
        elif b == 1:
            dvination = 26
        elif b == 2:
            dvination = 2
        elif b == 3:
            dvination = 41
        elif b == 4:
            dvination = 50
        elif b == 5:
            dvination = 20
        elif b == 6:
            dvination = 16
        elif b == 7:
            dvination = 24
    elif a == 5 :
        if b == 0:
            dvination = 35
        elif b == 1:
            dvination = 21
        elif b == 2:
            dvination = 62
        elif b == 3:
            dvination = 36
        elif b == 4:
            dvination = 54
        elif b == 5:
            dvination = 30
        elif b == 6:
            dvination = 48
        elif b == 7:
            dvination = 12
    elif a == 6 :
        if b == 0:
            dvination = 18
        elif b == 1:
            dvination = 40
        elif b == 2:
            dvination = 59
        elif b == 3:
            dvination = 60
        elif b == 4:
            dvination = 53
        elif b == 5:
            dvination = 37
        elif b == 6:
            dvination = 57
        elif b == 7:
            dvination = 9
    elif a == 7 :
        if b == 0:
            dvination = 10
        elif b == 1:
            dvination = 25
        elif b == 2:
            dvination = 4
        elif b == 3:
            dvination = 8
        elif b == 4:
            dvination = 33
        elif b == 5:
            dvination = 13
        elif b == 6:
            dvination = 42
        elif b == 7:
            dvination = 0


    print(_dvinationList[dvination])


def fortune():
    getAotu()

fortune()