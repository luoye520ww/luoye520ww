from datetime import datetime, timezone, timedelta
import json
from ..constant.config_loader import mai_config
from .make_mai_requests import get_api, login, logout
from .build_all import build_all
from .build_log import build_log
from .user_login_logout import upsert_all
from .user_login_logout import Data
from .user_login_logout import get_api

async def del_music(music_id, userid, level):
    now = datetime.now(timezone(timedelta(hours=8)))
    time = int(now.timestamp())
    ftime = now.strftime("%Y-%m-%d %H:%M:%S")
    ftime2 = now.strftime("%Y-%m-%d")
    
    login_info = await login(userid,time)
    returncode = json.loads(login_info).get("returnCode")
    if returncode == 100:
        await logout(userid,time)
        return "账号未登出\n若您确定您拉了那请再尝试一次命令"
    elif returncode == 102:
        await logout(userid,time)
        return "未拉取二维码"
    elif returncode == 1:
        pass
    else:
        return f"未知错误 login returnCode:{returncode}"
    login_id=json.loads(login_info).get("loginId")

    data_info = await get_api("GetUserDataApiMaimaiChn",userid)
    data = json.loads(data_info).get("userData")
    data["accessCode"]=""
    data["friendCode"]=""
    data["dateTime"]=time
    data["lastGameId"]="SDGB"
    data["lastAllNetId"]=0
    data["lastRegionId"]=mai_config["regionId"]
    data["lastRegionName"]="广东"
    data["lastCountryCode"]="CHN"
    data["lastPlaceName"]=mai_config["PlaceName"]
    data["lastClientId"]=mai_config["clientId"]
    data["eventWatchedDate"]=ftime
    data["lastLoginDate"]=ftime
    data["lastPlayDate"]=ftime

    userdata = Data.input(data)
    
    all = await build_all(userid,userdata,login_id,ftime)
    all["upsertUserAll"]["userMusicDetailList"] = [{"musicId": music_id,"level": level,"playCount": 1,"achievement": 0,"comboStatus": 0,"syncStatus": 0,"deluxscoreMax": 0,"scoreRank": 0,"extNum1": 0}]
    all["upsertUserAll"]["isNewMusicDetailList"] = "0"
    all = json.dumps(all,ensure_ascii=False)

    music_log = await build_log(userid,login_id,time,ftime,ftime2,userdata)
    music_log["userPlaylog"]["musicId"] = music_id
    music_log["userPlaylog"]["level"] = level
    log_info = await get_api("UploadUserPlaylogApiMaimaiChn",userid,json.dumps(music_log))

    returncode = json.loads(log_info).get("returnCode")
    if returncode == 1:
        pass
    else:
        await logout(userid,time)
        return f"上传log失败 returnCode:{returncode}"
    
    all_info = await upsert_all(userid, all)
    returncode = json.loads(all_info).get("returnCode")
    if returncode == 1:
        pass
    else:
        await logout(userid,time)
        return f"上传all失败 returnCode:{returncode}"
 
    await logout(userid,time)
    return "善"

