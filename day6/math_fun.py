res=divmod(11,3)
print(res) #몫과 나머지를 튜플로 반환   3,2 몫(//), 나머지(%)
print(abs(-5)) #절대값 반환
print(pow(4,2)) #4의 2제곱 반환
print(max(10,30,5)) #최댓값 반환
print(min(10,30,5)) #최솟값 반환
print(round(12.89)) #소수점 2자리까지 반올림
print(round(12.89,1)) #소수점 1자리까지 반올림

import math
from math import * 
#math 모든 함수를 네임스페이스에 가져옴
#내림
print(floor(24.9))
#올림
print(math.ceil(23.8))
print(math.sqrt(16)) #제곱근 반환
print(math.factorial(5)) #팩토리얼반환
print(math.pi)