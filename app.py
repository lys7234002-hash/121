import random

def guess_number_game():
    # 随机生成 1~100 的整数
    secret_number = random.randint(1, 100)
    guess_count = 0

    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个 1~100 之间的整数。")
    print("输入数字进行猜测，输入 q 或 quit 可以中途退出。")

    while True:
        user_input = input("请输入你的猜测：").strip()

        # 允许用户中途退出
        if user_input.lower() in ('q', 'quit', 'exit'):
            print(f"游戏结束。正确答案是 {secret_number}。")
            break

        # 处理非数字输入
        try:
            guess = int(user_input)
        except ValueError:
            print("输入无效，请输入一个整数（或输入 q 退出）！")
            continue

        # 判断范围（可选但推荐）
        if guess < 1 or guess > 100:
            print("请输入 1~100 之间的整数！")
            continue

        guess_count += 1

        if guess > secret_number:
            print("大了！")
        elif guess < secret_number:
            print("小了！")
        else:
            print(f"恭喜你猜对了！答案就是 {secret_number}。")
            print(f"你一共猜了 {guess_count} 次。")
            break

if __name__ == "__main__":
    guess_number_game()