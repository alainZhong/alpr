import random

def generate_question():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    print(f"{a} + {b} = ?")
    answer = int(input("请输入答案: "))
    if answer == a + b:
        print("✅ 正确！")
    else:
        print(f"❌ 错误，正确答案是 {a + b}")

if __name__ == "__main__":
    while True:
        generate_question()
        cont = input("继续吗？(y/n): ").lower()
        if cont != 'y':
            break