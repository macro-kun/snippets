# ユーザー名とパスワードを登録する関数
# 入力としてユーザー名とパスワードを受け取り、検証を行う
# ユーザー名に使用してよいのは、英数小文字のみ
# ユーザー名の長さは4文字から20文字
# パスワードに使用してよいのも英数小文字のみ
# パスワードの長さは6文字から12文字
# ユーザー名が一意であることを検証する
# 検証に合格したらjsonファイル users に保存する

import json
import os


def write_to_file(fileName, users, username, password):
    with open(fileName, 'w') as users_file:
        users[username] = password
        json.dump(users, users_file)
        print('ユーザー登録が完了しました')
        return True


def register_user(username, password):
    # ユーザー名が英数小文字であることを確認する
    if not (4 <= len(username) <= 20):
        print('ユーザー名の長さは4文字以上20文字以下です')
        return False
    if not username.islower():
        print('ユーザー名に使用できるのは英数小文字のみです')
        return False
    if not username.isalnum():
        print('ユーザー名に使用できるのは英数小文字のみです')
        return False
    # パスワードが6文字以上12文字以下であることを確認する
    if not (6 <= len(password) <= 12):
        print('パスワードの長さは6文字以上12文字以下です')
        return False
    # パスワードが英数小文字であることを確認する
    if not password.islower():
        print('パスワードに使用できるのは英数小文字のみです')
        return False
    if not password.isalnum():
        print('パスワードに使用できるのは英数小文字のみです')
        return False

    # ユーザー名が一意であることを検証する
    fileName = 'users.json'
    if os.path.isfile(fileName):
        with open('users.json', 'r+', encoding='utf-8') as users_file:
            users = json.loads(users_file.read())
            if username in users:
                print('そのユーザー名はすでに存在します')
                return False
            else:
                write_to_file(fileName, users, username, password)

    else:
        write_to_file(fileName, username, password)


if __name__ == '__main__':
    username = input('ユーザー名: ')
    password = input('パスワード: ')

    register_user(username, password)
