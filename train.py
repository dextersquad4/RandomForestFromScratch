import pandas as pd
import RandomForest

def evaluateModel(rf, ind_val, dep_val):
    missed = 0
    made = 0
    for index, row in ind_val.iterrows():
        if rf.predict(row) != dep_val.at[index, 0]:
            missed+= 1 
        else:
            made+=1
    print(f'Accurcy: {made / (missed+made)}')
    return


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

    d_val = pd.DataFrame(data=df['Neutered_or_spayed'].cat.codes)
    for cata in catagorical: 
        if (cata != "Neutered_or_spayed"):
            df[cata] = df[cata].cat.codes
        else:
            df.pop(cata)
    #Initialize rf object
    numDecisionTrees = 50

    rf = RandomForest.RandomForest(df, d_val, numDecisionTrees)
    rf.createRandomForest()

    evaluateModel(rf, df, d_val)



    