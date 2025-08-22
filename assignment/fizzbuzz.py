num = 1
end_num = 30

while num <= end_num:
    if num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)

    num = num + 1            