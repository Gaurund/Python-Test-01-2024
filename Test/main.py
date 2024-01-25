import argparse
import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)
handler_error = logging.FileHandler("error.log", encoding="utf-8")
handler_error.setLevel(logging.NOTSET)
logger.addHandler(handler_error)

parser = argparse.ArgumentParser(prog='Triangle',
                                 description='Validate ability of the lines to render a triangle ',
                                 epilog='Returns a notification')
parser.add_argument('numbers', metavar='N', type=str, nargs='*', help='type in some numbers')
args = parser.parse_args()


def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Треугольник существует", end=" ")
        if a == b == c:
            print("и он равносторонний")
        elif a == b or a == c or b == c:
            print("и он равнобедренный")
        else:
            print("и он разносторонний")
    else:
        print("Треугольник не существует")


def check_amount():
    try:
        a, b, c = args.numbers
    except Exception as e:
        # logger.critical(e)
        if len(args.numbers) > 2:
            logger.critical("Слишком много параметров. Чисел должно быть три.")
        else:
            logger.critical("Недостаточно параметров. Чисел должно быть три.")
        a = b = c = 0
    return a, b, c


values = check_amount()

triangle(x, y, z)
