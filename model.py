import pandas as pd
import numpy as np
import pickle


# Loading Recommendation System
ProductRecommendationSystem = pickle.load(file=open('./models/recommendation_engine_ubcf.pkl', 'rb'))

# Loading Recommendation System
clean_df_final = pickle.load(file=open('./models/clean_df_final.pkl', 'rb'))

def getRecommendations(username):
    try:
        # limit of 20 added due to memeory issue
        top20_recommendations = pd.DataFrame(ProductRecommendationSystem.loc[username].sort_values(ascending=False)[0:20].index)
    except KeyError:
        errorMessage=" Username '{}' doesn't not exist in the system!\n\
            Please try again with a user from 'Available Users' list provided above.".format(username)
        return errorMessage
    
    
    top5_recommendations = pd.merge(top20_recommendations,clean_df_final,on='id',how='inner').sort_values(['PositivePct'],ascending=False)[:5]
    
    ProdNames=top5_recommendations['name'].tolist()
    posSentRateList = top5_recommendations['PositivePct'].tolist()
    
    return ProdNames,posSentRateList





