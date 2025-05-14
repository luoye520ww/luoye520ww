import json
from .make_mai_requests import make_mai_request

async def getscore(user_id):
    api = "GetUserMusicApiMaimaiChn"
    data = json.dumps({
        'userId':user_id,
        'maxCount':2147483647,
        'nextIndex':0,
    },separators=(',',':'))
    response = await make_mai_request(api, data, user_id)
    return response
