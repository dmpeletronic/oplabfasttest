
def searchsequence(searchlist, target):
    ''' Given a list of numbers and target, return a tuple of initial
        and final position which sums up to target value when iterated.
        Return (-1,1) when it is not possible to achieve the target
        Example :
            Input list: [4, 3, 10, 2, 8]
            Target: 12
            Returns [2, 3]         
    '''
    initpos = 0
    while initpos < len(searchlist) :
        acc = 0
        # Seach from init position to the end of the list
        for i,value in enumerate(searchlist[initpos:], 0):
            acc = acc + value
            # Accumulate the value and check if target was achieved
            if (acc == target):
                # If so, we found the start and end point
                endpos = initpos+i
                return initpos, endpos
            elif (acc > target):
                # limit exceed, try next start position
                break
        initpos = initpos + 1
    # When achieving here, the result wasn't found
    return -1, 1