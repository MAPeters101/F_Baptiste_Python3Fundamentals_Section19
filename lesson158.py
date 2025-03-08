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
print('-'*80)


data = ['line 1', 'line 2', 'line 3']
with open('test.csv', 'w') as f:
    f.writelines(data)

with open('test.csv') as f:
    print(f.readlines())
print()

data = ['line 1\n', 'line 2\n', 'line 3\n']
with open('test.csv', 'w') as f:
    f.writelines(data)

with open('test.csv') as f:
    print(f.readlines())
print()


data = ['line 1', 'line 2', 'line 3']
with open('test.csv', 'w') as f:
    f.write('\n'.join(data))

with open('test.csv') as f:
    print(f.readlines())
print('-'*80)

# with open('test.csv', 'r') as file:
#     raise ValueError('bogus')
# print(file.closed)

with open('test.csv') as f:
    for line in f:
        print(line, end='')
print()
print()
with open('test.csv', 'a') as f:
    f.write('line4\n')
    f.write('line5\n')
with open('test.csv') as f:
    for line in f:
        print(line.strip())

print('-'*80)

with open('open_not_exists.txt', 'a') as f:
    f.write('Line 1')
with open('open_not_exists.txt',) as f:
    print(f.readlines())
print('='*80)




