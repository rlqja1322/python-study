def calc(r1):
    result = 3.14 * r1**2
    return result

r= float(input('반지름을 입력하세요 : '))
area = calc(r)
print(area)
#rpint(result)  #result는 함수 내부에서만 사용되는 지역변수이므로 함수 외부에서는 사용할 수 없다.
####################################
def calc2(r2):
    global a # 전역변수 a를 사용하겠다는 선언
    a = 3.14* r2**2
    return a # 지역변수

a=0 # 전역변수
r2= float(input('반지름을 입력하세요 : '))
area2 = calc2(r2)
print(area2)
print(a)
