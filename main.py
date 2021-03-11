'''

Sieve of Eratosthenes

'''
def sieve( listOfNums, upperBound ):
    print("Finding Primes! ")
    numToFilter = 3
    while ( numToFilter < upperBound ):
        for t in listOfNums:
            # print( t, " ", numToFilter)
            
            # print( (t == numToFilter))
            if ( t != numToFilter):
                if ( t % numToFilter ) == 0:
                    listOfNums.remove(t)
                    # print( "num removed ", t)
            
        numToFilter += 1;

    
    
listOfNums = []

upperBound = 10001
for x in range(upperBound):
    if ( x == 2 ) | ( x % 2 ) == 1:
        listOfNums.append(x)

sieve( listOfNums, upperBound )

itr = 0
for p in listOfNums:
    if ( itr == 101 ):
        print()
    print( p, end = " " )
    itr += 1
    

