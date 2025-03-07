f = open('test.csv', 'w')
print(f.write('abc'))
print(f.write('123456'))
f.close()

with open('test.csv') as f:
    print(f.readlines())



