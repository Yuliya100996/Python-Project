for i in range(3, 21):
    string = ''
    for j in range(1, i):
        for k in range(j+1, i):
            if i % (j+k) == 0:
                string += str(j) + str(k)
    print(f'{i} - {string}')