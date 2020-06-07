def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    rack = dict()
    result = []
    for weight in weights:
        answer = limit - weight
        rack[answer] = weights.index(weight)
        result.append(rack[answer])
        return result
    return None


print(get_indices_of_item_weights([4,4], 2, 8))