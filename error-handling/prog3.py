'''
discuss these additional blocks of the exception handling code
'''
def func1():
    try:
        f = open('test.txt', 'r')
    except Exception as e:
        print(e)
    else:
        print("we are in else block")

def func2():
    try:
        f = open('test.txt', 'w')
    except Exception as e:
        print(e)
    else:
        print("we are in else block")

func1()
func2()
