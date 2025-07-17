import re


def validate_password(password):
    lower = re.search('[a-z]', password)
    upper = re.search('[A-Z]', password)
    symbols = re.search('[#@!?-_]', password)
    numbers = re.search('[0-9]', password)

    if not (8 <= len(password) <= 16):
        print("パスワードの長さは8文字以上16文字以下です")
        return False

    if len(password) != len(re.findall(r'[a-zA-Z#@!?_\-0-9]', password)):
        print("パスワードに使用できない文字が含まれています")
        return False

    if lower is None:
        print("パスワードには小文字が含まれている必要があります")
        return False
    elif upper is None:
        print("パスワードには大文字が含まれている必要があります")
        return False
    elif symbols is None:
        print("パスワードには記号が含まれている必要があります")
        return False
    elif numbers is None:
        print("パスワードには数字が含まれている必要があります")
        return False
    else:
        print("パスワード OK")
        return True


if __name__ == '__main__':
    print("パスワードを入力してください。")
    print("パスワードの条件:")
    print("長さは8文字以上16文字以下で、使用できる文字は英数記号のみです。")
    print("また、小文字、大文字、数字、記号それぞれが少なくとも1つ含まれている必要があります。")
    print("使用できる記号は、#, !, @, ?, %, -, _ です。")

    password = input("パスワード:")
    result = validate_password(password)

    if result is False:
        print("パスワードの検証に失敗しました")
    else:
        print("パスワードの検証に成功しました")
