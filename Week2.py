import time
import random

def week2_game(Hero):
    print("""
    ▷ html/css 인프런 강의를 다 들었는가?
    ▷ 숙련되었는가?
    ▷ 그렇다면 htmlcss 용어를 맞혀보자
    ▶ <htmlcss 능숙해?> 게임
    """)

    print('시작하려면 enter를 눌러라.')
    input()
    print()

    word = ["opacity", "display", "position"]
    answer = word[random.randrange(0,3)]

    print(f'글자 수 : {len(answer)}')
    compare = []
    answerList = []

    for char in answer:
        answerList.append(char)
        compare.append("_")
        
    
    for char in compare:
            print(char, end="")
            
    print()
    i = 0
    
    while i<len(answer)+2:
        print(f'{len(answer)+2}번의 기회 중 {i+1}번째')
        letter = input("글자를 입력 : ")
        index = answer.find(letter)
        if index == -1:
            print("찾는 값이 없다! 기회 날림요")
            if i ==len(answer)+1:
                print("망")
                Hero.controlMoney(-1)
                Hero.controlPiro(5)
                print()
                break;
            i+=1
            continue;
        compare[index] = letter
        for char in compare:
            print(char, end="")
        print()
        i+=1
        if compare == answerList:
            print("축하합니다!")
            Hero.controlCoding(10)
            Hero.controlPiro(5)
            print()
            break;
        elif compare!=answerList and i ==len(answer)+1:
            print("망")
            Hero.controlMoney(-1)
            Hero.controlPiro(5)
            print()
            break;
