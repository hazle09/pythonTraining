fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
answer=input("좋아하는 과일은? ")
if answer in fruit.values():
    print("정답입니다")
else:
    print("정답이 아닙니다")