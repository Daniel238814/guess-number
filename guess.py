import random
import os

def load_highscore():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            return int(file.read())
    return None

def save_highscore(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

def play_game():
    secret = random.randint(1, 100)
    guess = None
    attempts = 0
    max_attempts = 7

    print("🎯 Tôi đã chọn một số từ 1 đến 100.")
    print(f"Bạn có {max_attempts} lượt để đoán đúng.")

    while guess != secret and attempts < max_attempts:
        try:
            guess = int(input(f"👉 Lượt {attempts + 1}: Nhập số bạn đoán: "))
            attempts += 1

            if guess < secret:
                print("🔼 Lớn hơn!")
            elif guess > secret:
                print("🔽 Nhỏ hơn!")
            else:
                print(f"🎉 Chính xác! Bạn đoán đúng sau {attempts} lượt.")

                highscore = load_highscore()
                if highscore is None or attempts < highscore:
                    print("🏆 Chúc mừng! Bạn vừa lập kỷ lục mới!")
                    save_highscore(attempts)
                else:
                    print(f"📈 Kỷ lục hiện tại: {highscore} lượt.")
                return

        except ValueError:
            print("⚠️ Vui lòng nhập một số hợp lệ!")

    if guess != secret:
        print("💥 Bạn đã hết lượt đoán. Trò chơi kết thúc!")
        print(f"📌 Số đúng là: {secret}")

# Bắt đầu vòng lặp chơi lại
while True:
    play_game()
    choice = input("\n🔁 Bạn có muốn chơi lại không? (y/n): ").strip().lower()
    if choice != 'y':
        print("👋 Cảm ơn bạn đã chơi! Hẹn gặp lại.")
        break