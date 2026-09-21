import numpy as np

class DecisionTree:
    """A modified version of decision tree to find the best spliting feature"""

    def __init__(self, min_sample_split=2, max_depth=1):
        self.min_sample_split = min_sample_split
        self.max_depth = max_depth

    def best_feature(self, dataset):
        features = dataset.columns.tolist()[1:]

        info_gains = {}
        for feature in features:
            right, left = self.split(dataset, feature)
            info_gain = self.information_gain(dataset['name'], right, left)

            info_gains[feature] = info_gain

        return max(info_gains, key = info_gains.get) #type: ignore
    
    def split(self, dataset, feature):
        right = dataset[dataset[feature] == True]
        left = dataset[dataset[feature] == False]

        return right, left

    def information_gain(self, target, right, left):

        target_entropy = self.entropy(target)
        right_entropy = self.entropy(right)
        left_entropy = self.entropy(left)

        weighted_entropy = len(right)/len(target)*right_entropy + (len(left)/len(target)*left_entropy)

        return (target_entropy - weighted_entropy)

    def entropy(self, y):
        p = y.value_counts() / y.shape[0]
        return np.sum(-p*np.log2(p+1e-9))