# String functions

def method1(str) :
    a = False
    b = False
    c = False
    d = False
    e = False

    for s in str:
        if s.isalnum():
            a = True
        if s.isalpha():
            b = True
        if s.isdigit():
            c = True
        if s.isupper():
            d = True
        if s.islower():
            e = True

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


def method2(str):
    for check in ['isalnum', 'isalpha', 'isdigit', 'isupper', 'islower']:
        print(any({getattr(s, check) for s in str}))




if __name__ == '__main__':
    str = input()

    method2(str)



