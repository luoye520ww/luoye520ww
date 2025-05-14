from .make_mai_requests import make_mai_request
import json
from ..constant.config_loader import mai_config

async def login(user_id, timestamp):
    api = 'UserLoginApiMaimaiChn'
    data = json.dumps({
        "userId":user_id,
        "acsessCode":"",
        "regionId":mai_config["regionId"],
        "placeId":mai_config["placeId"],
        "clientId":mai_config["clientId"],
        "dateTime":timestamp,
        "isContinue":False,
        "genericFlag":0
    },separators=(',',':'))
    response = await make_mai_request(api, data, user_id)
    return response

async def logout(user_id, timestamp):
    api = 'UserLogoutApiMaimaiChn'
    data = json.dumps({
        "userId": user_id,
        "regionId":mai_config["regionId"],
        "placeId":mai_config["placeId"],
        "clientId":mai_config["clientId"],
        "dateTime":timestamp,
        "type":5
    },separators=(',',':'))
    response = await make_mai_request(api, data, user_id)
    return response
