# 아스키 코드 그림 출력 하기
def print_duck():
    duck = [
          " _",
         "<(o )",
         " (  >)"

    ]
    
    for line in duck:
        print(line)

def print_bear():
    bear = [
       " ʕ•ᴥ•ʔ ",
       " /  つ つ "
    ]

    for line in bear:
        print(line)

def print_rabbit():
    rabbit = [
        " (\(\ ",
        " ( -.-)",
        " o_( )( )"
    ]
    
    for line in rabbit:
        print(line)


print("그림 출력 프로그램")
print("=====================")
print("1. 오리")
print("2. 곰")
print("3. 토 끼")
print("=====================")
n = int(input("선택: "))
# 만약에 1을 입력하면 1번 캐릭터 출력
if n == 1:
    print("오리")
    print_duck()
# 만약에 2를 입력하면 2번 캐릭터 출력
elif n == 2:
    print("곰")
    print_bear()
# 3을 입력하면 3번 캐릭터 출력
elif n == 3:
    print("토끼")
    print_rabbit()
# 잘못입력하면 잘못 입력했다고 출력
else:
    print("잘못입력")