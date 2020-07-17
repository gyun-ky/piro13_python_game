def week_6(myChar):

    import random
    rannum = random.randint(30,50)
    count = 0
    print('''Up & Down 게임입니다. 랜덤으로 생성된 30에서 50사이의 수를  4회 안에 맞혀주세요.
    30에서 50사이에 한 가지 정수를 입력해주세요.''')
    number = int(input(''))
    
    while True:
        count += 1
        if (count > 3):
            print('통과하지 못했습니다.')
            myChar.controlPiro(5)
            myChar.controlCoding(10)
            break
        elif (number > rannum) :
            print('다운')
        elif (number < rannum) :
            print('업')
        else:
            print('정답입니다.')
            myChar.controlPiro(5)
            myChar.controlMoney(-10000)
            break
        number = int(input('입력해주세요.\n'))
