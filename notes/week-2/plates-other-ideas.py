def middle_check(m):
    for c in m[2:]:
        if c.isnumeric():
            a,b,d = m.partition(c)
            print(a,b,d)
            if b == '0':
                print('starts with a zero')
                return False
            elif d.isnumeric() == False:
                print('does not end in a num')
                return False
            else:
                print('you still fcucking suck')
                return True

print(middle_check('Walter360'))
print('-'*50)
print(middle_check('WA0254'))
print('-'*50)
print(middle_check('WA256WA'))

