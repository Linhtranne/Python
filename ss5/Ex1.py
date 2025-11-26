import os

if not os.path.exists('file.txt'):
    with open('file.txt', 'w', encoding='utf-8') as f:
        f.write('Nội dung ban đầu')

file = open('file.txt', 'r', encoding='utf-8')
file.close()

new_line = input("Nhập: ")

file = open('file.txt', 'a', encoding='utf-8')
file.write('\n' + new_line)
file.close()

file = open('file.txt', 'r', encoding='utf-8')
content = file.read()
print("Nội dung:")
print(content)
file.close()