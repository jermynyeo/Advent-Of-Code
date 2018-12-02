def difference( str1, str2 ):
    diff = 0 
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]: 
                diff += 1
        return diff 
    
with open('adventofcode2_input.txt','r') as file:
    id_list = []
    for lines in file:
        lines = lines.rstrip('\n')
        id_list.append(lines)
for id in id_list:
    for id2 in id_list:
        char_diff = difference(id,id2)
        if char_diff == 1:
            print(id,id2)
