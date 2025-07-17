def validate_password(password):
    symbols = ['#', '@', '!', '?', '-', '_']

    num_of_lower = 0
    num_of_upper = 0
    num_of_symbols = 0
    num_of_numbers = 0

    # パスワードの長さを判定する
    if not (8 <= len(password) <= 16):
        print("パスワードの長さは8文字以上16文字以下です")
        return False

    # パスワードに含まれる文字の種類を判定する
    for c in password:
        if c.islower():
            num_of_lower += 1
        elif c.isupper():
            num_of_upper += 1
        elif c in symbols:
            num_of_symbols += 1
        elif c.isdigit():
            num_of_numbers += 1
        else:
            print("パスワードに使用できない文字が含まれています")
            return False

    # パスワードに各種文字が含まれているかを判定する
    if num_of_lower == 0:
        print("パスワードには小文字が含まれている必要があります")
        return False
    elif num_of_upper == 0:
        print("パスワードには大文字が含まれている必要があります")
        return False
    elif num_of_symbols == 0:
        print("パスワードには記号が含まれている必要があります")
        return False
    elif num_of_numbers == 0:
        print("パスワードには数字が含まれている必要があります。")
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
