twice = ''
print(type(twice))

freq_dict = {}
frequency = 0 
while isinstance(twice, int) == False: 
    with open('adventofcode1_input.txt','r') as file:   
        for lines in file:
            lines = lines.rstrip("\n")
            frequency += int(lines)
            if frequency not in freq_dict:
                freq_dict[frequency] = 1
            else:
                twice = frequency
                break
print(type(twice))
print(twice)
            
print(twice)
            