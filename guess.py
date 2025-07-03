import random

secret = random.randint(1, 100)
guess = None

print("🎲 Chào mừng đến với trò chơi Đoán số!")
print("Tôi đã chọn một số từ 1 đến 100. Hãy đoán thử nhé!")

while guess != secret:
    try:
        guess = int(input("Nhập số bạn đoán: "))
        if guess < secret:
            print("👉 Lớn hơn!")
        elif guess > secret:
            print("👈 Nhỏ hơn!")
        else:
            print("🎉 Chính xác! Bạn đã đoán đúng!")
    except:
        print("⚠️ Vui lòng nhập một số hợp lệ!")