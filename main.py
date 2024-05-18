class Password:
    def proverka(self):
        while True:
            password = input("Введите пароль: ")
            if len(password) < 8 or len(password) > 20:
                print("Ошибка! Длина пароля должна быть от 8 до 20 символов")
                continue
            if not any(char.isdigit() for char in password):
                print("Ошибка! Пароль должен содержать хотя бы одну цифру")
                continue
            if not any(char.isupper() for char in password):
                print("Ошибка! Пароль должен содержать хотя бы одну заглавную букву")
                continue
            if not any(char.islower() for char in password):
                print("Ошибка! Пароль должен содержать хотя бы одну строчную букву")
                continue
            if not any(not char.isalnum() for char in password):
                print("Ошибка! Пароль должен содержать хотя бы один специальный символ")
                continue
            print("Пароль верный")
            break

password = Password()
password.proverka()