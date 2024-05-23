
def cuvinte(n):
    word_list = []
    for start in dict['S']:
        word_list.append(start)

    while n>1:
        word_list_new = []
        for word in word_list:
            for index in range(len(word)):
                if word[index] in dict.keys():
                    for prod in dict[word[index]]:
                        if prod != '.':
                            word_list_new.append(f'{word[:index]}{prod}')
                        else:
                            word_list_new.append(f'{word[:index]}')
        word_list = word_list_new
        n -= 1

    with open("outputfile.txt", "w") as g:
        for word in word_list:
            if word.islower():
                g.write(f'{word}\n')

with open("inputfile.txt") as f:
    dict = {}
    for line in f:
        temp = line.strip().split()
        dict[temp[0]] = []
        for elem in temp[1:]:
            if elem != "->" and elem != "|":
                dict[temp[0]].append(elem)

n = int(input("Lungimea cuvintelor: "))
cuvinte(n)
