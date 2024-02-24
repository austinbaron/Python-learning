
try:
    f = open('test.txt', 'r')
except Exception as e:
    print(f'issue with the code {e}')