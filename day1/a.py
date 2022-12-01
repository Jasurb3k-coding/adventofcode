max1_num = 0
max2_num = 0
max3_num = 0
current_num = 0


with open('a.txt', 'r') as file:
    for line in file.readlines():
        if line == '\n':
            if current_num > max3_num:
                max_num3 = current_num
                if current_num > max2_num:
                    max3_num = max2_num
                    max2_num = current_num
                    if current_num > max1_num:
                        max2_num = max1_num
                        max1_num = current_num
            current_num = 0
        else:
            current_num += int(line.replace('\n', ''))
print(max1_num+max2_num+max3_num)
