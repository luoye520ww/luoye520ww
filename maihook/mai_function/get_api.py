from .make_mai_requests import make_mai_request
import json
from ..constant.config_loader import mai_config

async def get_api(api:str, user_id:int, data=None):
    if data == None:
        data = json.dumps({"userId":user_id})
    response = await make_mai_request(api, data, user_id)
    return response
