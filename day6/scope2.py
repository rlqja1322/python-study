# 스코프(scope)
# 파이썬은 변수를 찾을때 가까운 영역부터 찾는다
# LEGB 규칙(Local -> Enclosing -> Global -> Built-in)
# 1. 지역변수(local variable) : 함수 내부에서 선언된 변수(함수의 매개변수도 지역변수로 간주됨)
# 2. 전역변수(global variable) : 함수 외부에서 선언된 변수(모든 함수에서 접근 가능)
# 3. Enclosing variable : 중첩된 함수에서 외부 함수의 변수(중첩된 함수에서 가장 가까운 외부 함수의 변수)
# 4. Built-in variable : 파이썬이 기본적으로 제공하는 변수(예: len, print 등)
# 스코프(scope) : 변수의 유효 범위, 즉 변수가 참조될 수 있는 영역
a = '홍길동'  #전역
b = 99

def function1():
    a = '이순신' #중첩
    c = [1 ,2 ,3] 
    
    def function2():
        d = (1, 2, 3) #지역
        print('Local a =',a) #이순신
        print('Local b =',b) #99
        print('Local c =',c) #[1, 2, 3]
        print('Local d =',d) # (1, 2, 3)
        
    
    function2()
    print('Enclosing a =',a) #이순신
    print('Enclosing b =',b) #99
    print('Enclosing c =',c) #[1, 2, 3]
    print('Enclosing d =',d) #오류
function1()
print('Global a =',a) #홍길동
print('Global b =',b) #99
print('Global c =',c) #오류
print('Global d =',d) #오류