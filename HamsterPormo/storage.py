
import sqlite3,json,re
from datetime import datetime , timedelta
from .settings import Settings


class FetchType:
    FETCH_ONE    = "ONE"
    FETCH_MULTI  = "MUTI"
    FETCH_COUNT  = "COUNT"

def data_convertor(string:str):
    
    if type(string)==str:
        string=string.strip()
        if string.upper() in ["YES","NO"]:
            return True if string.upper()=="YES" else  False
        
        date_time = re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', string)
        if date_time:
            return datetime.fromisoformat(string) 
        
        
        timer = re.compile(r'^(\d{2})\s*:\s*(\d{2})\s*:\s*(\d{2})$').search(string)
        if timer:
            hour, minute, second = timer.groups()
            return timedelta(hours=int(hour),minutes=int(minute),seconds=int(second))
    
    
    return string           

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        
        if isinstance(obj, timedelta):
            hour=  obj.seconds // 3600
            minute=obj.seconds %  3600 // 60
            second=obj.seconds %  60
            if obj.days > 0:
                hour+=obj.days*24

            return f"{hour:0>2}:{minute:0>2}:{second:0>2}"
        return json.JSONEncoder.default(self, obj)


fild_list=["code","name"]
class PromoCode:
    name:str
    code:str
    

    def __init__(self, data:dict):
        self.has_data=False
        self.data_dict={}
        if data and type(data)==dict:
            for k,v in data.items():
                if k not in fild_list:continue
                cv=data_convertor(v)
                self.data_dict[k]=cv
                self.__dict__[k]=cv
            self.has_data=True

    def to_json_str(self):
        return json.dumps(self.data_dict,indent=4,ensure_ascii=False,cls=DateTimeEncoder)
        
    def __str__(self) -> str:
        return self.to_json_str()


class Storage:
    
    def __init__(self,tb_name):
        self._db_name=Settings.promo_db_path
        self._tb_name=tb_name

    def __quary(self,quary_string:str,values:str='',fetch_type:FetchType=FetchType.FETCH_COUNT,execute_many:bool=False):
        def dict_factory(cursor, row):
            sqd = {}
            for idx, col in enumerate(cursor.description):
                sqd[col[0]] = row[idx]
            return sqd
        
        conn=sqlite3.connect(self._db_name)
        conn.row_factory =dict_factory
        cursor= conn.cursor()
        
        cursor.executemany(quary_string,values) if execute_many else cursor.execute(quary_string,values)
        
        if fetch_type==FetchType.FETCH_MULTI:
            data=cursor.fetchall()
        elif fetch_type==FetchType.FETCH_ONE:
            data=cursor.fetchone()
        else:
            data=cursor.rowcount
        
            

        conn.commit()
        cursor.close()
        conn.close()

        return  data 
        


    def insert_one(self,code:str,name:str)->int:
        data=self.__quary(f"INSERT OR IGNORE INTO [{self._tb_name}] (code,name) VALUES(?,?)",[code,name])
        return data
        
    
    
    def insert_many(self,list_cods:list)->int:
        '''
        ### list_code: 
            [[code-1],[code-2],[code-3],...]
        
        '''
        data=self.__quary(f"INSERT OR IGNORE INTO [{self._tb_name}] (code) VALUES(?)",list_cods,execute_many=True)
        return data
    
    def get_one(self,random:bool=False) -> PromoCode:
        randoming="ORDER BY RANDOM()" if random else ""
        data=self.__quary(f"SELECT * FROM [{self._tb_name}] {randoming};",fetch_type=FetchType.FETCH_ONE)
        return PromoCode(data)
    
    def get_many(self,limit=0)->list[PromoCode]:
        lmt=f"LIMIT {limit}" if limit else ''
        data=self.__quary(f"SELECT * FROM [{self._tb_name}] {lmt};",fetch_type=FetchType.FETCH_MULTI)
        return [PromoCode(i) for i in data] if data else []
   



    def delete_data(self,code:str)->int:
        if code.upper()=='ALL':
            return self.__quary(f"DELETE FROM [{self._tb_name}];")

        return self.__quary(f"DELETE FROM [{self._tb_name}]  WHERE code=?",code)
        
    

    
    def create_table(self,name:str):
        table_data=f'''
                    code      TEXT PRIMARY KEY NOT NULL,
                    name       TEXT   DEFAULT '{name}'
                    
                    '''
        
        self.__quary(f'CREATE TABLE IF NOT EXISTS [{self._tb_name}] ({table_data});')
       
        return self

    def check_exist_table(self,tbname)->bool:
        data=self.__quary(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tbname}';",fetch_type=FetchType.FETCH_ONE)
        return True if data else False
    
    def get_count(self) -> int:
        result=self.__quary(f"SELECT COUNT(*) FROM [{self._tb_name}];",fetch_type=FetchType.FETCH_ONE)
        return  result.get('COUNT(*)',0) if result else 0
   



