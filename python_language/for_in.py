test = [i for i in range(1, 11)]

print(test)

print('-- 2 --------------')
print([i*2 for i in range(1, 11)])
print('-- 3 --------------')
print([i*i for i in range(1, 11)])
print('-- 4 --------------')
print([str(i) for i in range(1, 11)])
print('-- 5 --------------')
print([i for i in range(1, 11) if i % 2 == 0])