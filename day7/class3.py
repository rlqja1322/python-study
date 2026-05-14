# class_ex.py
# 부모 클래스
class Passbook:
    def __init__(self,owner,balance): # 생성자
        #생성자(객체 생성하면서 초기값을 저장)       
        self.owner=owner
        self.balance=balance
    def  deposit(self,money): #입금하는 함수
        self.balance += money      #입금금액 money를 balance(객체멤버변수)에 더함
        print(f"{money}원이 입금되었습니다.") #입금금액 money 출력
        print(f"현재 잔액은 {self.balance}원")  #현재 잔액 출력

        #예) 출금 5000원, 잔액 3000원 -> "잔액이 부족합니다." 출력
    def withdraw(self,money): #출금하는 함수
        if self.balance >= money:
            #잔액이 출금금액보다 크거나 같아야함
            self.balance -= money
            print(f"{money}원이 출금되었습니다.")
            print(f"현재 잔액은 {self.balance}원")
        else:
            print("잔액이 부족합니다.")
    def showInfo(self):
        print(f"예금주: {self.owner}")
        print(f"잔액: {self.balance}")

class MinusPassbook(Passbook):
    #재정의(오버라이딩)
    def withdraw(self,money): #출금하는 함수

        if self.balance >= money:
            #잔액이 출금금액보다 크거나 같아야함
            self.balance -= money
            print(f"{money}원이 출금되었습니다.")
            print(f"현재 잔액은 {self.balance}원")
        else:
            print("마이너스 한도 잔액 부족.")
#실행
#객체 생성 account1 + 생성자 호출(예금주:홍길동, 잔액:100,000)
account1 = Passbook("홍길동",100000)
#입금 함수 호출 50,000원 입금
account1.showInfo()
account1.deposit(50000)
#출금 함수 호출 120,000원 출금
account1.withdraw(120000)
#출금 함수 호출 70,000원 출금
account1.withdraw(70000)
account1.showInfo()


account2 = MinusPassbook("김철수",100000)
account2.showInfo()
account2.deposit(50000)
account2.withdraw(120000)
account2.withdraw(9000000)