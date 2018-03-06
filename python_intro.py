if 3 > 2:
    print('it works!')

name = 'karina'
if name == 'ola':
    print('hey ola')
elif name == 'karina':
    print('hey Karina')
else:
    print('hey everyone')

def hi():
    print('hi there')
    print('how are you')
hi()

def hello(name):
    if name == 'ola':
        print('hi ola')
    elif name == 'karina':
        print('hi Karina')
    else:
        print('Hi anonymous')
hello('karina')

def hola(name):
    print('hi ' + name + '!')
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hola(name)
print('next girl')

for i in range(1, 6):
    print(i)
