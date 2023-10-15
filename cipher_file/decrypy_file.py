import pyAesCrypt


""" Программа создана для дешифрования файлов """


def main():
    password = input('Введите пароль для файла: ')
    pyAesCrypt.decryptFile('just_test.txt.aes', 'result.txt', password)


if __name__ == '__main__':
    main()
