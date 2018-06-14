def table(num, index):
    print (num * index)
    index = index + 1
    if index <= 20:
        table(num, index)
table(12, 1)
