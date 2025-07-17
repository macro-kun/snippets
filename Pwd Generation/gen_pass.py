import string
import random


def generate_password(length, symbols, lower, upper, digit):
    chars = []
    chars += symbols
    if lower is True:
        chars += list(string.ascii_lowercase)
    if upper is True:
        chars += list(string.ascii_uppercase)
    if digit is True:
        chars += list(string.digits)

    passwd = ""

    for _ in range(length):
        passwd += random.choice(chars)

    return passwd


if __name__ == '__main__':
    length = int(input("パスワードの長さ: "))
    symbols = list(input("使用する記号をスペースなしで入力してください: "))
    if input('英小文字を使用しますか？YまたはN: ') == 'N':
        lower = False
    else:
        lower = True
    if input('英大文字を使用しますか？YまたはN: ') == 'N':
        upper = False
    else:
        upper = True
    if input('数字を使用しますか？YまたはN: ') == 'N':
        digit = False
    else:
        digit = True

    passwd = generate_password(length, symbols, lower, upper, digit)

    print(f"生成されたパスワード: {passwd}")


generate_password(6, ['!', '@', '#', '%', '&', '-', '_'], True, True, True)
generate_password(8, [], True, False, True)
generate_password(10, [], True, True, False)
generate_password(12, ['!', '?', '-', '_'], True, True, True)
