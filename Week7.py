#Week7

import random

def RSP(Hero): 

    print("""
    ▷ 내 코딩 능력이 애매해 팀플할 때 힘이 든다.
    ▷ '코딩신이여, 도와주세요!!!'
    ▷ 코딩신을 이기면 당신이 건 코딩 능력만큼 더해주고, 아니라면 뺏겠다.
    ▶ <코딩신과의 가위 바위 보> 게임
    """)

    print("enter를 누르면 게임이 시작된다.")
    input()

    while(1):
        bonus = int(input("코딩 능력을 얼만큼 걸텐가? : "))
        if 0 < bonus <= Hero.getCoding() :
            print("당신은 {0}만큼 걸기로 했다.".format(bonus))
            break
        elif 0 == Hero.getCoding():
            print("껄껄 당신.. 코딩 능력이 없군. 그냥 가위바위보나 한 판 하세.")
            break
        else:
            print("장난하나? 다시!")

    user_value = input("가위, 바위, 보: ")
    codingshin = random.randrange(1, 3) # 1은 가위, 2는 바위, 3은 보

    if (user_value=='가위' and codingshin == 3 ) or (user_value =='바위' and codingshin ==1) or (user_value == '보' and codingshin ==2):
        print("승리! 코딩 능력 상승 +{0}!".format(bonus))
        Hero.controlCoding(bonus)
        
    elif (user_value =='가위' and codingshin ==1) or (user_value =='바위' and codingshin ==2) or (user_value =='보' and codingshin ==3):
        print("비겼다. 코딩능력에 변화가 없다.")

    else :
        print("패배! 코딩 능력 하락 -{0}!".format(bonus))
        Hero.controlCoding(-bonus)

    print("한 주가 무사히 지나갔다. 피로도 5 상승.")
    Hero.controlPiro(5)
