from PyPDF2 import PdfWriter, PdfReader
from getpass import getpass


def main():
    pdf_writer = PdfWriter()
    pdf = PdfReader('микросервисы.pdf')

    for page in range(len(pdf.pages)):
        pdf_writer.add_page(pdf.pages[page])

    password = getpass(prompt='Введите пароль: ')
    pdf_writer.encrypt(password)

    with open('protected.pdf', 'wb') as file:
        pdf_writer.write(file)


if __name__ == '__main__':
    main()
