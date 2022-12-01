# open input.txt and read it
with open('input.txt') as fp:
    lst = [p.strip() for p in fp.read().split('\n\n')]
    #change \n to space
    lst = [p.replace('\n', ' ') for p in lst]
    # create list for each value of lst
    lst = [p.split(' ') for p in lst]
    #for each list in lst add the values
    lst = [sum([int(p) for p in l]) for l in lst]
    #print highest 3 values in lst
    highest = sorted(lst, reverse=True)[:3]

    #print the sum of the highest 3 values
    print(sum(highest))
    

