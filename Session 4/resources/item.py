from db import items, stores
import uuid

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("items", __name__, description="Operations on items.")

#blp.arguments - papasok na data
#blp.response - palabas

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    # Validation for the response
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        if item_id in items:
            return items[item_id]

        abort(404, message="Item not found.")

    def delete(self, item_id):
        if item_id in items:
            del items[item_id]
            return {"message": "Item deleted."}
        else:
            abort(404, message="Item not found")

    # Validates the update item
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemUpdateSchema)
    def put(self, new_item_data, item_id):
    
        if item_id in items:
            item = items[item_id]
            item |= new_item_data

            return item
        
        abort(404, message="Item not found.")

@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return list(items.values())
    

    # Data Validation: JSON -> Blp.Arg -> POST Method
    @blp.arguments(ItemSchema) 
    @blp.response(200, ItemSchema)
    def post(self, item_data):
        for item in items.values():
            if (
                item["name"] == item_data["name"] 
                and item_data["store_id"] == item["store_id"]
            ):
                abort(400, message="Item already exists.")
            

            if item_data["store_id"] in stores:
                item_id = uuid.uuid4().hex

                new_item = {
                    "id": item_id,
                    "name": item_data["name"],
                    "price": item_data["price"],
                    "store_id": item_data["store_id"],
                }

                items.update({item_id:new_item})

                return new_item, 201

        abort(404, message="Store not found.")