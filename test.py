import time

def timer(*args: tuple):
    seconds = 0
    # for i in range(0, len(args)):
    #     # if type(args[i]) == float or type(args[i]) == int:
    #     #     seconds = type(args[i])
    #     #     print(args[i])
    #     #     time.sleep(seconds)
    #     #     break
    #     print(type(args[i]))
    for i in args:
        print(i, 'sth')


a = ('abcd')
b = (4)
c = ('')
d = ('sadsda')
e = (2.4)
f = ('awdawd')
timer(a, b, c, d, e)
