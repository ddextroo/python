def calculator(**evaluations):
    return eval(f"{evaluations.get('first_number')} {evaluations.get('operator')} {evaluations.get('second_number')}")

print(calculator(first_number = 5, operator = '*', second_number = 2))