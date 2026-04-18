class User:
    user_count = 0
    __default_password = "12345678"
    def __init__(self, username, phone_number, password = __default_password):
        self.username = username
        self.role = "user"
        # self.password = User.default_password
        self.password = password
        self.phone_number = phone_number
        User.user_count += 1
    @classmethod
    def create_admin(cls, username, phone_number, password):
        new_user = User(username, phone_number, password)
        new_user.role = "admin"
        return new_user
    @classmethod
    def get_user_count(cls):
        return cls.user_count
    @staticmethod
    def validate_password(password):
        return len(password) >= 8
    def change_password(self, password):
        if User.validate_password(password):
            self.password = password
        else:
            raise ValueError("Password must be at least 8 characters long.") #запустить ошибку



print(f"{User.user_count} users created")
user_1 = User("WalicFeed", "+79107939695", "Aboba_1")
print(f"{User.user_count} users created")
print(f"user1 password is {user_1.password}")
admin_1 = User.create_admin("Razan", "+6666666666", "NO")
print(f"{admin_1.username}'s role is {admin_1.role}")
print(User.get_user_count())
# user_1.change_password("1234") ошибка
