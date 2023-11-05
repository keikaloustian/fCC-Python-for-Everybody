# When the asterisk or star symbol (*) is used immediately before a sequence, such as some_items, it unpacks the sequence into its individual components.

# string.isdigit() - returns True if string is made up of numeric digits only, False otherwise

# There are no increment ++ / decrement -- operators in Python.

# Multiple concatenation operator
# 'string' + 'a' * 5 -> stringaaaaa

def arithmetic_arranger(problems, answers=False):

  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''

  # Number of problems limit is 5
  if len(problems) > 5:
    return 'Error: Too many problems.'

  n = 0
  while n < len(problems):
    if n > 0:
      line1 += ' ' * 4
      line2 += ' ' * 4
      line3 += ' ' * 4
      line4 += ' ' * 4

    problem = problems[n]
    
    # Operator has to be + or -
    if '+' not in problem and '-' not in problem:
      return "Error: Operator must be '+' or '-'."

    operand1 = problem.split()[0]   
    operand2 = problem.split()[2]   
    operator = problem.split()[1]
    longest = max(len(operand1), len(operand2))
    
    # Operands must contain digits only
    if not operand1.isdigit() or not operand2.isdigit():
      return "Error: Numbers must only contain digits."

    # Operands must be 4 digits or less
    if len(operand1) > 4 or len(operand2) > 4:
      return "Error: Numbers cannot be more than four digits."

    # Assemble each line of result
    # Line 1
    line1 += '  '
    if len(operand1) < len(operand2):
      line1 += ' ' * (len(operand2) - len(operand1))
    line1 += operand1
    
    # Line 2
    line2 += operator + ' '
    if len(operand2) < len(operand1):
      line2 += ' ' * (len(operand1) - len(operand2))
    line2 += operand2
  
    # Line 3
    line3 += '--'
    i = 0
    while i < longest:
      line3 += '-'
      i += 1

    # Line 4
    if answers:
      if operator == '+':
        ans = int(operand1) + int(operand2)
      else: 
        ans = int(operand1) - int(operand2)

      dashes = longest + 2
      line4 += ' ' * (dashes - len(str(ans)))
      line4 += str(ans)   

    # Advance index of problems list
    n += 1
 
  # Assemble lines into final result
  arranged_problems = line1 + '\n' + line2 + '\n' + line3
  if answers:
    arranged_problems += '\n' + line4
    
  return arranged_problems