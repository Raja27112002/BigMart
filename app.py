from flask import Flask, render_template, request
import pickle

application = Flask(__name__)


@application.route('/', methods= ['GET', 'POST'])

def homePage():
    return render_template("index.html")

@application.route('/predict', methods= ['POST'])

def prediction():
    try:
        if (request.method == 'POST'):
            Item_Weight = float(request.form['Item_Weight'])

            Item_Fat_Content = request.form['Item_Fat_Content']

            Item_Visibility = float(request.form['Item_Visibility'])

            Item_Type = request.form['Item_Type']

            Item_MRP = float(request.form['Item_MRP'])

            Outlet_Establishment_Year = (request.form['Outlet_Establishment_Year'])

            Outlet_Size = request.form['Outlet_Size']

            Outlet_Location_Type = request.form['Outlet_Location_Type']

            Outlet_Type = request.form['Outlet_Type']

            categorical_encode = {'Low Fat': 1, 'Regular': 2, 'low fat': 3, 'LF': 0, 'reg': 4, 'Dairy': 4,
                                  'Soft Drinks': 14, 'Meat': 10,
                                  'Fruits and Vegetables': 6, 'Household': 9,
                                  'Baking Goods': 0, 'Snack Foods': 13, 'Frozen Foods': 5, 'Breakfast': 2,
                                  'Health and Hygiene': 8, 'Hard Drinks': 7, 'Canned': 3, 'Breads': 1,
                                  'Starchy Foods': 15,
                                  'Others': 11, 'Seafood': 12, 'Medium': 1, 'High': 0, 'Small': 2, 'Tier1': 0,
                                  "Tier2": 1,
                                  "Tier3": 2,
                                  'Supermarket Type1': 1,
                                  'Supermarket Type2': 2, 'Grocery Store': 0,
                                  'Supermarket Type3': 3}
            New_Item_Fat_Content = categorical_encode[Item_Fat_Content]

            New_Item_Type = categorical_encode[Item_Type]

            New_Outlet_Size = categorical_encode[Outlet_Size]

            New_Outlet_Location_Type = categorical_encode[Outlet_Location_Type]

            New_Outlet_Type = categorical_encode[Outlet_Type]
            filename = 'refgressors.pickle'
            loaded_model=pickle.load(open(filename,'rb'))
            predic = loaded_model.predict(
                [[Item_Weight,New_Item_Fat_Content,Item_Visibility,
                  New_Item_Type,Item_MRP,
                  Outlet_Establishment_Year, New_Outlet_Size,
                  New_Outlet_Location_Type, New_Outlet_Type]])

            print('prediction is',predic)

            return render_template('results.html',prediction=predic)

        else:

            return render_template('index.html')
    except Exception as e:
        return render_template('results.html',prediction=e)
    
    
if __name__ == '__main__':
    application.run(port=4000,debug=True)
