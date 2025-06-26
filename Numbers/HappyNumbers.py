
def isHappynumber(n):
    sum, x = n, n

    # print(sum)
    # print(x)
    # cant be single digit that isn't 1 or 7
    # basically, taking each digit off of a number, squaring
    # after squaring, adding the sum until it reaches 1.
    # if it never reaches 1, it is considered an unhappy number
    while sum > 9:
        sum = 0

        # This loop finds the sum of
        # square of digits
        while x > 0:
            d = x % 10
            print("Val of D: ",d)
            sum += d * d
            x = int(x / 10)

        x = sum
        print("sum: ", sum)

    if sum == 1 or sum == 7:
        return True

    return False


happynum = list(filter(isHappynumber, [x for x in range(0,100)]))  # leaves number in if True, else removes.
print(happynum)
