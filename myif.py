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

# 여기서 반복
for i in range(5):
while True: # 무한 반복 (계속 참)
    print("그림 출력 프로그램")
    print("=====================")
    print("1. 오리")
    print("2. 곰")
    print("3. 토 끼")
    print("=====================")
    /n = 3
# n = int(input("선택:(0을 압력하면 종료): "))
# 0이 입력되면 프로그램 종료
if n== 0:
    print("프로그램을 종료합니다.")
    break
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

# 동물 그림 출력 프로그램이 총 5번 반복 실행될 수 있게 만드시오.

# 할 수 있는 사람은 프로그램이 계속(무한)반복하게 하고
# 만약에 0을 입력하면 종료 되는 프로그램을 만드시오.