from ft_calculator import calculator

a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a,b)
calculator.add_vec(a,b)
calculator.sous_vec(a,b)

calculator_obj:calculator = calculator()

print(calculator_obj.__doc__)
print(calculator_obj.dotproduct.__doc__)
print(calculator_obj.add_vec.__doc__)
print(calculator_obj.sous_vec.__doc__)
