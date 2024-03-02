'''
Assertion
'''

def division(x,y):
  assert y!=0
  
  print(x/y)
  
#call division() function in try block
try:
  division(10,0)
except AssertionError as msg:
  print(msg)