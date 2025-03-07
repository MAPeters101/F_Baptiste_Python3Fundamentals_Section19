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







