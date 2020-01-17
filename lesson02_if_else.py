print('Menu:')
print('Open:1')
print('Save:2')
print('Report:7')
print('Exit:0')
s = input('Input your choice:')

if s == '1':
    print('Open')
elif s == '2':
        print('Save')
elif s == '0':
    print('Goodby')
elif s == 7:
    print('Report')
else:
    print('Icorrect input')

if a < b :
    c = a
else:
    c = b

c = a if a < b else b
