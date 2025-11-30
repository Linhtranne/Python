
import os

if not os.path.exists('file.txt'):
    with open('file.txt', 'w', encoding='utf-8') as f:
        f.write('Nội dung ban đầu\n')
        f.write('Dòng thứ hai\n')
        f.write('Dòng thứ ba\n')
        f.write('Dòng thứ tư\n')
        f.write('Dòng thứ năm\n')
        file = open('file.txt', 'r', encoding='utf-8')
        for line in file:
            print(line.strip())
        file.close()
        