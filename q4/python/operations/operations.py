
def is_even(bn):
    ''' Check if a given number is even
        Return true if is even, false otherwise.
        4 is an even number.
        5 is an odd number.
    '''
    if bn & 1:
        return False
    else:
        return True

def is_power_of_2(bn):
    ''' Check if a number is power of 2.
        A power of 2 number will have only one bit as 1
    '''
    if (bn <= 1):
        return False
    number = bn
    max_1 = 0
    while max_1 <= 1 and number > 0:
        if (number & 1):
            max_1 = max_1 + 1
        number = number >> 1
    
    return (max_1 == 1)

def find_closest_upper_power_of_2(bn):
    ''' Given a bignumber, find the power of 2 that is highier then the bignumber.
        For the higher power of 2, duplicate the number, rotate to right and clear all 1
        than rotate back
        Example:
        40 = 0x28 =0b00101000
                        << 1    duplicate
                   0b01010000
                      |__________rotate this number 1 to the right and count
                   0b00000001
                            |____rotate the 1 to the left the "count" times from step before
                   0b00100000
                       |_________this is the lower power of 2: 0x40 = 64decimal    
    '''
    n = bn << 1
    count = 0
    while n > 1:
        n = n >> 1
        count = count + 1
    while count > 0:
        n = n << 1
        count = count - 1
    return n

def find_closest_lower_power_of_2(bn):
    ''' Given a bignumber, find the power of 2 that is smaller then the bignumber.
        For the lower power of 2, rotate to right and clear all 1 except the most left.
        Example:
        40 = 0x28 =0b00101000
                       |_________rotate this number 1 to the right and count
                   0b00000001
                            |____rotate the 1 to the left the "count" times from step before
                   0b00100000
                       |_________this is the lower power of 2: 0x20 = 32decimal
    '''
    n = bn 
    count = 0
    while n > 1:
        n = n >> 1
        count = count + 1
    while count > 0:
        n = n << 1
        count = count - 1
    return n

def find_closest_power_of_2(bn):
    ''' Given a bignumber, find the closes power of 2 number
        Return the one that is closest to the given bignumber
    '''
    upper = find_closest_upper_power_of_2(bn)
    lower = find_closest_lower_power_of_2(bn)

    if bn - lower > upper - bn:
        return upper
    else:
        return lower

def get_operations(bignumber):
    ''' Function that receives a big number and calculates how many operations
        are necessary to reduce this number to 1.
        The valid operations are:
         * add 1
         * subtract 1
         * divide by 2 when the number is even
        The functions returns the number of operations.
    '''
    operations = 0
    bn = int(bignumber)
    while bn > 1:
        #print("Current bn ", bn)
        if is_even(bn):
            # for even numbers, just divide
            bn = bn >> 1
            operations = operations + 1
        else:
            # for odd numbers we need to find the closest power of 2, and 
            # move into its direction (sum or sub)
            close = find_closest_power_of_2(bn)
            if close < bn:
                bn = bn - 1
                operations = operations + 1
            else:
                bn = bn + 1
                operations = operations + 1
    return operations
