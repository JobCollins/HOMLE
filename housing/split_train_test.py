import numpy as np
from zlib import crc32

def test_set_check(identifier, test_ratio):
    """
    compute a hash of each instance’s identifier 
    and put that instance in the test set 
    if the hash is lower or equal to 20% of the maximum hash value.

    input:
              identifier: identifier column
              test_ratio: percentage split of the data
    output:
              a test set check
    """
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32

def split_train_test_by_id(data, test_ratio, id_column):
     """
    split data into train and test set by id
    input:
              data: data to split randomly into train and test sets
              test_ratio: percentage split of the data
              id_column: the unique identifier column
    output:
              data.loc[~in_test_set]: train set
             data.loc[in_test_set]: test set
    """
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

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