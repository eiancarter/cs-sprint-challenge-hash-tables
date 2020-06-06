def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    rack = dict()

    for weight in weights:
        Answer = limit - weight
        if Answer not in rack:
            rack[Answer] = 1
        else:
            return (weights.index(Answer), weights.index(weight))
    return None


print(get_indices_of_item_weights([4,4], 2, 8))