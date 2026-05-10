
s = 'abcdefghij'
print(s[2:5])
print(s[0:6])
print(s[2:7])

print(s[-9:-4])
print(s[-3:])
print(s[:-3])
print(s[::-1])

print(s[1:7:2])
print(s[3::2])
print(s[:7:3])
print(s[::2])
print(s[::-1])
print(s[::-2])

#Изменение строки
s = s[:4] + 'X' + s[5:]

s = 'abcdefghij'

print(s[2:][:-2])
print(s[1::2][::-1][:3])