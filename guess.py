import random

secret = random.randint(1, 100)
guess = None
attempts = 0
max_attempts = 7

print("🎯 Chào mừng đến với trò chơi Đoán số!")
print("Tôi đã chọn một số từ 1 đến 100.")
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
            print(f"🎉 Chính xác! Bạn đã đoán đúng sau {attempts} lượt.")
            break

    except ValueError:
        print("⚠️ Vui lòng nhập một số hợp lệ!")

# Nếu hết lượt mà vẫn đoán sai
if guess != secret:
    print("💥 Bạn đã hết lượt đoán. Trò chơi kết thúc!")
    print(f"Số đúng là: {secret}")