import pandas as pd
import RandomForest


if __name__ == "__main__":

    #get data and assign catagorical data
    df = pd.read_csv("archive (4)/cat_breeds_clean.csv", sep=';')
    df['Breed'] = pd.Categorical(df.Breed)
    df['Gender'] = pd.Categorical(df.Gender)
    df['Neutered_or_spayed'] = pd.Categorical(df.Neutered_or_spayed)
    df['Fur_colour_dominant'] = pd.Categorical(df.Fur_colour_dominant)
    df['Fur_pattern'] = pd.Categorical(df.Fur_pattern)
    df['Eye_colour'] = pd.Categorical(df.Eye_colour)
    df['Allowed_outdoor'] = pd.Categorical(df.Allowed_outdoor)
    df['Preferred_food'] = pd.Categorical(df.Preferred_food)
    df['Country'] = pd.Categorical(df.Country)

    catagorical = ['Breed', 'Gender', 'Neutered_or_spayed', 'Fur_colour_dominant', 'Fur_pattern', 'Eye_colour', 'Allowed_outdoor', 'Preferred_food', 'Country']

    ind_val = pd.DataFrame(data=df['Neutered_or_spayed'].cat.codes)
    for cata in catagorical: 
        if (cata != "Neutered_or_spayed"):
            df[cata] = df[cata].cat.codes
        else:
            df.pop(cata)


    #Initialize rf object
    minSplit = 50
    leafDepth = 5
    numDecisionTrees = 50

    rf = RandomForest.RandomForest(df, ind_val, 50, 5, 50)
    rf.createRandomForest()




    