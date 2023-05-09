def first_formula(x: float) -> float:
    upper_part = x + 5
    lower_part = 2 * (x + 1)
    y = upper_part / lower_part
    return second_formula(x, y)


def second_formula(x: float, y: float) -> float:
    upper_part = (y * y) + x * (x - (2 * y))
    lower_part = x * y
    return upper_part / lower_part


if __name__ == '__main__':
    s = input()

    print(first_formula(float(s)))
