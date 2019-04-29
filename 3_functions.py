def func1(name, midname, sername):
    print(name, midname, sername)

# positional parameter passing
print('-'*6, ' positional parameter passing')
func1('Dima', 'Dimich', 'Dimov')

# keyword argument passing.
print('-'*6, ' keyword argument passing')
func1(name='Dima', midname='Dimich', sername='Dimov')
func1(sername='Dimov', name='Dima', midname='Dimich')

# mixed way of argument passing.
print('-'*6, ' mixed way of argument passing.')
func1('Dima', sername='Dimov', midname='Dimich')

# mixed way of argument passing.
print('-'*6, ' default value for parametr')
def func2(name, midname, sername='Dimov'):
    print(name, midname, sername)
func2('Dima', 'Dimich', 'Dimov')
func2('Dima', 'Dimich')

# if a function doesn’t return a certain value using a return expression clause, it is assumed that it implicitly returns None.
print('-'*6, ' return value')
def strange(n):
    if (n%2 == 0):
        return True
print(strange(2))
print(strange(1))






