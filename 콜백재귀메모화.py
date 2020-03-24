#재귀함수 예시

#문제1
#팩토리얼
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

#print(factorial(10))


#문제1.5
#피보나치
def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#print(fibonacci(3))


#----------------------------------------------------------------------------
#메모화(memoization)

#문제2
#재귀함수에 메모화를 활용한 팩토리얼 코드
cache = {}

def factorial_recursive(n):
    global cache

    if n in cache:
        return cache[n]
    elif n <= 1:
        return 1
    else:
        cache[n] = n * factorial_recursive(n-1)
        return cache[n]

    return n * factorial_recursive(n-1) if n > 1 else 1

#print(factorial_recursive(10))

#---------------------------------------------
#callback함수
#기본예제1
def call_back(func):
    for i in range (1,10):
        func()

def print_hello():
    print("안녕 파이썬 초딩들")

call_back(print_hello)

#기본예제2
def call_back2(print_hello):
    for i in range (1,10):
        def print_hello2():
            print("안녕 파이썬 초딩들")
        print_hello()

#call_back2(print_hello)    