def get_lotto_numbers():
    from random import randint
    numbers = [] #비어있는 리스트
    while len(numbers) < 6:
        n=random.andint(1,45) 

        if n not in numbers: #포함하지 않나
            numbers.append(n) #numbers에 n을 추가
        return numbers