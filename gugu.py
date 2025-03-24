# 사용자 입력 기반 구구단 프로그램
try:
    # 사용자로부터 단 입력받기
    dan = int(input("출력할 구구단의 단을 입력하세요: "))
    
    # 입력값 검증 (일반적으로 구구단은 1~9단까지 사용)
    if 1 <= dan <= 9:
        print(f"\n--- {dan}단 ---")
        for i in range(1, 10):
            print(f"{dan} x {i} = {dan*i}")
    else:
        print("1부터 9 사이의 숫자를 입력해주세요.")
        
except ValueError:
    print("유효한 숫자를 입력해주세요.")