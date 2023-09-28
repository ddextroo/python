def format_number(n):
    str_n = str(n)
    new = ''
    count = 0
    for _ in str_n[::-1]:
        count += 1
        new = _ + new
        print(new, count)
        if count % 3 == 0 and count != len(str_n):
            new = ',' + new
    return new
        
format_number(1234567)
print(7 % 3 == 0)
'''
c=  0
0001

1


'''