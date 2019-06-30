# Challenge of the day
# Alphabet Dictionary in single line of code
# i.e. {1 = 'A', 2 = 'B'.................26 = 'Z'}

print(dict(zip([n for n in range(1,27)], [chr(c) for c in range(65,91)])))