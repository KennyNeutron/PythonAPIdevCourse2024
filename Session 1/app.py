from flask import Flask, request


app= Flask(__name__)


stores = [
    {
        "name": "My Store", 
        "items": [
            {
                "name": "Chair",
                "price": 19.99
            },
            {
                "name": "Laptop",
                "price": 1099.99
            }
        ]
    }

]


# print(stores[0]["name"])


# #Create item
# new_item = {
#     "name": request.get_json()["name"],
#     "price": request.get_json()["price"]
# }

# stores[0]["items"].append(new_item)


#Create our very first endpoint
# '/store' endpoint
@app.get("/store")

def get_stores():
    return stores


#Create our second endpoint
@app.post("/store")
def create_store():
    #Get the JSON payload from the POST request
    store_data = request.get_json()

    #print(store_data)

    #Create a new store using dictionary
    new_store= {
        "name": store_data["name"],
        "items": []
    }

    stores.append(new_store)

    return new_store, 201


#Create a new endpoint where in we utilize the URL segments
#FORMAT: endpoint/<dtype: var_name>
@app.get('/store/<string:store_name>')
def get_store(store_name):
    for store in stores:
        if(store["name"]) == store_name:
            return store
        
#Create a new endpoint to create a new item
@app.post('/store/<string:store_name>/item')
def create_item(store_name):
    item_data = request.get_json()

    for store in stores:
        if(store["name"]) == store_name:
            new_item = {
                "name": item_data["name"],
                "price": item_data["price"]
            }
            
            store["items"].append(new_item)
            return new_item, 201
    
    return {"message": "Store Not Found"},404


# This would run our flask web app
if __name__ == '__main__':
    app.run(debug=True)