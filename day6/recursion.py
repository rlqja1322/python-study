# #재귀 호출(함수)(함수 내부에서 자기자신을 호출)
# #5!(팩토리얼): 5*4*3*2*1
# def fact(n): #fact:함수명(매개변수는 1개)
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)



# a=int(input("정수를 입력하세요 : "))
# res = fact(a) #함수 호출, 인수 a(정수) 보냄
# # 반환되어서 온 결과값을 res에 저장
# print(a,"!은",res,"이다")

def fact2(n):
    if n == 1:
        return 1
    else:
        return n + fact2(n-1)
n = int(input("정수를 입력하세요 : "))
res= fact2(n)
print(f"1부터 {n}까지의 합은 {res}이다")