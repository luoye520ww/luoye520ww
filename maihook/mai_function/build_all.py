import json

from .make_mai_requests import make_mai_request
from ..constant.config_loader import mai_config
from .get_api import get_api


async def build_all(user_id, userdata, logid, ftime, ):
    extend_info = await get_api("GetUserExtendApiMaimaiChn", user_id)
    extend = Data.input(json.loads(extend_info).get("userExtend"))
    
    option_info = await get_api("GetUserOptionApiMaimaiChn",user_id)
    option = Data.input(json.loads(option_info).get("userOption"))
    
    rating_info = await get_api("GetUserRatingApiMaimaiChn",user_id)
    rating = json.loads(rating_info).get("userRating")
    udemae = Data.input(rating.get('udemae'))
    s_udemae = {
        "rate": udemae.rate,
        "maxRate": udemae.maxRate,
        "classValue": udemae.classValue,
        "maxClassValue": udemae.maxClassValue,
        "totalWinNum": udemae.totalWinNum,
        "totalLoseNum": udemae.totalLoseNum,
        "maxWinNum": udemae.maxWinNum,
        "maxLoseNum": udemae.maxLoseNum,
        "winNum": udemae.winNum,
        "loseNum": udemae.loseNum,
        "npcTotalWinNum": udemae.npcTotalWinNum,
        "npcTotalLoseNum": udemae.npcTotalLoseNum,
        "npcMaxWinNum": udemae.npcMaxWinNum,
        "npcMaxLoseNum": udemae.npcMaxLoseNum,
        "npcWinNum": udemae.npcWinNum,
        "npcLoseNum": udemae.npcLoseNum
    }
    rating["udemae"] = s_udemae
    
    activity_info = await get_api("GetUserActivityApiMaimaiChn",user_id)
    activity = json.loads(activity_info).get("userActivity")
    
    charge_info = await get_api("GetUserChargeApiMaimaiChn",user_id)
    charge = json.loads(charge_info).get("userChargeList",[])
    new_charge =[]
    try:
        for t in charge:
            del t['extNum1']
            new_charge.append(t)
    except:
        pass
    charge = new_charge

    data ={
    "userId": user_id,
    "playlogId": logid,
    "isEventMode": False,
    "isFreePlay": False,
    "upsertUserAll": {
        "userData": [
            {
                "accessCode": "",
                "userName": userdata.userName,
                "isNetMember": 1,
                "iconId": userdata.iconId,
                "plateId": userdata.plateId,
                "titleId": userdata.titleId,
                "partnerId": userdata.partnerId,
                "frameId": userdata.frameId,
                "selectMapId": userdata.selectMapId,
                "totalAwake": userdata.totalAwake,
                "gradeRating": userdata.gradeRating,
                "musicRating": userdata.musicRating,
                "playerRating": userdata.playerRating,
                "highestRating": userdata.highestRating,
                "gradeRank": userdata.gradeRank,
                "classRank": userdata.classRank,
                "courseRank": userdata.courseRank,
                "charaSlot": userdata.charaSlot,
                "charaLockSlot": userdata.charaLockSlot,
                "contentBit": userdata.contentBit,
                "playCount": userdata.playCount,
                "currentPlayCount": userdata.currentPlayCount,
                "renameCredit": 0,
                "mapStock": userdata.mapStock,
                "eventWatchedDate": userdata.eventWatchedDate + ".0",
                "lastGameId": "SDGB",
                "lastRomVersion": userdata.lastRomVersion,
                "lastDataVersion": userdata.lastDataVersion,
                "lastLoginDate": ftime + ".0",
                "lastPlayDate": ftime + ".0",
                "lastPlayCredit": 1,
                "lastPlayMode": 0,
                "lastPlaceId": 2120,
                "lastPlaceName": userdata.lastPlaceName,
                "lastAllNetId": userdata.lastAllNetId,
                "lastRegionId": userdata.lastRegionId,
                "lastRegionName": userdata.lastRegionName,
                "lastClientId": userdata.lastClientId,
                "lastCountryCode": userdata.lastCountryCode,
                "lastSelectEMoney": 0,
                "lastSelectTicket": 0,
                "lastSelectCourse": userdata.lastSelectCourse,
                "lastCountCourse": userdata.lastCountCourse,
                "firstGameId": userdata.firstGameId,
                "firstRomVersion": userdata.firstRomVersion,
                "firstDataVersion": userdata.firstDataVersion,
                "firstPlayDate": userdata.firstPlayDate,
                "compatibleCmVersion": userdata.compatibleCmVersion,
                "dailyBonusDate": userdata.dailyBonusDate,
                "dailyCourseBonusDate": userdata.dailyCourseBonusDate,
                "lastPairLoginDate": userdata.lastPairLoginDate,
                "lastTrialPlayDate": userdata.lastTrialPlayDate,
                "playVsCount": userdata.playVsCount,
                "playSyncCount": userdata.playSyncCount,
                "winCount": userdata.winCount,
                "helpCount": userdata.helpCount,
                "comboCount": userdata.comboCount,
                "totalDeluxscore": userdata.totalDeluxscore,
                "totalBasicDeluxscore": userdata.totalBasicDeluxscore,
                "totalAdvancedDeluxscore": userdata.totalAdvancedDeluxscore,
                "totalExpertDeluxscore": userdata.totalExpertDeluxscore,
                "totalMasterDeluxscore": userdata.totalMasterDeluxscore,
                "totalReMasterDeluxscore": userdata.totalReMasterDeluxscore,
                "totalSync": userdata.totalSync,
                "totalBasicSync": userdata.totalBasicSync,
                "totalAdvancedSync": userdata.totalAdvancedSync,
                "totalExpertSync": userdata.totalExpertSync,
                "totalMasterSync": userdata.totalMasterSync,
                "totalReMasterSync": userdata.totalReMasterSync,
                "totalAchievement": userdata.totalAchievement,
                "totalBasicAchievement": userdata.totalBasicAchievement,
                "totalAdvancedAchievement": userdata.totalAdvancedAchievement,
                "totalExpertAchievement": userdata.totalExpertAchievement,
                "totalMasterAchievement": userdata.totalMasterAchievement,
                "totalReMasterAchievement": userdata.totalReMasterAchievement,
                "playerOldRating": userdata.playerOldRating,
                "playerNewRating": userdata.playerNewRating,
                "banState": 0,
                "dateTime": userdata.dateTime
            }
        ],
        "userExtend": [
            {
                "selectMusicId": extend.selectMusicId,
                "selectDifficultyId": extend.selectDifficultyId,
                "categoryIndex": extend.categoryIndex,
                "musicIndex": extend.musicIndex,
                "extraFlag": extend.extraFlag,
                "selectScoreType": extend.selectScoreType,
                "extendContentBit": extend.extendContentBit,
                "isPhotoAgree": False,
                "isGotoCodeRead": False,
                "selectResultDetails": extend.selectResultDetails,
                "selectResultScoreViewType": extend.selectResultScoreViewType,
                "sortCategorySetting": extend.sortCategorySetting,
                "sortMusicSetting": extend.sortMusicSetting,
                "playStatusSetting": extend.playStatusSetting,
                "selectedCardList": [],
                "encountMapNpcList": []
            }
        ],
        "userOption": [
            {
                "optionKind": option.optionKind,
                "noteSpeed": option.noteSpeed,
                "slideSpeed": option.slideSpeed,
                "touchSpeed": option.touchSpeed,
                "tapDesign": option.tapDesign,
                "holdDesign": option.holdDesign,
                "slideDesign": option.slideDesign,
                "starType": option.starType,
                "outlineDesign": option.outlineDesign,
                "noteSize": option.noteSize,
                "slideSize": option.slideSize,
                "touchSize": option.touchSize,
                "starRotate": option.starRotate,
                "dispCenter": option.dispCenter,
                "outFrameType": option.outFrameType,
                "dispChain": option.dispChain,
                "dispRate": option.dispRate,
                "dispBar": option.dispBar,
                "touchEffect": option.touchEffect,
                "submonitorAnimation": option.submonitorAnimation,
                "submonitorAchive": option.submonitorAchive,
                "submonitorAppeal": option.submonitorAppeal,
                "matching": option.matching,
                "trackSkip": option.trackSkip,
                "brightness": option.brightness,
                "mirrorMode": option.mirrorMode,
                "dispJudge": option.dispJudge,
                "dispJudgePos": option.dispJudgePos,
                "dispJudgeTouchPos": option.dispJudgeTouchPos,
                "adjustTiming": option.adjustTiming,
                "judgeTiming": option.judgeTiming,
                "ansVolume": option.ansVolume,
                "tapHoldVolume": option.tapHoldVolume,
                "criticalSe": option.criticalSe,
                "tapSe": option.tapSe,
                "breakSe": option.breakSe,
                "breakVolume": option.breakVolume,
                "exSe": option.exSe,
                "exVolume": option.exVolume,
                "slideSe": option.slideSe,
                "slideVolume": option.slideVolume,
                "breakSlideVolume": option.breakSlideVolume,
                "touchVolume": option.touchVolume,
                "touchHoldVolume": option.touchHoldVolume,
                "damageSeVolume": option.damageSeVolume,
                "headPhoneVolume": option.headPhoneVolume,
                "sortTab": option.sortTab,
                "sortMusic": option.sortMusic
            }
        ],
        "userCharacterList": [],
        "userGhost": [],
        "userMapList": [],
        "userLoginBonusList": [],
        "userRatingList": [rating],
        "userItemList": [],
        "userMusicDetailList": [{"musicId": 0,"level": 0,"playCount": 1,"achievement": 0,"comboStatus": 0,"syncStatus": 0,"deluxscoreMax": 0,"scoreRank": 0,"extNum1": 0}],
        "userCourseList": [],
        "userFriendSeasonRankingList": [],
        "userChargeList": charge,
        "userFavoriteList": [],
        "userActivityList": [activity],
        "userGamePlaylogList": [
            {
                "playlogId": logid,
                "version": "1.41.00",
                "playDate": ftime + ".0",
                "playMode": 0,
                "useTicketId": -1,
                "playCredit": 1,
                "playTrack": 1,
                "clientId": mai_config["clientId"],
                "isPlayTutorial": False,
                "isEventMode": False,
                "isNewFree": False,
                "playCount": 56,
                "playSpecial": 1614394056,
                "playOtherUserId": 0
            }
        ],
        "user2pPlaylog": {
            "userId1": 0,
            "userId2": 0,
            "userName1": "",
            "userName2": "",
            "regionId": 0,
            "placeId": 0,
            "user2pPlaylogDetailList": []
        },
        "isNewCharacterList": "",
        "isNewMapList": "",
        "isNewLoginBonusList": "",
        "isNewItemList": "",
        "isNewMusicDetailList": "0",
        "isNewCourseList": "",
        "isNewFavoriteList": "",
        "isNewFriendSeasonRankingList": ""
    }
}
    return data

async def upsert_all(user_id, all_data):
    api = "UpsertUserAllApiMaimaiChn"
    response = await make_mai_request(
        api, 
        all_data, 
        user_id,
        aes_key= mai_config["aesKey"],
        aes_iv= mai_config["aesIV"]
    )
    return response