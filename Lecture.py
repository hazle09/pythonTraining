import csv

f=open('C:\pythonTraining\modifiedLectureList.csv','r',encoding='cp949')
data=csv.reader(f,delimiter=',')

# month=row[0].split('-')[1]
next(data)
day=[]
name=[]


iday=input('원하는 요일을 한글자만 입력하세요(예: 월) >>')
itime=input('원하는 시작 시간(교시)를 입력하세요(예: 7) >>')


for row in data:
    if iday==row[6].split('(')[0]:
        if itime==row[6].split('(')[1][0]:
            name.append([row[3],row[6]])

print('------------------------------------------------')
print('조건에 해당하는 과목의 리스트를 출력합니다.')
print('------------------------------------------------')

if not name:
    print("조건에 해당하는 과목을 찾을 수 없습니다.\n탐색을 종료합니다.")
else:
    for index, value in enumerate(name):
        print('{0:2} {1:10} {2:30} '.format(index+1,value[1],value[0]))


