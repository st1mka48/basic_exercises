# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
t = 0

for le in word:
    if le.lower() == 'а':
        t += 1
print(f'Количество букв "a" {t}')

# Вывести количество гласных букв в слове
letter = ['о', 'о', 'а', 'я', 'а', 'а', 'и', 'а', 'е', 'у', 'о', 'о', 'а', 'е', 'я', 'о', 'у']
word = 'Архангельск'
count = 0
for i in word:
    if i.lower() in letter:
        count += 1
print(f'Гласных букв {count}')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for i in sentence.split():
    print(i[:1])
print('-' * 40)

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
avg = 0
for j in sentence.split():
    avg += len(j)
print(avg / len(sentence.split()))


