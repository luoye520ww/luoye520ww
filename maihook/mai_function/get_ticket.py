import datetime
import json
import pytz

from .user_login_logout import login, logout
from .make_mai_requests import make_mai_request
from ..constant.config_loader import mai_config

async def get_ticket(user_id:int, chargeId:int):
    time = int(datetime.now(pytz.timezone('Asia/Shanghai')).timestamp())
    api = 'UpsertUserChargelogApiMaimaiChn'
    data = json.dumps({
    "userId":user_id ,
    "userChargelog": {
        "chargeId": chargeId,
        "price": 0,
        "purchaseDate": "2024-05-13 17:40:17.0",
        "playCount": 6,
        "playerRating": 4855,
        "regionId":mai_config["regionId"],
        "placeId":mai_config["placeId"],
        "clientId":mai_config["clientId"],
    },
    "userCharge": {
        "chargeId": chargeId,
        "stock": 1,
        "purchaseDate": "2024-05-13 17:40:17.0",
        "validDate": "2025-08-11 04:00:00"
    }
},separators=(',',':'))
    login_res = await login(user_id, time)
    login_code = json.loads(login_res).get('returnCode')
    if login_code == 100:
        await logout(user_id, time)
        return '账号未登出'
    elif login_code == 102:
        return '未获取二维码'
    elif login_code == 1:
        pass
    response = await make_mai_request(api, data, user_id)
    ticket_code = json.loads(response).get('returnCode')
    if ticket_code == 1:
        msg = '获取成功'
    else:
        msg = '获取失败，号上可能还有未使用的'    
    await logout(user_id, time)
    return msg
