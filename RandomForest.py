import random
import pandas as pd



class Tree:
    def __init__(self, num, vals, df, threshold, left=None, right=None):
        self.num = num
        self.vals = vals
        self.df = df
        self.threshold = threshold
        self.left = left
        self.right = right
        self.create()

    def createOptimalSplit(self, df, col):
        df = df.iloc[:, col]

        return split
    
    
    def create(self):
        df = self.df
        if (numCols) < 50:
            return
        else:
            numCols = (df.shape)[1]
            randomCol = int(random.random() * numCols)


    
    

class RandomForest:
    trees = []

    def __init__ (self, df, vals, minSplit, numLeafs, decisionTrees):
        self.df= df
        self.vals = vals
        self.minSplit = minSplit
        self.numLeafs = numLeafs
        self.decisionTrees = decisionTrees


    def createDecisionTree(self, df):

        return
    
    def createRandomForest(self):
        df = self.df
        itr = self.decisionTrees
        for i in range(itr):
            rows = (df.shape)[0]
            cols = (df.shape)[1]

            #Get the random rows used
            totalRows = range(0, rows)
            randomRows = random.sample(totalRows, int(rows * 0.75))

            #Get the random 2 rows
            totalCols = range(0, cols)
            randomCols = random.sample(totalCols, 2)

            decisionTree = self.createDecisionTree(df.iloc[randomRows, randomCols], vals)

            self.trees.append(decisionTree)

   