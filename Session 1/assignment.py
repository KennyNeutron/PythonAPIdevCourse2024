from flask import Flask, request

app = Flask(__name__)


accounts = [
    {
        "name": "Naruto Uzumaki",
        "age": 33,
        "hobby": "Ninjutsu"
    },
    {
        "name": "Sasuke Uchiha",
        "age": 34,
        "hobby": "genjutsu"
    },
    {
        "name": "Sakura Haruno",
        "age": 32,
        "hobby": "summoning"
    }
]

@app.get("/accounts")
def get_accounts():
    return accounts


@app.post("/accounts")
def create_account():
    store_data = request.get_json()

    new_account = {
        "name": store_data["name"],
        "age": store_data["age"],
        "hobby": store_data["hobby"]
    }          

    accounts.append(new_account)

    return new_account, 201


@app.get("/accounts/<string:account_name>")
def get_account(account_name):
    for account in accounts:
        if(account["name"]) == account_name:
            return account

# This would run our flask web app
if __name__ == '__main__':
    app.run(debug=True)