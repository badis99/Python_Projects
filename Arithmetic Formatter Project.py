def arithmetic_arranger(problems, show_answers=False):
    k = 0
    if len(problems) > 5:
        problems = 'Error: Too many problems.'
        k = 1
    else :
        number1 = [string[:string.find(' ')].strip(' ') for string in problems]
        number2 = [string[string.find(' ') + 3:].strip(' ') for string in problems]
        before_solutions = []
        solutions = []
        for i in range(len(number1)):
            if not (number1[i].isdigit() and number2[i].isdigit()):
                problems = 'Error: Numbers must only contain digits.'
                k = 1
                break
            elif len(number1[i]) > 4 or len(number2[i]) > 4:
                problems = 'Error: Numbers cannot be more than four digits.'
                k = 1
                break
        if k == 0:
            for i in range(len(problems)):
                operation=problems[i][problems[i].find(' ') + 1]
                solution = ""
                if operation != '+' and operation != '-':
                    k = 1
                    problems = "Error: Operator must be '+' or '-'."
                    break
                else:
                    before_solution = "--"
                    if operation == '+':
                        solution = str(int(number1[i]) + int(number2[i]))
                    elif operation == '-':
                        solution = str(int(number1[i]) - int(number2[i]))
                    if len(number1[i]) > len(number2[i]):
                        for j in range(len(number1[i]) - len(number2[i])):
                            number2[i] = ' ' + number2[i]
                    elif len(number2[i]) > len(number1[i]):
                        for j in range(len(number2[i]) - len(number1[i])):
                            number1[i] = ' ' + number1[i]
                    for j in range(max(len(number1[i]),len(number2[i]))):
                        before_solution += '-'
                    for j in range(len(before_solution) - len(solution)):
                        solution = ' ' + solution
                    number1[i] = '  ' + number1[i]
                    number2[i] = operation + ' ' + number2[i]
                    before_solutions.append(before_solution)
                    solutions.append(solution)
        if k == 0:
            problems = '    '.join(number1) + '\n' + '    '.join(number2) + '\n' + '    '.join(before_solutions)
            if show_answers == True:
                problems += '\n' + '    '.join(solutions)
    return problems

print(f'{arithmetic_arranger(["24 + 8515", "3801 - 2", "45 + 43", "123 + 49"])}')