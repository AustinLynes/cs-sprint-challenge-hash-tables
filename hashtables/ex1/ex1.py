# Given a package with a weight limit `limit` and a list `weights` of item
# weights, implement a function `get_indices_of_item_weights` that finds
# two items whose sum of weights equals the weight limit `limit`. Your
# function will return a tuple of integers that has the following form:
# ```
# (zero, one)
# ```

# where each element represents the item weights of the two packages.
# _**The higher valued index should be placed in the `zeroth` index and
# the smaller index should be placed in the `first` index.**_ If such a
# pair doesn’t exist for the given inputs, your function should return

# Example:
# ```
# input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
# output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
# ```


"""
YOUR CODE HERE
"""
def get_indices_of_item_weights(weights, length, limit):
    # if you give me invalid input then im gonna give you nothing in return
    if length <= 1:
        return None
    
    _table = {}
    _indices = []
    cur = 0;

    while cur < length:

        cur += 1 
        
    for k, v in _table.items():
    
        if k < length - 1:
            if _table[k] + _table[k + 1] == limit:
                _indices.append(_table[k])
                _indices.append(_table[k + 1])

    return _indices

weights_2 = [4, 4]
print(get_indices_of_item_weights(weights_2, 2, 8))
#  [ 1, 0 ]