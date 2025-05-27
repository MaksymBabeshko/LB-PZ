import hashlib
from datetime import datetime

# Базовий клас користувача
class User:
    def __init__(self, username, password, is_active=True):
        self.username = username
        self.password_hash = self.hash_password(password)
        self.is_active = is_active

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        return self.password_hash == self.hash_password(password)

# Адміністратор з додатковими правами
class Administrator(User):
    def __init__(self, username, password, permissions=None):
        super().__init__(username, password)
        self.permissions = permissions if permissions else []

    def add_permission(self, permission):
        if permission not in self.permissions:
            self.permissions.append(permission)

# Звичайний користувач з останньою датою входу
class RegularUser(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.last_login = None

    def update_login_date(self):
        self.last_login = datetime.now()

# Гість із обмеженим доступом
class GuestUser(User):
    def __init__(self, username):
        super().__init__(username, password="", is_active=False)
        self.limited_access = True

# Клас контролю доступу
class AccessControl:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user.verify_password(password) and user.is_active:
            if isinstance(user, RegularUser):
                user.update_login_date()
            return user
        return None

# === Приклад використання ===
if __name__ == "__main__":
    access = AccessControl()

    admin = Administrator("admin", "admin456", permissions=["manage_users", "view_logs"])
    user = RegularUser("Maks_babesh", "password456")
    guest = GuestUser("guest")

    access.add_user(admin)
    access.add_user(user)
    access.add_user(guest)

    # Спроба входу
    auth_user = access.authenticate_user("Maks_babesh", "password456")
    if auth_user:
        print(f"Успішний вхід: {auth_user.username}")
        if isinstance(auth_user, RegularUser):
            print("Останній вхід:", auth_user.last_login)
    else:
        print("Помилкові облікові дані або неактивний акаунт.")
