#Week5

import time

def week5_push(Hero):
    print("""
    ▷ 슬슬 느슨해지는 거 같은데?
    ▷ 운영진 하나 이겼다고 자만하는 건가?
    ▷ 지각하지 말자
    ▶ <시간 개념을 지키자> 게임
    """)

    print("enter를 누르면 시작!")
    input()
    print("10초에 맞춰서 enter를 눌러봐. 특별히 아주 조금의 오차는 봐준다")

    start = time.time()
    while (1):
        input("...입력을 기다리는중")
        your_second = time.time() - start
        break

    print()
    print("걸린 시간:", round(your_second, 1))
    print()

    if (12 > your_second > 8):
        print("성공이군.")
        print("코딩 능력이 10 상승 하였다.")
        Hero.controlCoding(10)

    else:
        print("실패군.")
        print("보증금이 1 차감되었다.")
        Hero.controlMoney(-1)
    print("한 주가 무사히 지나갔다. 피로도 5 상승.")
    Hero.controlPiro(5)

    
