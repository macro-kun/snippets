import os
from cryptography.fernet import Fernet


def generate_key():
    if os.path.exists('key_file.key'):
        return
    else:
        key = Fernet.generate_key()
        with open('key_file.key', 'wb') as key_file:
            key_file.write(key)


def get_key():
    with open('key_file.key', 'rb') as key_file:
        key = key_file.read()
    return key


def encrypt_file(filename):
    key = get_key()
    fernet = Fernet(key)

    with open(filename, 'rb') as original_file:
        original = original_file.read()

    encrypted = fernet.encrypt(original)

    with open('encrypted_' + filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt_file(filename):
    key = get_key()
    fernet = Fernet(key)

    with open('encrypted_' + filename, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open('decrypted_' + filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)


if __name__ == '__main__':
    generate_key()
    print("暗号化を行いますか？復号しますか？")
    operation = int(input("暗号化の場合は 1、復号の場合は 2 を入力してください: "))

    if operation == 1:
        filename = input("暗号化するファイル: ")
        encrypt_file(filename)
        print(f"暗号化が完了しました。ファイル名は {'encrypted_' + filename} です。")
    elif operation == 2:
        filename = input("復号するファイル: ")
        decrypt_file(filename)
        print(f"ファイルの復号が完了しました。ファイル名は{'decrypted_' + filename}です。")
    else:
        print('1 または 2 を入力してください。')
