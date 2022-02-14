import numpy as np

def split_train_test(data, test_ratio):
    """
    pick some instances of data randomly
    and set the aside
    input:
              data: data to split randomly into train and test sets
              test_ratio: percentage split of the data
    output:
              data.iloc[train_indices]: random train set
              data.iloc[test_indices]: random test set
    """
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]