def has_negatives(a):
    """
    YOUR CODE HERE
    """
    numbers = dict()
    negatives = []
    for number in a:
        if number not in numbers and number < 0:
            numbers[abs(number)] = number
    for num in a:
        if num in numbers:
            negatives.append(num)

    return negatives
        


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
