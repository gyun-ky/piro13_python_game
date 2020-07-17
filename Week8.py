import random
import time

def final_fight(Hero, Chairman):
    
    print("""
    ▷ 슬슬 느슨해지는 거 같은데?
    ▷ 운영진 하나 이겼다고 자만하는 건가?
    ▷ 지각하지 말자
    ▶ <round 8> 게임
    """)

    print("enter를 누르면 시작!")
    input()


    #week8 에서만 쓰일 변수                 
    ei_obesity = Hero.getObesity()
    eiHero_coding = Hero.getCoding() - Hero.getPiro() * 0.2
    eiCh_coding = Chairman.getCoding()
    ei_confidence = Chairman.getConfidence()
    ei_piro = Hero.getPiro()

    #중간 라운드랑 최종 라운드에서 "코딩능력 = 코딩능력 - 피로도*0.2"
    
    print("깎인 피로도 : ", Hero.getPiro())
    print("선후결정 하겠습니다")

    #누가 먼저 시작?
    member = ["hero", "exe"]
    wF = random.choice(member)
          
    #주인공 먼저
    if(wF == "hero"):
        print(f"{Hero.name}이(가) 먼저 공격합니다")
        while ei_obesity > 0:
            ei_confidence -= eiHero_coding
            if ei_confidence <= 0:
                break
            ei_obesity -= eiCh_coding
            print("\n")

        if ei_obesity > 0 and ei_confidence <= 0:
            print("주인공 이김 / 운영진 짐")
            #코딩능력 / 피로도 상승
            Hero.controlCoding(10)
            Hero.controlPiro(5)

        else:
            print("주인공 짐/ 운영진 이김")
            #보증금 차감 / 피로도 상승
            Hero.controlMoney(-1)
            Hero.controlPiro(5)

    #임원진 먼저
    else:
        print(f"{Chairman.name}(가) 먼저 공격합니다")
        while ei_confidence > 0:
            ei_obesity -= eiCh_coding
            if ei_obesity <= 0:
                break
            ei_confidence -= eiHero_coding
        print("\n")

        if ei_confidence > 0 and ei_obesity <= 0:
            print("임원진 이김 / 주인공 짐")
            #보증금 차감 / 피로도 상승
            Hero.controlMoney(-1)
            Hero.controlPiro(5)
                
        else:
            print("주인공 이김/ 운영진 짐")
            #코딩능력 / 피로도 상승
            Hero.controlCoding(10)
            Hero.controlPiro(5)
