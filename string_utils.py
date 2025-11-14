def split_before_each_uppercases(formula):
    pass # Replace the `pass` with your code


def split_at_first_digit(formula):
  for i in range (len(formula)):
    if formula[i].isdigit():
      return formula [:i], int(formula [i:])    
  return formula, 1   
