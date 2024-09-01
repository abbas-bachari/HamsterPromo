from loguru import logger
import sys,uuid,random,time
from typing import Any
import json,sys
from .storage import Storage
from .settings import Settings
logger.remove()
logger.add(sink = sys.stdout, format = '<white>{time:YYYY-MM-DD HH:mm:ss}</white> | <level>{level: <8}</level>|<white><b>{message}</b></white>')
logger = logger.opt(colors = True)

# GAMES_FILE = 'games.json'
def generate_client_id():
    time_ms = int(time.time() * 1000)
    rand_num = "34" + str(random.randint(10000000000000000, 99999999999999999))
    return f"{time_ms}-{rand_num}"

def generate_event_id():
    return str(uuid.uuid4())

def escape_html(text: str) -> str:
    return text.replace('<', '\\<').replace('>', '\\>')


    
def search_in_json_list(list_data,key,search_value)->dict:
    for data in list_data:
        if data.get(key)==search_value:
            return data





class Game:
    promo_id:str
    app_token:str
    name:str
    event_timeout:int= 21
    def __init__(self,game_data:dict) -> None:
        if isinstance(game_data,dict):
            for k,v in game_data.items():
                self.__dict__[k]=v
    def PromoCodes(self):
        db=Storage(tb_name= self.promo_id) 
        db.create_table(self.name)
        return db

    
class Games:
    
    def __init__(self) -> None:
        self.__games=Settings.games
    
    def ALL(self) -> list[Game]:
        return [Game(i) for i in self.__games]

    def GET(self, index:int=-1,promo_id:str='',name:str='') -> Game:
        
        try:
           
            if  index >-1 and len(self.__games) >=index:
                return Game(self.__games[index])
            else:
                search_type=("promo_id",promo_id )if promo_id else (("name",name) if name else None)
                if search_type:
                    srh=search_in_json_list(self.__games,search_type[0],search_type[1])
                    return Game(srh)
        except:
            pass
