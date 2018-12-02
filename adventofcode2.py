with open('adventofcode2_input.txt','r') as file:
    number_three = 0
    number_two =0 
    for lines in file:
        lines = lines.rstrip("\n")
        #checking char
        char_dict = {}
        for ch in lines:
            if ch not in char_dict:
                char_dict[ch] = 1
            else:
                char_dict[ch] += 1
        appear_three = 0
        appear_two = 0
        for key in char_dict:
            if char_dict[key] == 2:
                appear_two += 1
            elif char_dict[key] == 3:
                appear_three += 1
        if appear_three > 0 : 
            number_three += 1
        if appear_two > 0:
            number_two += 1
    print(number_three * number_two)