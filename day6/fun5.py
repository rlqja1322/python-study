# *args : arguments의 약자로, 위치 인자들을 함수로 전달할 때 사용됨 (튜플)
# **kwargs : keyword arguments의 약자로, 키워드 인자들을 함수로 전달할 때 사용됨 (딕셔너리)

def manyParam(*args):
    # 몇개의 매개변수를 받을 지 모를 때는 args 앞에 *를 사용한다
    print(type(args))  # 튜플로 전달됨
    sum = 0
    for i in args:
        sum += i
    return sum

print(manyParam(1,2,3,4,5,6,7,8,9,10))  # 55
print(manyParam(1,2,3,4,5))  # 15
print('-'*30)    

def dictParam(**kwargs):
    # **kwargs는여러개의 매개변수를 받으며 딕셔너리 형태로 함수 내부에 전달
    print(kwargs)  # 딕셔너리로 전달됨

    dictParam(a= 'A') #{a : A}
    dictParam(x = 10, y = 20, z= 30) #{'x' : 10, 'y' : 20, 'z' : 30}
    print('-'*30)