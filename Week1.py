#Week1

import time
import random


def memory_name_game(Hero):

    print("""
    ▷ 워크샵이다
    ▷ 13기 동료들의 이름은 다 외웠겠지?
    ▷ 한 번 확인해보겠다. '40초 안에 7명 이상'을 맞혀라.
    ▶ <이름 기억하기> 게임
    """)
    count = 0
    names = ['Leejinhee', 'Yoobyungwook', 'Hanjiyoung', 'Leeyoorim', 'Sonminjoo'
             , 'Choisangyoon', 'Kimwooyoung', 'Parkhanseok', 'Sonheewoo',
             'Parkyejin', 'Leehyein', 'Ohchaeeun', 'Kimhakyung', 'Koeunseo',
             'Okhyewon', 'Jungsoohyun', 'Sonyoungjoon', 'Baeinkyung', 'Choiinji',
             'Leejiho', 'Parksomin', 'Kimkiyoon', 'Shinminji', 'Leeyejin']

    print('시작하려면 enter를 눌러라.')
    input()

    t_end = time.time() + 40
    while time.time() < t_end:
      
        Q = random.choice(names)
        print("")
        print('[', Q, ']')
        names.remove(Q)
        A = input('→')
        if Q == A:
            print('잘 외운 것 같다!')
            print('남은 시간:',round(t_end - time.time(), 1))
            print("==================================")
            print("")
            count += 1
            
        else:
            print(Q, '이(가) 당신을 싫어하는 것 같다.')
            print('남은 시간:',round(t_end - time.time(), 1))
            print("==================================")
            print("")

        if Q == []:
            print("이제 칠 이름이 없다.")


        
    print("=================================")
    print("Week1 완료!")
    print("네 점수는 {0}점이다.".format(count))
    print("=================================")
    print()
    
    if count >= 7 :
        print("축하한다. Week1을 통과하였다.")
        print("코딩 능력이 10 상승 하였다.")
        Hero.controlCoding(10)
    else:
        print("Week1을 실패하였다. 사요나라~")
        print("보증금이 2 차감되었다.")
        Hero.controlMoney(-2)
    print("한 주가 무사히 지나갔다. 피로도 5 상승.")
    Hero.controlPiro(5)
    print()
