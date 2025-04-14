from rich.console import Console

console = Console()

def print_duck():
    duck = [
        " _",
        "<(o )",
        " (  >)"
    ]
    for line in duck:
        console.print(line, style="yellow")

def print_bear():
    bear = [
        " ʕ•ᴥ•ʔ ",
        " /  つ つ "
    ]
    for line in bear:
        console.print(line, style="white")

def print_rabbit():
    rabbit = [
        " (\\(\\ ",
        " ( -.-)",
        " o_( )( )"
    ]
    for line in rabbit:
        console.print(line, style="magenta")

# UI 출력
console.print("[bold cyan]그림 출력 프로그램[/bold cyan]")
console.print("[bold blue]=====================[/bold blue]")
console.print("[green]1. 오리[/green]")
console.print("[green]2. 곰[/green]")
console.print("[green]3. 토끼[/green]")
console.print("[red]0. 종료[/red]")
console.print("[bold blue]=====================[/bold blue]")

# 무한 반복
while True:
    try:
        n = int(input("선택: "))
    except ValueError:
        console.print("[red]숫자를 입력해주세요.[/red]")
        continue

    if n == 0:
        console.print("[bold red]프로그램을 종료합니다.[/bold red]")
        break
    elif n == 1:
        console.print("[bold yellow]오리[/bold yellow]")
        print_duck()
    elif n == 2:
        console.print("[bold white]곰[/bold white]")
        print_bear()
    elif n == 3:
        console.print("[bold magenta]토끼[/bold magenta]")
        print_rabbit()
    else:
        console.print("[red]잘못입력[/red]")

    console.print()  # 출력 후 빈 줄
