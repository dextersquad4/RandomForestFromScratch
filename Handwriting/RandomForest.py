import random
import pandas as pd

class Tree:

class RandomForest:
    trees = []

    def __init__ (self, df, minSplit, numLeafs, decisionTrees):
        self.df= df
        self.minSplit = minSplit
        self.numLeafs = numLeafs
        self.decisionTrees = decisionTrees


    def createDecisionTree():

        return
    
    def createRandomForest(self):
        df = self.df
        itr = self.decisionTrees
        for i in range(itr):

            rows = (df.shape)[0]
            cols = (df.shape)[1]
            total = range(0, cols)
            randomRows = random.sample(int(rows * 0.75), total)
            print(randomRows)
            
   