input_list = open("day1_input.txt", "r")
numbers = []

for i in input_list:
    first = False
    first_num = 0
    second_num = 0
    for j in i:
        if j.isdigit():
            if first == False:
                first = True
                first_num = j
            else:
                second_num = j
    if second_num == 0:
        second_num = first_num
    combined = first_num + second_num
    combined = int(combined)
    print(combined)
    numbers.append(combined)

def check_spelled():
    spelled = ["one", "two", "three", "four", "five", "six", "seven", "eight","nine"]
    
print(sum(numbers))