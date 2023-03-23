import os
import time


time1 = time.time()

list_dir = [
    'rfc-ref.txt',
    'rfc3164.txt',
    'rfc4287.txt',
    'rfc4709.txt',
    'rfc5023.txt',
    'rfc5785.txt',
    'rfc5829.txt',
    'rfc5988.txt',
    'rfc5995.txt',
    'rfc6272.txt'
]

for index, file in enumerate(list_dir):
    t2 = time.time()
    my_file = os.path.abspath(f'{file}')

    with open(my_file, mode='r', encoding='ISO-8859-1') as the_file:

        content = the_file.read()

        find_text = 'Gregorio'

        if find_text in content:
            with open('success.txt', 'a') as temp_file:
                temp_file.write(my_file + '\n')
                print(f'{index}\t✅ {my_file}')
        else:
            with open('failures.txt', 'a') as temp_file:
                temp_file.write(my_file + '\n')
                print(f'{index}\t❌ {my_file}')
    t3 = time.time()
    t23 = t3 - t2
    print(f'🕛 Total Time: {t23}')

time4 = time.time()
t14 = time4 - time1


print(f'⌛ Total Time: {t14}')