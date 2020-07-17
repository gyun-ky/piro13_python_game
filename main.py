import sys
import hero as h
import executive as e
import chairman as c
import Week1 as w1
import Week2 as w2
import week3 as w3
import Week4 as w4
import Week5 as w5
import week6 as w6
import Week7 as w7
import Week8 as w8
import time


sungik = c.Chairman()
exe = e.Executive()

def dining(myChar, sungik):
    print("********회식 불참 투표********")
    select = input("회식에 참여하시겠습니까?(yes/no) : ")
    if select.upper() == "YES":
        print()
        print(f'회장 {sungik.name} : 흡족합니다!')
        print()
        print('회장의 코딩 능력(공격력)이 5 감소하였다!')
        sungik.controlCoding(-5)
        print(f'{myChar.name}의 비만도가 20 증가하였다')
        myChar.controlObesity(20)
        print(f'{myChar.name}의 피로도가 10 증가하였다')
        myChar.controlPiro(10)
        print()
    elif select.upper() == "NO":
        print()
        print(f'회장 {sungik.name} : 아쉽네요 다음에 함께해요!(찡긋)')
        print()
        print('회장의 코딩 능력(공격력)이 10 증가하였다!')
        sungik.controlCoding(10)
        print(f'{myChar.name}의 비만도가 20 감소하였다')
        myChar.controlObesity(-20)
        print(f'{myChar.name}의 피로도가 10 감소하였다')
        myChar.controlPiro(-10)
        print()
    else:
        print()
        print(f'회장 {sungik.name} : 아니 가시겠다는거에요 말겠다는 거에요?! 올바른 답을 해주셔야죠')
        print()
        print('회장의 코딩 능력(공격력)이 15 증가하였다!')
        sungik.controlCoding(15)
        print()

while(True):
    print("*******P-rogramming*******")
    print("[캐릭터 생성]")
    print(">>피로그래밍 13기 지원서<<")
    name = input("이름 : ")
    
    myChar = h.Hero(name);
    
    print()
    print("*******합격을 축하합니다*******")
    myChar.printInfo()

    print()
    time.sleep(1)
    
    print("[Game Rule]")
    print('''
    * 피로도가 100이 되면 건강 이상! Game Over!
    * 비만도가 100이 되면 건강 이상! Game Over!
    * 보증금이 0원이 되면 다시 시작!
    * 코딩 능력이 100이 되면 하산하시오! 수료!''')
    print()

    time.sleep(2)
    print("===========Week1 : 워크샵===========")
    print()
    w1.memory_name_game(myChar)
    myChar.printInfo()

    check = myChar.diagnose()
    if check == 0:
        sys.exit()
    elif check == 2:
        continue
    print()

    time.sleep(2)
    print("===========Week2 : HTML/CSS를 배우자!===========")
    print("HTML/CSS 인프런 강의를 다 들었는가? 숙되었는가?")
    print("자신있는가? 그럼 한번 검증해보겠다")


    w2.week2_game(myChar)
    myChar.printInfo()
    print()

    time.sleep(2)
    
    print("------------------Week2 : 회식------------------")
    print("Week2부터는 회식이 있다고 한다.")
    dining(myChar, sungik)

    check = myChar.diagnose()
    if check == 0:
        sys.exit()
    elif check == 2:
        continue
    print()
    
    
    print("===========Week3 : 장고 잡기===========")
    print()
    print()

    w3.week__3(myChar)
    myChar.printInfo()

    print()
    
    print("------------------Week3 : 회식------------------")
    dining(myChar, sungik)

    check = myChar.diagnose()
    if check == 0:
        sys.exit()
    elif check == 2:
        continue
    
    
    print("===========!!!Week4 : 중간 점검 | 임원진을 이겨라!!!===========")
    print()

    w4.middle_fight(myChar, exe)
    myChar.printInfo()
    print()
    
    check = myChar.diagnose()
    if check == 0:
        sys.exit()
    elif check == 2:
        continue

    print()
    time.sleep(2)
    print("===========Week5 : 지각하지 말기===========")
    print()

    w5.week5_push(myChar)
    myChar.printInfo()
    print()
    
    print("------------------Week5 : 회식------------------")
    dining(myChar, sungik)

    check = myChar.diagnose()
    if check == 0:
        sys.exit()
    elif check == 2:
        continue
    print()
    
    print("===========Week6 : 컴파일 오류 개수를 찾아라!===========")
    print()
    
    w6.week_6(myChar)
    myChar.printInfo()
    print()
    
    print("------------------Week6 : 회식------------------")
    dining(myChar, sungik)

    check = myChar.diagnose()
    if check == 0:
        sys.exit()
    elif check == 2:
        continue
    print()
    
    print("===========Week7 : 코딩신과의 도박===========")
    print()

    w7.RSP(myChar)
    myChar.printInfo()
    print()
    
    print("------------------Week7 : 회식------------------")
    dining(myChar, sungik)

    check = myChar.diagnose()
    if check == 0:
        sys.exit()
    elif check == 2:
        continue
    print()
    
    print("===========!!!Week8 최종 관문 | 회장님을 이겨라!!!===========")
    print()

    w8.final_fight(myChar, sungik)
    myChar.printInfo()
    print()
    
    check = myChar.diagnose()
    if check == 0:
        sys.exit()
    elif check == 2:
        continue

    print()
    time.sleep(2)
    
    break;

    





