#Function 3 : No parameter/Have Returns ***
def funcA( ):
    print('AAA')
    print('BBB')
    return 'Wow Wow Wow'
def funcB( ) :
    return 999, True, 10+85

# funcA( ) เขียนได้ แต่ไม่ทำกัน
print (funcA( ))
x = funcA()

a, b, c = funcB( ) #***
print(f'{a} {b} {c}')