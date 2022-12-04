with open("input.txt", 'r') as f: 
    lines = [i.strip() for i in f.readlines()] 
    list = []
    letters = []
    scores = [{'a' : 1}, {'b' : 2}, {'c' : 3}, {'d' : 4}, {'e' : 5}, {'f' : 6}, {'g' : 7}, {'h' : 8}, {'i' : 9}, {'j' : 10}, {'k' : 11}, {'l' : 12}, {'m' : 13}, {'n' : 14}, {'o' : 15}, {'p' : 16}, {'q' : 17}, {'r' : 18}, {'s' : 19}, {'t' : 20}, {'u' : 21}, {'v' : 22}, {'w' : 23}, {'x' : 24}, {'y' : 25}, {'z' : 26}, {'A' : 27}, {'B' : 28}, {'C' : 29}, {'D' : 30}, {'E' : 31}, {'F' : 32}, {'G' : 33}, {'H' : 34}, {'I' : 35}, {'J' : 36}, {'K' : 37}, {'L' : 38}, {'M' : 39}, {'N' : 40}, {'O' : 41}, {'P' : 42}, {'Q' : 43}, {'R' : 44}, {'S' : 45}, {'T' : 46}, {'U' : 47}, {'V' : 48}, {'W' : 49}, {'X' : 50}, {'Y' : 51}, {'Z' : 52}]
    points = 0
    # part 1
    for line in lines: 
        half1 = line[:len(line)//2]
        half2 = line[len(line)//2:]
        # add the two halves to the list
        list.append([half1, half2])
    #  make a list
    for item in list:
        # compate the two halves get the one letter that is in both
        for letter in item[0]:
            if letter in item[1]:
                letters.append(letter)
                # remove the letter from the second half
                item[1] = item[1].replace(letter, '')
                # add the letter to the first half
                item[0] = item[0].replace(letter, '')
                # break the loop
                break
    

    #part 2 
    # make a list of each 3 lines lines
    list = []
    for i in range(0, len(lines), 3):
        list.append([lines[i], lines[i+1], lines[i+2]])
    # for each list in list compere values and vind the matching letters
    letters = []
    for item in list:
        for letter in item[0]:
            if letter in item[1] and letter in item[2]:
                letters.append(letter)
                item[1] = item[1].replace(letter, '')
                item[0] = item[0].replace(letter, '')
                item[2] = item[2].replace(letter, '')
                break


    for letter in letters:
        for score in scores:
            if letter in score:
                points += score[letter]

    print(points)