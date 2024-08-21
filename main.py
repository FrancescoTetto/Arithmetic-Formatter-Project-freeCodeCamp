def arithmetic_arranger(problems, show_answers=False):
    #Will display a message because the program si made for a resonable number of arithmetic problems
    if len(problems) > 5:
        return 'Error: Too many problems.'    
    
    first_operands = []
    operators = []
    second_operands = []
    answers = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid problem format.'
        
        operand1, operator, operand2 = parts

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        

        if operator == "+":
            answer = str(int(operand1) + int(operand2))
        else:
            answer = str(int(operand1) - int(operand2)) 

        first_operands.append(operand1)
        operators.append(operator)
        second_operands.append(operand2)
        answers.append(answer)
    
    line1 = line2 = line3 = line4 = ""

    for i in range(len(problems)):
        width = max(len(first_operands[i]), len(second_operands[i])) + 2
        line1 += first_operands[i].rjust(width) + "    "
        line2 += operators[i] + " " + second_operands[i].rjust(width - 2) + "    "
        line3 += "-" * width + "    "
        if show_answers:
            line4 += answers[i].rjust(width) + "    "
    
    # Combine the lines
    arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()
    if show_answers:
        arranged_problems += "\n" + line4.rstrip()
    
    return arranged_problems

    

        
        
    

    

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')

case3 = arithmetic_arranger(["3 + 855", "988 + 40"], True)
print(case3)
case4 = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)
print(case4)
