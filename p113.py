a=input("입력: ")
a.split()
print(float(a[0]))
if a[1]=='달러':
    print(a[0]*(1167/1000),'원')
elif a[1]=='엔':
    print(a[0]*(1.196/1000),'원')
elif a[1]=='유로':
    print(a[0]*(1268/1000),'원')
elif a[1]=='위안':
    print(a[0]*(171/1000),'원')