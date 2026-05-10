#Метод capitalize()
#Возравщение строки с первой заглавной буквой и остальными маленькими
s = 'foO BaR BAZ quX'
print(s.capitalize())
#
s = 'foo123#BAR#.'
print(s.capitalize())

#Метод swapcase()
#Преобразование верхнего регистра на нижний и наоборот

s = 'FOO Bar 123 baz qUX'
print(s.swapcase())

#Метод title() вывод первый символ каждого слова в верхний регистр

s = 'the sun also rises'
print(s.title())

# Метод lower() возвращает строку, где все символы имеют нижний регистр

s = 'FOO Bar 123 baz qUX'
print(s.lower())

#Метод upper() возвращает строку, где все символы имеют верхний регистр

s = 'FOO Bar 123 baz qUX'
print(s.upper())

##
song = 'the show must go on'
song = song.title()

print(song)