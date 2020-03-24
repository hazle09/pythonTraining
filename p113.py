a=input("입력: ")
b=a.split()
c=int(b[0])
print(c)
if b[1]=="달러":
    print(c*(1167),'원')
elif b[1]=="엔":
    print(c*(1.196),'원')
elif b[1]=="유로":
    print(c*(1268),'원')
elif b[1]=="위안":
    print(c*(171),'원')