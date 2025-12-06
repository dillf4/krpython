x = 0
def 출력하다(b): #print
    print(b)
    return 0

def 정수x(a): #int
    global x
    x = a
    return 0
def 입력하다(): #input()
    return input()

#test code 테스트 코드
정수x(입력하다())
출력하다("안녕 세계!")
출력하다(x)
