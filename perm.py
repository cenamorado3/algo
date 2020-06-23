#permutes the given iterable        
def perm(iterable, r=None):

'''
example:
    permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    permutations(range(3)) --> 012 021 102 120 201 210
'''
    
    #generates a tuple from the given iterable object. keep in mind tuples are imutable.
    pool = tuple(iterable)
    n = len(pool)
    
    #if an r argument is given, it must be greater than the len(pool) or len(iterable)
    r = n if r is None else r
    if r > n:
        return
    
    #generate a list of indices, 0 - (n-1) -> [0,1,2,3,4]
    indices = list(range(n))
    #generate a list of indices/'cycles',-> [5,4,3,2,1]
    cycles = list(range(n, n-r, -1))
    #yields or 'generates' a tuple of pool[i] where i is the range of indices[:r], if is r is omitted, it yields the tuple(iterable)?
    yield tuple(pool[i] for i in indices[:r])
    while n:
        #reverses r, 4,3,2,1,0
        for i in reversed(range(r)):
            #decrements i by 1
            cycles[i] -= 1
            if cycles[i] == 0:
              #
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return





'''
DRIVER
a = list(perm('531')) #it is important to note this is a generator function, extra step must be taken to avoid <generator object perm at 0x0...........> statements
b = [''.join(i) for i in a] #string elements of list for output
print('FINAL OUTPUT')
print(b)

SAMPLE OUTPUT
init indices: [0, 1, 2]
init cycles: [3, 2, 1]      
yield
('5', '3', '1')
enter while
enter for
i is 2
cycles: [3, 2, 0]
cycles[i] == 0
[2]
1
i is 1
cycles: [3, 1, 1]
cycles[i] != 0
None
j is: 1
pre-swap indices: [0, 1, 2] 
post swap indices: [0, 2, 1]
('5', '1', '3')
yield and break
enter for
i is 2
cycles: [3, 1, 0]
cycles[i] == 0
[1]
1
i is 1
cycles: [3, 0, 1]
cycles[i] == 0
[1, 2]
2
i is 0
cycles: [2, 2, 1]
cycles[i] != 0
None
j is: 2
pre-swap indices: [0, 1, 2]
post swap indices: [1, 0, 2]
('3', '5', '1')
yield and break
enter for
i is 2
cycles: [2, 2, 0]
cycles[i] == 0
[2]
1
i is 1
cycles: [2, 1, 1]
cycles[i] != 0
None
j is: 1
pre-swap indices: [1, 0, 2]
post swap indices: [1, 2, 0]
('3', '1', '5')
yield and break
enter for
i is 2
cycles: [2, 1, 0]
cycles[i] == 0
[0]
1
i is 1
cycles: [2, 0, 1]
cycles[i] == 0
[0, 2]
2
i is 0
cycles: [1, 2, 1]
cycles[i] != 0
None
j is: 1
pre-swap indices: [1, 0, 2]
post swap indices: [2, 0, 1]
('1', '5', '3')
yield and break
enter for
i is 2
cycles: [1, 2, 0]
cycles[i] == 0
[1]
1
i is 1
cycles: [1, 1, 1]
cycles[i] != 0
None
j is: 1
pre-swap indices: [2, 0, 1]
post swap indices: [2, 1, 0]
('1', '3', '5')
yield and break
enter for
i is 2
cycles: [1, 1, 0]
cycles[i] == 0
[0]
1
i is 1
cycles: [1, 0, 1]
cycles[i] == 0
[0, 1]
2
i is 0
cycles: [0, 2, 1]
cycles[i] == 0
[0, 1, 2]
3
FINAL OUTPUT
['531', '513', '351', '315', '153', '135']
'''
