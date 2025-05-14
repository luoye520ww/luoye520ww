import json
from .make_mai_requests import make_mai_request

async def get_user_preview(user_id:int):
    data = json.dumps({'userId': user_id})
    api = 'GetUserPreviewApiMaimaiChn'
    response = await make_mai_request(api, data, user_id)
    return response
