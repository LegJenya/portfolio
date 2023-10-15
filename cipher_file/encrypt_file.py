import pyAesCrypt


""" Программа создана для шифрования файлов с текстом симметричным алгоритмом блочного шифрования AES """


def main():
    password = input('Введите пароль для шифрования файла: ')
    pyAesCrypt.encryptFile('just_test.txt', 'just_test.txt.aes', password)


if __name__ == '__main__':
    main()
