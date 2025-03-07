file_name = 'DEXUSEU.csv'

file = open(file_name, 'r')
print(file.name)
print(file.readable())
print(file.writable())
print(file.closed)
file.close()
print(file.closed)
f = open(file_name)
data = f.readlines()
f.close()
print(data)
print('-'*80)


f = open(file_name)
for line in f:
    print(line)
print('- '*20)

f = open(file_name)
for line in f:
    print(line, end='')
print('. '*20)
for line in f:
    print(line, end='')
f.close()
print()

f = open(file_name)
print(next(f))
print(next(f))
print(next(f))
f.close()
print()


# f = open(file_name)
# try:
#     for row in f:
#         print(row)
#         raise ValueError('forcing an exception...')
# finally:
#     print('closing file...')
#     f.close()
#     print(f.closed)


with open(file_name) as f:
    print(f.closed)
print(f.closed)
print('='*80)


with open(file_name) as f:
    for line in f:
        print(line)

with open(file_name) as f:
    print(f.readlines())
print('='*80)


with open(file_name) as f:
    headers = next(f)

    for row in f:
        row = row.strip()
        date, value_str = row.split(',')

        print(date, value_str)

print('!'*80)





