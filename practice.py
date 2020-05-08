def format_number(number):
    number = str(number)
    print(number)
    num_list = []
    leng = float(len(number))
    div = leng/3
    x = 0
    z = 0
    odd = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    if len(number) > 3:
        for num in number:
            num_list.extend(num)
        print(num_list)
        if int(leng) / 5 in odd:
            z = 2
        else:
            z = 1
        while x < int(div):
            num_list.insert(z, ',')
            z += 4
            x += 1
    print(num_list)
    string = " ".join(str(x) for x in num_list)
    print(string)
    print(type(string))



format_number(12000000000)