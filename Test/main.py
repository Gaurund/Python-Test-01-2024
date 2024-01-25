import argparse
import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)
handler_error = logging.FileHandler("error.log", encoding="utf-8")
handler_error.setLevel(logging.NOTSET)
logger.addHandler(handler_error)

parser = argparse.ArgumentParser(prog='Triangle',
                                 description='Приложение принимает три целых числа и проверяет можно ли из отрезков '
                                             'такой длинны составить треугольник.')
parser.add_argument('numbers', metavar='N', type=str, nargs='*', help='Введите три целых числа.')
args = parser.parse_args()


def triangle(*nums):
    a, b, c = nums
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


def check_amount(vals):
    if len(vals) > 3:
        logger.critical("Слишком много параметров. Чисел должно быть три. Но мы удалим лишние за вас.")
        return vals[:3:]
    elif len(vals) < 3:
        logger.critical("Недостаточно параметров. Чисел должно быть три.")
        return 0, 0, 0
    return vals


def convert_list_to_int(str_list):
    num_list = list()
    for e in str_list:
        try:
            num_list.append(int(e))
        except Exception:
            logger.critical("Следует вводить только целые числа!")

    return num_list


if __name__ == '__main__':
    values = convert_list_to_int(args.numbers)
    values = check_amount(values)
    triangle(*values)
