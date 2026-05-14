class Board:
    def set_data(self, title, writer):
        self.title = title #오른쪽 title은 호출할때 받아온 매개변수값
                           #왼쪽 title은 객체(붕어빵)의 멤버변수
                           #내자신(객체)의미: self
        self.writer = writer
        self.cnt = 0

    def cntup(self): #조회수 구하는 함수
        self.cnt += 1

# 게시판 객체 생성
board1 = Board()
board2 = Board()

board1.set_data("자바의 정석","홍길동")
board2.set_data("파이썬의 정석","이순신")

board1.cntup()
board1.cntup()
board2.cntup()
print(board1.title, board1.writer, board1.cnt)
print(board2.title, board2.writer, board2.cnt)

board3=Board()
#board3.cnt() set_data()를 호출하지 않으므로 cnt 생성되지 않음 