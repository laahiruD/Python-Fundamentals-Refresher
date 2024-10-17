try:
  print(x)
except:
  print('This is an Error')

#This will catch only NameError
try:
  print(T)
except NameError:
  print('Name Error means something is probably undefined.')

R = 2
try:
  print(R/0)
except NameError:
  print('Name Error means something is probably  not defined.')
except ZeroDivisionError:
  print('Do not devide by zero.')


P = 2
try:
  print(P/1)
except NameError:
  print('Name Error means something is probably  not defined.')
except ZeroDivisionError:
  print('Do not devide by zero.')
else:
  print('No Errors')


#Finally will execute with or without an error.
S = 2
try:
  print(S/0)
except NameError:
  print('Name Error means something is probably  not defined.')
except ZeroDivisionError:
  print('Do not devide by zero.')
else:
  print('No Errors')
finally:
  print('This will be print with or without an error.')

W = 2
try:
  if type(W) is not str:
    raise TypeError('This message is not mandatory!')
except NameError:
  print('Name Error means something is probably  not defined.')
except ZeroDivisionError:
  print('Do not devide by zero.')
except Exception as error:
  print(error)
else:
  print('No Errors')
finally:
  print('This will be print with or without an error.')


#Custom Exception with a class
class CustomException(Exception):
  pass

N = 2
try:
  raise CustomException('This is a custom exception')
except NameError:
  print('Name Error means something is probably  not defined.')
except ZeroDivisionError:
  print('Do not devide by zero.')
except Exception as error:
  print(error)
else:
  print('No Errors')
finally:
  print('This will be print with or without an error.')

