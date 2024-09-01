import json



class settings:
    promo_db_path:str='promo_data.db'
    games=[
    {
        "promo_id": "b2436c89-e0aa-4aed-8046-9b0515e1c46b",
        "app_token": "b2436c89-e0aa-4aed-8046-9b0515e1c46b",
        "name": "Zoopolis",
        "event_timeout": 21
    },
    {
        "promo_id": "c7821fa7-6632-482c-9635-2bd5798585f9",
        "app_token": "b6de60a0-e030-48bb-a551-548372493523",
        "name": "Gangs Wars",
        "event_timeout": 31
    },
    {
        "promo_id": "bc0971b8-04df-4e72-8a3e-ec4dc663cd11",
        "name": "Cafe Dash",
        "app_token": "bc0971b8-04df-4e72-8a3e-ec4dc663cd11",
        "event_timeout": 31
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
    }
    ]
    
    def __init__(self) -> None:
        # options=['sessions_path','lang_code','system_lang_code']
        file_exist=False
        try:
            settings=json.load(open('settings.json',encoding='utf-8'))
            if isinstance(settings,dict):
                self.__dict__.update(settings)
                file_exist=True
        except :
            pass
        if not file_exist:
            with open('settings.json','w',encoding='utf-8') as save:
                settings_dict={
                                "promo_db_path":'promo_data.db',
                                "games":self.games
                                }
                json.dump(settings_dict,save,ensure_ascii=False,indent=4)
    
Settings=settings()
