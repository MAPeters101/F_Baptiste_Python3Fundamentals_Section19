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


source_file = 'DEXUSEU.csv'
with open(source_file) as f:
    for _ in range(5):
        print(next(f).strip())
target_file = 'output.csv'
with open(source_file) as f:
    data = f.readlines()
print(data[0:5])
del data[0]
print(data[0:5])
data = [line.strip() for line in data]
print(data[0:5])
data = [line.split(',') for line in data]
print(data[0:5])

def split_date(dt_str):
    return dt_str[:4], dt_str[5:7], dt_str[8:]
print(split_date('2015-04-09'))
year, month, day = split_date('2015-04-09')
print(year, month, day)

# def transform_row_for_output(row):
#     row = row.strip()
#     dt_str, rate = row.split(',')
#     year, month, day = split_date(dt_str)
#     result = ','.join([year,month,day,rate])
#     result += '\n'
#     return result
# print(transform_row_for_output('2015-04-03,1.0990\n'))

# def transform_row_for_output(row):
#     row = row.strip()
#     dt_str, rate = row.split(',')
#     year, month, day = split_date(dt_str)
#     month = str(int(month))
#     day = str(int(day))
#     result = ','.join([year,month,day,rate])
#     result += '\n'
#     return result
# print(transform_row_for_output('2015-04-03,1.0990\n'))
# print('='*80)

# def transform_row_for_output(row):
#     row = row.strip()
#     dt_str, rate = row.split(',')
#     year, month, day = split_date(dt_str)
#
#     try:
#         float(rate)
#     except ValueError:
#         return None
#
#     month = str(int(month))
#     day = str(int(day))
#     result = ','.join([year,month,day,rate])
#     result += '\n'
#     return result
#
# row = '2015-04-03,.\n'
# result = transform_row_for_output(row)
# print(result)
# print(type(result))
print('='*80)

def transform_row_for_output(row):
    row = row.strip()
    dt_str, rate = row.split(',')
    year, month, day = split_date(dt_str)

    try:
        float(rate)
    except ValueError:
        return ''

    month = str(int(month))
    day = str(int(day))
    result = ','.join([year,month,day,rate])
    result += '\n'
    return result

row = '2015-04-03,.\n'
result = transform_row_for_output(row)
print(result)
print(type(result))
print('='*80)


with open(source_file) as f:
    data = f.readlines()
del data[0]
with open(target_file, 'w') as f:
    f.write('YEAR,MONTH,DAY,EXCHANGE\n')
    for row in data:
        f.write(transform_row_for_output(row))

with open(target_file) as f:
    for row in f:
        print(row.strip())
print('+'*80)


def transform_file_batch(source_file, target_file):
    with open(source_file) as f:
        data = f.readlines()
    del data[0]
    with open(target_file, 'w') as f:
        f.write('YEAR,MONTH,DAY,EXCHANGE\n')
        for row in data:
            f.write(transform_row_for_output(row))

with open(target_file, 'w') as f:
    f.write('abc')

with open(target_file) as f:
    for row in f:
        print(row.strip())

transform_file_batch(source_file=source_file, target_file=target_file)
with open(target_file) as f:
    for row in f:
        print(row.strip())
print('=-'*40)


def transform_file(source_file, target_file):
    with open(source_file) as source:
        with open(target_file, 'w') as target:
            next(source)
            target.write('YEAR,MONTH,DAY,EXCHANGE\n')

            for row in source:
                target.write(transform_row_for_output(row))
transform_file(source_file, target_file)
with open(target_file) as f:
    print(f.readlines())
