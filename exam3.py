

def f1(l,m):
    '''
    type(l): list(int)
    type(m): list(int)
    type(return): int
    l,m do not change
    PRECONDITION: len(l) == len(m)
    >>> f1([],[]) ==>0
    >>> f1([2,3],[1,4]) ==> 2*1 + 3*4 = 14

    '''
    


def f2(cipher,text):
    '''
    type(cipher): dictionary(Key:String,Value:String)
    type(text): String
    type(return): String

    PRECONDITION: cipher is good with lowercase letters as keys and values
                  text is a (possibly empty) string of lowercase letter
    Returns an encoded copy of text using given cipher dictionary
    Example: 
    >>> f2({'a':'o','z':'b'},'razzle') ==> 'robble'
    '''
 pass # replace this with your code

def f3(l,m):
    '''
    type(l): list(T)
    type(m): list(T)
    type(return): list(T)
    l, m do not change
    
    Returns the list of common elements of l,m in the order in which they appear in l
    >>> f4([1,2,3],[4,5]) ==> []
    >>> f4([1,2,3],[4,3,6],[7,8,3]) ==> [3]
    >>> f4([1,2,3],[4,3,1,6],[7,8,3,1]) ==> [1,3]
    '''
    pass


def f4(l,m,n):
    '''
    type(l): list(T)
    type(m): list(T)
    type(n): list(T)
    type(return): list(T
    l, m, n do not change
    
    Returns the list of common elements of l,m,n in the order in which they appear in l
    >>> f5([1,2,3],[4,6],[7,8,9]) ==> []
    >>> f5([1,2,3],[3],[7,3]) ==> [3]
    >>> f5([9,1,2,3],[4,3,1,6],[7,8,3,1,5]) ==> [1,3]

    NO LOOPS PERMITTED
    USE the function f4 that you have written above
    '''
    pass # 



def f5(l,i):
    '''
    type(l): list(T)
    i: int
    type(return): list(T)
    l does not change
    PRECONDITION: i >= 0 and i < len(l)
    Returns a copy of l with the ith element removed
    >>> f5([1,2,3],1) ==> [1,3]
    >>> f5([[1,2],[3,4],[5,6]],2) ==> [[1,2],[3,4]]
    '''
    pass # replace this with your code


def f6(t,r,c):
    '''
    type(t): table(int)
    type(r): int
    type(c): int
    type(return): table(int)
    t does not change
    PRECONDITION: t is a table of ints
                  All elements of t are list(int) of the same length
    This function removes a single row r and a single column c from t.
    See exam3.pdf for examples
    '''
# Hint: you may find it useful to use f6 as a helper function
pass # replace this with your code


def f7(d1, d2):
    '''
    type(d1): dictionary(Key: String, Value: List(int))
    type(d2): dictionary(Key: String, Value: List(int))
    type(return): NONE
    
    d1 and d2 are (possibly empty) dictionaries representing win-loss records:
    Each key is a non-empty string representing a team name.
    The value for each key is a two-item list of ints, where the first is
    the number of wins and the second is the number of losses for that
    team in some tournament.
    
    This function adds the win-loss records of d2 into d1.
    It does NOT return anything; it changes d1 but not d2.
    And, the values in the altered d1 should be different list objects than the
    list objects that are values in d2, even if they have the same numbers in them.
    
    example:
    if d1 is {"Cornell": [10,1], "Harvard": [4,3]}
       d2 is {"Cornell": [2,0], "Stanford": [0,3]}
    then with f8(d1,d2) 
       d1 becomes {"Cornell": [10,1], "Harvard": [4,3], "Stanford": [0,3]}
       d2: does not change
'''
pass # replace this with your code

