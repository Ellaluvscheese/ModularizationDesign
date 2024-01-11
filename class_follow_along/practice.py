# test

def dollars_from_euros(euro):
    return(round(1.13 * euro, 2))

def dollars_from_euros_test():
    testing = True
    euro_amount = float(input('Please input a Euro value: '))
    while testing:
        if euro_amount == -22:
            testing = False
            print(f"The dollar value for {euro_amount} \
                  is ${dollars_from_euros(euro_amount)}")
        
def dollars_from_euros_auto():
    assert 113 == dollars_from_euros(100)
    print("yay")

if __debug__:
    dollars_from_euros_auto()