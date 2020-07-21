def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    numbers = {}
    # look at each array
    for array in arrays:
        # look at each number in each array
        for number in array:
            # if the number is not in the numbers
            if number not in numbers:
                # number count is one
                numbers[number] = 1
            else:
                # else add to the number count because we found another
                numbers[number] += 1

    result = []
    #for each of the numbers inside the  numbers dict
    for number in numbers:
        # if we have more than one occourence of the number
        if numbers[number] > 1:
            # add the number to the results array
            result.append(number)
            
    return result


if __name__ == "__main__":
    
    print(intersection([
            [1,2,3],
            [1,4,5,3],
            [1,6,7,3]
        ]))
