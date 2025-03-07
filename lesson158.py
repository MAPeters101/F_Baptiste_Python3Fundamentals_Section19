f = open('test.csv', 'w')
print(f.write('abc'))
print(f.write('123456'))
f.close()

with open('test.csv') as f:
    print(f.readlines())
print()


with open('test.csv', 'w') as f:
    f.write('abc\n')
    f.write('123456\n')

with open('test.csv') as f:
    print(f.readlines())
