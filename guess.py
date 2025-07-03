import random
import os
import datetime

def load_highscore():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            return int(file.read())
    return None

def save_highscore(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

def show_history():
    print("\n📜 Lịch sử chơi gần đây:")
    if not os.path.exists("log.txt"):
        print("📂 Chưa có lịch sử chơi.")
    else:
        with open("log.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                print("📂 Lịch sử trống.")
            else:
                for line in lines[-5:]:
                    print("•", line.strip())

def play_game():
    secret = random.randint(1, 100)
    guess = None
    attempts = 0
    max_attempts = 7

    print("\n🎯 Tôi đã chọn một số từ 1 đến 100.")
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
                    print("🏆 Chúc mừng! Bạn lập kỷ lục mới!")
                    save_highscore(attempts)
                else:
                    print(f"📈 Kỷ lục hiện tại: {highscore} lượt.")
                break

        except ValueError:
            print("⚠️ Vui lòng nhập một số hợp lệ!")

    if guess != secret:
        print("💥 Bạn đã hết lượt đoán. Trò chơi kết thúc!")
        print(f"📌 Số đúng là: {secret}")

    # 📜 Ghi lịch sử chơi
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if guess == secret:
        result = f"[{timestamp}] ✅ Thắng sau {attempts} lượt.\n"
    else:
        result = f"[{timestamp}] ❌ Thua – số đúng là {secret}.\n"

    with open("log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(result)

# 📜 Hiển thị lịch sử trước khi bắt đầu chơi
show_history()

# 🔁 Vòng lặp chơi lại
while True:
    play_game()
    again = input("\n🔁 Bạn có muốn chơi lại không? (y/n): ").strip().lower()
    if again != 'y':
        print("👋 Cảm ơn bạn đã chơi! Hẹn gặp lại.")
        break