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
print("3. 토끼")
print("0. 종료")
print("=====================")

# 무한 반복
while True:
    n = int(input("선택: "))  # 사용자 입력 받기

    # 0을 입력하면 종료
    if n == 0:
        print("프로그램을 종료합니다.")
        break  # 루프 종료

    # 1을 입력하면 오리 출력
    elif n == 1:
        print("오리")
        print_duck()
    # 2를 입력하면 곰 출력
    elif n == 2:
        print("곰")
        print_bear()
    # 3을 입력하면 토끼 출력
    elif n == 3:
        print("토끼")
        print_rabbit()
    # 잘못된 입력 처리
    else:
        print("잘못입력")
    
    print()  # 각 출력 후 공백 한 줄 추가
