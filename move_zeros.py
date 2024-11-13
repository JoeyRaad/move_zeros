#solved with 2 solutions + need also comments and more review

def move_zeros(numbers):

    #create list to get non-zero elements
    non_zeros= [num for num in numbers if num!=0]
    #create a counter for zeros
    zeros_count= numbers.count(0)
    #add zeros to the non-zeros list
    return non_zeros + [0]*zeros_count


numbers = [0, 1, 0, 3, 12]
result = move_zeros(numbers)
print(result)  # Output: [1, 3, 12, 0, 0]
