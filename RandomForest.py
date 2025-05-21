import random
import pandas as pd



class Tree:
    threshold = None
    colEditted = None
    mode = None
    def __init__(self, vals, df, depth, left=None, right=None):
        self.vals = vals
        self.df = df
        self.depth = depth
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
        leftVal = self.vals[left_mask]
        leftdf = df[left_mask]

        right_mask =  df.iloc[:, col] > minSplit
        rightVal = self.vals[right_mask]
        rightdf = df[right_mask]

        #Stop if either has a size less than 50
        if (leftdf.shape)[0] < 10 or (rightdf.shape)[0] < 10 or self.depth == 5:
            return
        else:
            #Assign left and right splits
            self.left = Tree(leftVal, leftdf, self.depth+1)
            self.right = Tree(rightVal, rightdf, self.depth+1)

            #Assigning threshold so we can predict
            self.threshold = minSplit
            self.colEditted = df.columns[col]

    def create(self):
        df = self.df
        self.mode = (self.vals.mode()).iloc[0,0]
        numCols = (df.shape)[1]
        randomCol = int(random.random() * numCols)
        self.createOptimalSplit(self.vals, df, randomCol)

    def assignLeftRight(self, series):
        if (series[self.colEditted] <= self.threshold):
            return self.left
        return self.right


    
    

class RandomForest:
    trees = []

    def __init__ (self, df, vals, decisionTrees):
        self.df= df
        self.vals = vals
        self.decisionTrees = decisionTrees


    def createDecisionTree(self, df, vals):
        # Return the head of the tree
        return Tree(vals,df, 1)
    
    def createRandomForest(self):
        df = self.df
        itr = self.decisionTrees
        for i in range(itr):
            rows = (df.shape)[0]
            
            #Get the random rows used
            totalRows = range(0, rows)
            randomRows = random.sample(totalRows, int(rows * 0.75))

            decisionTree = self.createDecisionTree(df.iloc[randomRows], self.vals.iloc[randomRows])
            print(f'Finished {i+1}th tree')

            self.trees.append(decisionTree)

    def predict(self, series):
        sum = 0
        for tree in self.trees:
            while tree.left != None and tree.right != None:
                tree = tree.assignLeftRight(series)
            sum+=tree.mode
        return round(sum / len(self.trees))
            
            



   