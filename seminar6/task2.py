# 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,. приоритет операций стандартный.
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;

def ConvertRPN(inputSequence: list) -> list:
    operatorsPriority = {'+': 1, '-': 1, '/': 2, '*': 2}
    outputSequence = []
    stack = []
    for token in inputSequence:
        if token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                outputSequence.append(stack.pop())
            stack.pop()
        elif token in operatorsPriority.keys():
            while len(stack) > 0 and stack[-1] in operatorsPriority.keys():
                if operatorsPriority[stack[-1]] >= operatorsPriority[token]:
                    outputSequence.append(stack.pop())
                else:
                    break
            stack.append(token)
        else:
            outputSequence.append(token)

    while len(stack) > 0:
        outputSequence.append(stack.pop())

    return outputSequence


def CalcRPN(rpnSequence: list) -> float:
    operators = {'+': lambda a, b: a + b,
                 '-': lambda a, b: a - b,
                 '/': lambda a, b: a / b,
                 '*': lambda a, b: a * b}
    stack = []
    for token in rpnSequence:
        if token in operators.keys():
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operators[token](operand1, operand2))
        else:
            stack.append(float(token))
    return stack[0]

def Calculator(eval: str):
    operators = {'+', '-', '/', '*', '(', ')'}
    for o in operators:
        eval = eval.replace(o, f' {o} ')
    tokens = eval.split()
    rpn = ConvertRPN(tokens)
    return CalcRPN(rpn)


test0 = "(1+2)*4+3"
test1 = "1+2*3"
test2 = "(1+2)*3"
test3 = "1-2*3"
test4 = "(8*(6+3)/(12-9.8))*3.5"
test5 = "(1+2+1)*3"
print(f"{test0} = {Calculator(test0)}; eval = {eval(test0)}")
print(f"{test1} = {Calculator(test1)}; eval = {eval(test1)}")
print(f"{test2} = {Calculator(test2)}; eval = {eval(test2)}")
print(f"{test3} = {Calculator(test3)}; eval = {eval(test3)}")
print(f"{test4} = {Calculator(test4)}; eval = {eval(test4)}")
print(f"{test5} = {Calculator(test5)}; eval = {eval(test5)}")
