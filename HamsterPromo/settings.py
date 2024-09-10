import json,asyncio
import aiohttp,aiohttp_proxy




GAMES_DATA=[
        {
            "promo_id": "b2436c89-e0aa-4aed-8046-9b0515e1c46b",
            "app_token": "b2436c89-e0aa-4aed-8046-9b0515e1c46b",
            "name": "Zoopolis",
            "event_timeout": 21
        },
        {
            "promo_id": "ef319a80-949a-492e-8ee0-424fb5fc20a6",
            "name": "Mow and Trim",
            "app_token": "ef319a80-949a-492e-8ee0-424fb5fc20a6",
            "event_timeout": 31
        },
        {
            "promo_id": "b4170868-cef0-424f-8eb9-be0622e8e8e3",
            "name": "Chain Cube 2048",
            "app_token": "d1690a07-3780-4068-810f-9b5bbf2931b2",
            "event_timeout": 21
        },
        {
            "promo_id": "c4480ac7-e178-4973-8061-9ed5b2e17954",
            "name": "Train Miner",
            "app_token": "82647f43-3f87-402d-88dd-09a90025313f",
            "event_timeout": 121
        },
        {
            "promo_id": "dc128d28-c45b-411c-98ff-ac7726fbaea4",
            "name": "Merge Away",
            "app_token": "8d1cc2ad-e097-4b86-90ef-7a27e19fb833",
            "event_timeout": 21
        },
        {
            "promo_id": "61308365-9d16-4040-8bb0-2f4a4c69074c",
            "name": "Twerk Race",
            "app_token": "61308365-9d16-4040-8bb0-2f4a4c69074c",
            "event_timeout": 21
        },
        {
            "promo_id": "2aaf5aee-2cbc-47ec-8a3f-0962cc14bc71",
            "name": "Polysphere",
            "app_token": "2aaf5aee-2cbc-47ec-8a3f-0962cc14bc71",
            "event_timeout": 31
        },
        {
            "promo_id": "112887b0-a8af-4eb2-ac63-d82df78283d9",
            "app_token": "112887b0-a8af-4eb2-ac63-d82df78283d9",
            "name": "Fluff Crusade",
            "event_timeout": 31
        },
        {
            "promo_id": "e68b39d2-4880-4a31-b3aa-0393e7df10c7",
            "app_token": "e68b39d2-4880-4a31-b3aa-0393e7df10c7",
            "name": "Tile Trio",
            "event_timeout": 31
        },
        {
            "promo_id": "04ebd6de-69b7-43d1-9c4b-04a6ca3305af",
            "app_token": "04ebd6de-69b7-43d1-9c4b-04a6ca3305af",
            "name": "Stone Age",
            "event_timeout": 31
        }
    ]
    


async def get_games_data(proxy_url:str=None) :
    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
    "Host": "api21.datavibe.top"}
    proxy_conn = aiohttp_proxy.ProxyConnector().from_url(proxy_url) if proxy_url else None
    async with aiohttp.ClientSession(headers=headers, connector=proxy_conn) as http_client:
        try:
            response = await http_client.get('https://api21.datavibe.top/api/Games')
            response_text= await response.text()
            response_json=json.loads(response_text)
            return response_json

        except:
            pass

async def update_games_data(proxy_url:str=None):
    new_games_data  :dict=await get_games_data(proxy_url)
    try:
        settings_data :dict=json.load(open('hamster-promo-settings.json',encoding='utf-8'))
        games_data=settings_data["games"]
    except:
        settings_data={"promo_db_path": "promo_data.db"}
        games_data=GAMES_DATA


   
    if new_games_data:
        games_data=[] 
        for data in new_games_data:
            games_data.append({
                            "promo_id"  : data.get('promoId'),
                            "app_token" : data.get('appToken'),
                            "name"      : data.get('name'),
                            "event_timeout": data.get('minWaitAfterLogin')
                            })
                
    settings_data["games"]=games_data
    
    with open('hamster-promo-settings.json','w',encoding='utf-8') as save:
        json.dump(settings_data,save,indent=4,ensure_ascii=False)
    

   
    
    return settings_data



class settings:
    promo_db_path:str='promo_data.db'
    games=list[dict]
    
    def __init__(self) -> None:
        settings=asyncio.run(update_games_data())
        self.__dict__.update(settings)
               
        


Settings=settings()
