# Things To try and do: 
# 1. Make sure it creates a file where it stores all the details(encrypted version)
# Details to store there: Platorm, username and password
# It should be able to create a file to save the details there.

# 2. Will be using AES(Advanced Encryption Standard) from the cryptography Library, which
# i will be doing some research on.

# 3. Noticed some installations needed so i'll be creating a requirements.txt file for the project.
# [Make sure to install everything in the requirements.txt file before running the code]

# 4. I will be using the Fernet module from the cryptography library to encrypt and decrypt the passwords.
# I will be using the Fernet module to encrypt and decrypt the passwords. The Fernet module is a symmetric encryption method, meaning that the same key is used for both encryption and decryption.




from cryptography.fernet import Fernet      # This will be used to encrypt and decrypt the passwords
import os                                   # This will be used to check if the file [for storing the key and storing user details] exists or not


class SecurePasswordManager:
    user_details = []
    key_file = "key.txt"                    # This is the file that will be used to store the key
    data_file = "Details Manager.txt"       # This is the file that will be used to store the details
    key = None                              # This is the variable that will be used to store the key
    f = None                                # This is the variable that will be used to encrypt and decrypt the passwords


    # This will create a file to store the key if it does not exist
    # This will also create a file to store the details if it does not exist

    @classmethod
    def load_key(cls):
        if os.path.exists(cls.key_file):
            with open(cls.key_file, "rb") as file:
                key = file.read()
        else:
            key = Fernet.generate_key()
            with open(cls.key_file, "wb") as file:
                file.write(key)                                     # Kept on adding texts here not knowing it was going to cause errors because it's writing the text into a binary file.
        return key
    
    # This will load the key from the file or generate a new one if it does not exist
    # This will also create a Fernet object using the key
    @classmethod
    def init_key(cls):
        cls.key = cls.load_key()
        cls.f = Fernet(cls.key)



    # Add details to get details and store them in the variable User_details
    # The details will be encrypted and stored in the user_details list
    # The details will also be stored in the data_file
    # The details will be stored in the data_file in the format: Platform, Username, Password
    def add_details(self, platform, username, password):
        encoded_platform = SecurePasswordManager.f.encrypt(bytes(platform, 'utf-8')).decode()
        encoded_username = SecurePasswordManager.f.encrypt(bytes(username, 'utf-8')).decode()
        encoded_password = SecurePasswordManager.f.encrypt(bytes(password, 'utf-8')).decode()
        SecurePasswordManager.user_details.append({'Platform': encoded_platform, 'Username': encoded_username, 'Password': encoded_password})
        print("Details have been successfully added")
        with open(SecurePasswordManager.data_file, "a") as file:
            file.write(f'{encoded_platform},{encoded_username},{encoded_password}\n')



    # This will delete the details from the data_file and the user_details list and update the details from the data_file
    # The details will be deleted from the data_file in the format: Platform, Username, Password and update the details from the data_file
    # The details will be deleted from the user_details list in the format: Platform, Username, Password and update the details from the data_file
    def edit_details(self, old_platform, old_username, old_password, new_platform, new_username, new_password):
        found = False
        updated_details = []
        try:
            with open(SecurePasswordManager.data_file, "r") as file:
                for line in file:
                    encoded_platform, encoded_username, encoded_password = line.strip().split(",")
                    platform = SecurePasswordManager.f.decrypt(encoded_platform.encode()).decode()
                    username = SecurePasswordManager.f.decrypt(encoded_username.encode()).decode()
                    password = SecurePasswordManager.f.decrypt(encoded_password.encode()).decode()
                     
                    if platform == old_platform and username == old_username and password == old_password:
                        encoded_platform = SecurePasswordManager.f.encrypt(bytes(new_platform, 'utf-8')).decode()
                        encoded_username = SecurePasswordManager.f.encrypt(bytes(new_username, 'utf-8')).decode()
                        encoded_password = SecurePasswordManager.f.encrypt(bytes(new_password, 'utf-8')).decode()
                        updated_details.append(f"{encoded_platform},"
                                               f"{encoded_username},"
                                               f"{encoded_password}\n")
                        found = True
                    else:
                        updated_details.append(line)
                        
                if found:
                    with open (SecurePasswordManager.data_file, "w") as file:
                        file.writelines(updated_details)
                    print("Details Updated!")
                else:
                    print("Details not found. No changes made.")
        except FileNotFoundError:
            print("No stored details found!")


    # This will view the details from the data_file and the user_details list
    # The details will be viewed from the data_file in the format: Platform, Username, Password and update the details from the data_file
    def view_details(self):
        try:
            with open(SecurePasswordManager.data_file, "r") as file:
                for index, line in enumerate(file, start=1):
                    print('<>' *40)
                    encoded_platform, encoded_username, encoded_password = line.strip().split(",")
                    platform = SecurePasswordManager.f.decrypt(encoded_platform.encode()).decode()
                    username = SecurePasswordManager.f.decrypt(encoded_username.encode()).decode()
                    password = SecurePasswordManager.f.decrypt(encoded_password.encode()).decode()
                    print(f"{index}. Platform: {platform}\n"
                          f"   Username: {username}\n"
                          f"   Password: {password}")
        except FileNotFoundError:
            print("File not found!")

SecurePasswordManager.init_key()            # This will initialize the key and the fernet object
