# open input.txt and read it
with open('input.txt', 'r') as file:
    data = file.read().splitlines()
    amount_1 = 0
    amount_2 = 0
    # put the data in a list
    list = []
    for line in data:
        list.append([line])
    
    # for each list in list split value on , and on -
    for i in range(len(list)):
        list[i] = list[i][0].split(',')
        for j in range(len(list[i])):
            list[i][j] = list[i][j].split('-')

    # for each list in list convert to int
    for i in range(len(list)):
        for j in range(len(list[i])):
            for k in range(len(list[i][j])):
                list[i][j][k] = int(list[i][j][k])
    
    # part 1
    for i in range(len(list)):

        if list[i][0][0] <= list[i][1][0] and list[i][0][1] >= list[i][1][1] or list[i][0][0] >= list[i][1][0] and list[i][0][1] <= list[i][1][1]:
            amount_1 += 1


    # part 2    
        if list[i][0][0] >= list[i][1][0] and list[i][0][0] <= list[i][1][1] or list[i][0][1] >= list[i][1][0] and list[i][0][1] <= list[i][1][1] or list[i][1][0] >= list[i][0][1] and list[i][1][0] <= list[i][0][1] or list[i][1][1] >= list[i][0][0] and list[i][1][1] <= list[i][0][1]:

            amount_2 += 1    
    print(amount_2)
