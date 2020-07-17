class Hero:
    def __init__(self, name):
        self.name = name
        self.__piro = 0
        self.__obesity = 0
        self.__coding = 0
        self.__money = 10

    def controlPiro(self, num):
        self.__piro += num
        if self.__piro<0:
            self.__piro = 0

    def controlObesity(self, num):
        self.__obesity += num
        if self.__obesity < 0 :
            self.__obesity = 0

    def controlCoding(self, num):
        self.__coding += num
        if self.__coding < 0 :
            self.__coding = 0

    def controlMoney(self, num):
        self.__money += num
        if self.__money < 0 :
            self.__money = 0

    def getPiro(self):
        return self.__piro

    def getObesity(self):
        return self.__obesity

    def getCoding(self):
        return self.__coding

    def getMoney(self):
        return self.__money
    
    def diagnose(self):
        if self.__piro == 80 or self.__obesity == 100 :
            if self.__piro==80 :
                print("!!!!!피로도 80!!!!!")
            else:
                print("!!!!!비만도 100!!!!!")
            print("엠뷸런스 위이이이잉~")
            print(f'{self.name}부모님 : 왜 우리 애를 이렇게..? 만들었나요?')
            print('회장 : 죄송합니다...')
            print(f'{self.name}은 피로그래밍을 실패하였다. GAME OVER!')
            return 0
        elif self.__coding == 100 :
            print("!!!!!코딩 능력 100!!!!!")
            print("더 이상 배울 것이 없다!")
            print(f'Contratuation!{self.name} You Win')
            return 0
        elif self.__money == 0 :
            print("!!!!!보증금 0원!!!!!")
            print("보증금을 다 까먹었다. 다시 처음부터 시작하라")
            print(f'{self.name}은 피로그래밍을 다시 이수한다. GAME OVER! 처음으로 돌아갑니다.')
            return 2
        else :
            return 1
            
    def printInfo(self):
        print(f'[현재 {self.name}의 상태]')
        print(f'코딩 능력 : {self.__coding}')
        print(f'피로도 : {self.__piro}')
        print(f'비만도 : {self.__obesity}')
        print(f'보증금 : {self.__money}')
        print()
        
        
