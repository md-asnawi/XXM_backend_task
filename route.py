from fastapi import APIRouter, HTTPException, status

from model import Pallet
from db import collection
from schema import pallet_serializer, pallets_serializer
# from bson import ObjectId
import json

pallet = APIRouter()

@pallet.get('/')
async def find_all_pallets():
    return pallets_serializer(collection.find())

@pallet.get('/{id}')
async def find_one_pallet(id):
    # if len(id) != 24 or not id.isalnum():
    #     raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = f"ID {id} is invalid")
    try:
        return pallet_serializer(collection.find_one({"id": id}))
    except:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Pallet {id} not found")

@pallet.post('/', status_code=status.HTTP_201_CREATED)
async def create_pallet(pallet: Pallet):
    if pallet.dimensions.depth < 0.0:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = f"Depth {pallet.dimensions.depth} less than minimum")
    if pallet.dimensions.height < 0.0:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = f"Height {pallet.dimensions.height} less than minimum")
    if pallet.dimensions.pallet_height < 0.0:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = f"Pallet height {pallet.dimensions.pallet_height} less than minimum")
    if pallet.dimensions.wheel_opening_width < 0.0:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = f"Wheel opening width {pallet.dimensions.wheel_opening_width} less than minimum")
    if pallet.dimensions.width < 0.0:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = f"Width {pallet.dimensions.width} less than minimum")

    inserted_id = str(collection.insert_one(json.loads(json.dumps(pallet, default=lambda o: o.__dict__))).inserted_id)
    created_pallet = await find_one_pallet(inserted_id)
    return created_pallet["id"]

@pallet.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_pallet(id, pallet: Pallet):
    await find_one_pallet(id)
    
    if pallet.dimensions.depth < 0.0:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = f"Depth {pallet.dimensions.depth} less than minimum")
    if pallet.dimensions.height < 0.0:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = f"Height {pallet.dimensions.height} less than minimum")
    if pallet.dimensions.pallet_height < 0.0:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = f"Pallet height {pallet.dimensions.pallet_height} less than minimum")
    if pallet.dimensions.wheel_opening_width < 0.0:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = f"Wheel opening width {pallet.dimensions.wheel_opening_width} less than minimum")
    if pallet.dimensions.width < 0.0:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = f"Width {pallet.dimensions.width} less than minimum")

    collection.find_one_and_update(
        {
            "id": id
        },
        {
            "$set": json.loads(json.dumps(pallet, default=lambda o: o.__dict__))
        }
    )

@pallet.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one_pallet(id):
    await find_one_pallet(id)
    collection.find_one_and_delete({"id": id})