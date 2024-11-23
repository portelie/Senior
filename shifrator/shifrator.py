class InteractiveCipher:
    def __init__(self, shift=3):
        self.shift = shift  # Кількість зміщень для шифрування

    def encrypt(self, text):
        encrypted_text = ""
        for char in text:
            if char.isalpha():  # Якщо це літера
                shift_base = ord('А') if char.isupper() else ord('а')  # Визначаємо алфавіт
                new_char = chr((ord(char) - shift_base + self.shift) % 32 + shift_base)
                encrypted_text += new_char
            else:
                encrypted_text += char  # Неалфавітні символи залишаються без змін
        return encrypted_text

    def start(self):
        print("🔐 Ну що ти збираєшся ховати?) 🔐")
        print(f"Ти заїбешся на {self.shift} години.")
        while True:
            message = input("\nВведи повідомлення для шифрування (або 'вихід' для завершення): ")
            if message.lower() == "вихід":
                print("👋 Я тебе задоксив, хахахахаахха")
                break
            encrypted = self.encrypt(message)
            print(f"🔒 Зашифроване повідомлення: {encrypted}")


# Створюємо об'єкт шифратора і запускаємо його
cipher = InteractiveCipher(shift=5)
cipher.start()
