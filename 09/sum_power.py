def sum_pow_recur(pow):
    if pow == 0:
        return 0
    else:
        next = 2 ** (pow - 1)
        return next + sum_pow_recur(pow - 1)
    
def main():
    print(sum_pow_recur(3))


main()