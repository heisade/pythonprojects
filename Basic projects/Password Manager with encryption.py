from cryptography.fernet import Fernet

# To create File to store details
with open("stored passwords.txt", "w") as file:
    pass

class User:
    def __init__(self):
        self.user_details = []

    def load_details(self):
        if not detail in self.user_details:
            print("Details not found!")
        else:
            for detail in self.user_details:
                print(f"Platform: {detail['Platform']}\n"
                      f"Username: {detail['Username']}\n"
                      f"Password: {detail['Password']}")


    def add_details(self, username, password, platform):
        self.username = username
        self.password = password
        self.platform = platform
        self.user_details.append({'Username': {self.username}, 'Password': {self.password}, 'Platform': {self.platform}})
        with open("stored passwords.txt", "w") as file:
            file.write(str({'Username': self.username, 'Password': self.password, 'Platform': self.platform}))
        print("Details Successfully Added!")
