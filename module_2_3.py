my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(my_list):
    if 0 > my_list[a]:
        continue
    print(my_list[a])
    a += 1
