import random
import pandas as pd


# I need to 
# class Tree:

class RandomForest:
    trees = []

    def __init__ (self, df, minSplit, numLeafs, decisionTrees):
        self.df= df
        self.minSplit = minSplit
        self.numLeafs = numLeafs
        self.decisionTrees = decisionTrees


    def createDecisionTree(df):

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

            decisionTree = self.createDecisionTree(df.iloc[randomRows, randomCols])

            self.trees.append(decisionTree)
   