import numpy as np

class DecisionTree:
    """A modified version of decision tree to find the best spliting feature"""

    def best_feature(self, dataset):
        features = dataset.columns.tolist()[1:]

        info_gains = {}
        for feature in features:
            right, left = self.split(dataset, feature)

            if right.empty or left.empty:
                continue

            info_gain = self.information_gain(dataset['name'], right, left)

            info_gains[feature] = info_gain

        if info_gains:
            return max(info_gains, key = info_gains.get) #type: ignore
        else:
            return None
    
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