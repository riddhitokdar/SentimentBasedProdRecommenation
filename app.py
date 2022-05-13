# Importing required libraries
from flask import Flask, render_template, request, redirect, url_for
#import warnings
import pandas as pd
#warnings.filterwarnings("ignore")

#importing model
import model

#initialising flask
app = Flask(__name__)

# Defining method for root path
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend-products', methods=['POST'])
def recommendProducts():
    # Fetching the user entered username 
    username =  str(request.form.get('username'))
    # Getting recommendations for user using the model
    productNameList, posSentimentRateList = model.getRecommendations(username)
    productList = zip(productNameList, posSentimentRateList)
    prd=pd.DataFrame(productList,columns=["Product Name","Positive Sentiment Percentage"])
    prd_table=prd.to_html()
    # Defining Table title
    table_title = 'Top 5 Product Recommendations for : {}'.format(username)
    # Rendering Template while passing the results
    return  render_template('index.html', productsTable = prd_table, titles=table_title)


@app.route('/allusernames', methods=['GET'])
def allUsernames():
    # Reading usernames from source i.e. recommendation system
    usernamesList = list(model.ProductRecommendationSystem.index)

    # Converting List to a dataframe
    usernamesDF = pd.DataFrame(usernamesList, columns=['Available Usernames'])

    # Creating a HTML table using DataFrame
    usernameTable = [usernamesDF.to_html()]
    # Defining Table title
    table_title = ['NAN', 'List of all usernames available in SBPRS Database']

    # Rendering the page
    return render_template('allusernames.html', usernameTable = usernameTable, titles = table_title )

if __name__ == '__main__':
    #print('Sentiment Based Product Recommendation System')
    app.run(debug = False)



