numbers=input("주민번호를 입력하시오>>") #980925-1234567
numlist=[2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5] #for문으로 상콤하게 곱할 예정
result=0
newnumbers=numbers.split("-") #980925와 1234567로 나놔줌
new=newnumbers[0]+newnumbers[1] #9809251234567로 하나의 문자열을 만들었다

for i in range(0,12): #12번 돌릴게
    result+=int(new[i])*numlist[i] #아까만든 하나의 문자열과 위에 만들어놓은 리스트를 같이 곱해주고 result변수에 저장*12
result2=11-(result%11) #하라는 대로 계산
if result2==int(numbers[13]): 
    print("유효한 주민번호입니다")
else:
    print("유효하지 않은 주민번호입니다")

    