input_list = open("day2_input.txt", "r")
def get_id(line):
    line = line.split(":")
    line = line[0]
    line = line.split(" ")
    id = line[1]
    id = int(id)
    return id

def get_game(line):
    line = line.split(":")
    line = line[1]
    return line

for i in input_list:
    print(get_game(i))
