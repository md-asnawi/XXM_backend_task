def pallet_serializer(pallet) -> dict:
    return {
        "id": str(pallet["id"]),
        "display_name": pallet["display_name"],
        "description": pallet["description"],
        "dimensions": pallet["dimensions"]
    }

def pallets_serializer(pallets) -> list:
    return [pallet_serializer(pallet) for pallet in pallets]