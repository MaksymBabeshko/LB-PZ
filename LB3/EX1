import sqlite3
import hashlib


class UserManager:
    def __init__(self, db_name='user.db'):
        self.db_name = db_name
        self._create_database()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def _create_database(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    login TEXT PRIMARY KEY,
                    password TEXT NOT NULL,
                    full_name TEXT
                )
            ''')
            conn.commit()
        print(f"Базу даних '{self.db_name}' та таблицю 'users' створено (або вони вже існують).")

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def add_user(self, login, password, full_name):
        hashed_password = self._hash_password(password)
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO users (login, password, full_name) VALUES (?, ?, ?)",
                    (login, hashed_password, full_name)
                )
                conn.commit()
            print(f"Користувача '{login}' успішно додано.")
        except sqlite3.IntegrityError:
            print(f"Помилка: Користувач з логіном '{login}' вже існує.")
        except Exception as e:
            print(f"Виникла помилка при додаванні користувача: {e}")

    def update_password(self, login, new_password):
        hashed_password = self._hash_password(new_password)
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE users SET password = ? WHERE login = ?",
                (hashed_password, login)
            )
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Пароль для користувача '{login}' успішно оновлено.")
            else:
                print(f"Помилка: Користувача з логіном '{login}' не знайдено.")

    def authenticate_user(self, login, password):
        hashed_password = self._hash_password(password)
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT password FROM users WHERE login = ?",
                (login,)
            )
            result = cursor.fetchone()

        if result:
            stored_password = result[0]
            if hashed_password == stored_password:
                print(f"Автентифікація для '{login}' успішна.")
                return True
            else:
                print(f"Невірний пароль для '{login}'.")
                return False
        else:
            print(f"Користувача з логіном '{login}' не знайдено.")
            return False


def main_menu():
    manager = UserManager()

    while True:
        print("\n--- Меню управління користувачами ---")
        print("1. Додати нового користувача")
        print("2. Оновити пароль користувача")
        print("3. Перевірити автентифікацію")
        print("4. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == '1':
            login = input("Введіть логін нового користувача: ")
            password = input("Введіть пароль: ")
            full_name = input("Введіть повне ПІБ: ")
            manager.add_user(login, password, full_name)
        elif choice == '2':
            login = input("Введіть логін користувача, чий пароль потрібно оновити: ")
            new_password = input("Введіть новий пароль: ")
            manager.update_password(login, new_password)
        elif choice == '3':
            login = input("Введіть логін для автентифікації: ")
            password = input("Введіть пароль: ")
            manager.authenticate_user(login, password)
        elif choice == '4':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main_menu()
