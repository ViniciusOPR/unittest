 #https://docs.python.org/pt-br/3/library/doctest.html
 #https://docs.python.org/pt-br/3/library/unittest.html

from calculator import soma
try:
   print(soma('15', 15))
except AssertionError as e:
    print(f'Conta Inválida: {e}')

print('conta', soma(50, 50))