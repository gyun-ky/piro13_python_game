import random

def middle_fight(Hero, Executive):
    
    print("""
    ▷ 슬슬 느슨해지는 거 같은데?
    ▷ 운영진 하나 이겼다고 자만하는 건가?
    ▷ 지각하지 말자
    ▶ <round 4> 게임
    """)

    print("enter를 누르면 시작!")
    input()


    #week4 에서만 쓰일 변수                 
    xi_obesity = Hero.getObesity()
    xiHero_coding = Hero.getCoding() - Hero.getPiro() * 0.2
    xiExe_coding = Executive.getCoding()
    xi_confidence = Executive.getConfidence()
    xi_piro = Hero.getPiro()

    #중간 라운드랑 최종 라운드에서 "코딩능력 = 코딩능력 - 피로도*0.2"
    
    print("깎인 피로도 : ", Hero.getPiro())
    print("선후결정 하겠습니다")

    #누가 먼저 시작?
    member = ["hero", "exe"]
    wF = random.choice(member)
          
    #주인공 먼저
    if(wF == "hero"):
        print(f"{Hero.name}이(가) 먼저 공격합니다")
        while xi_obesity > 0:
            xi_confidence -= xiHero_coding
            if xi_confidence <= 0:
                break
            xi_obesity -= xiExe_coding
            print("\n")

        if xi_obesity > 0 and xi_confidence <= 0:
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
        print(f"{Executive.name}(가) 먼저 공격합니다")
        while xi_confidence > 0:
            xi_obesity -= xiExe_coding
            if xi_obesity <= 0:
                break
            xi_confidence -= xiHero_coding
        print("\n")

        if xi_confidence > 0 and xi_obesity <= 0:
            print("임원진 이김 / 주인공 짐")
            #보증금 차감 / 피로도 상승
            Hero.controlMoney(-1)
            Hero.controlPiro(5)
                
        else:
            print("주인공 이김/ 운영진 짐")
            #코딩능력 / 피로도 상승
            Hero.controlCoding(10)
            Hero.controlPiro(5)
