class User:
    count = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        User.count += 1

    def is_valid_email(email_address):
        return "@" in email_address

# user1 = User("강영훈", "younghoon@codeit.kr", "123456")

print(User.is_valid_email(""))