class Board:
    def __init__(self,title,writer): #생성자 
        self.title = title
        self.writer = writer
        self.cnt = 0

    def cntup(self): #조회수 구하는 함수
        self.cnt += 1

board1 = Board("자바의 정석","홍길동")
board2 = Board("파이썬의 정석","이순신")

board1.cntup()
board1.cntup()
board2.cntup()

print(board1.title, board1.writer, board1.cnt)
print(board2.title, board2.writer, board2.cnt)