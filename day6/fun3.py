def dis_price(price,dis):


    A = price - (price * dis / 100)
    return A

#A상품 : 10000원, 10% 할인 
price_A = dis_price(10000, 10)
print(int (price_A))      #할인금액을 뺀 금액 출력

# B상품 : 50000원, 20% 할인
price_B = dis_price(50000, 20)
print(int (price_B))      #할인금액을 뺀 금액 출력



