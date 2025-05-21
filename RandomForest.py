import random
import pandas as pd



class Tree:
    def __init__(self, vals, df, threshold = None, left=None, right=None):
        self.vals = vals
        self.df = df
        self.threshold = threshold
        self.left = left
        self.right = right
        self.create()

    def createOptimalSplit(self, val, df, col):
        columnOfInterest = df.iloc[:, col]
        unq = columnOfInterest.unique()

        # Standard deviation
        def score(dep, df, split):
            lhs = df<=split
            return (dep[lhs].std() + dep[~lhs].std())/len(dep)
        
        #Try to minimize the standard deviation amongst the two splits
        min = 100
        minSplit = -1
        for i in unq:
            curScore = score(val, columnOfInterest, i)
            if (curScore.values)[0] < min:
                min = (curScore.values)[0]
                minSplit = i

        #Get teh left and right df to pass to subtrees
        left_mask = df.iloc[:, col] <= minSplit
        leftVal = df[left_mask]
        leftdf = df[left_mask]

        right_mask =  df.iloc[:, col] > minSplit
        rightVal = df[right_mask]
        rightdf = df[right_mask]

        #Stop if either has a size less than 50
        if (leftdf.shape)[0] < 50 or (rightdf.shape)[0] < 50:
            return
        else:
            #Assign left and right splits
            self.left = Tree(leftVal, leftdf)
            self.right = Tree(rightVal, rightdf)

            #Assigning threshold so we can predict
            self.threshold = minSplit

    def create(self):
        df = self.df
        numCols = (df.shape)[1]
        randomCol = int(random.random() * numCols)
        self.createOptimalSplit(self.vals, df, randomCol)


    
    

class RandomForest:
    trees = []

    def __init__ (self, df, vals, minSplit, numLeafs, decisionTrees):
        self.df= df
        self.vals = vals
        self.minSplit = minSplit
        self.numLeafs = numLeafs
        self.decisionTrees = decisionTrees


    def createDecisionTree(self, df, vals):
        # Return the head of the tree
        return Tree(vals,df)
    
    def createRandomForest(self):
        df = self.df
        itr = self.decisionTrees
        for i in range(itr):
            rows = (df.shape)[0]
            
            #Get the random rows used
            totalRows = range(0, rows)
            randomRows = random.sample(totalRows, int(rows * 0.75))

            decisionTree = self.createDecisionTree(df.iloc[randomRows], self.vals.iloc[randomRows])
            print(f'Finished {i} tree')

            self.trees.append(decisionTree)

   