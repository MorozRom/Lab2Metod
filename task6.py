def calculate(a, b, op):
    """Выполняет арифметическую операцию op над числами a и b."""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b
    elif op == "**":
        return a ** b
    else:
        raise ValueError(f"Неизвестная операция: {op}")
