

from .utils import *
from .api import ApiClient
import aiohttp,aiohttp_proxy
import asyncio


class Generator:
    

    async def get_promo_code(self, GAME:Game|str,proxy_url:str=None,max_attempts: int=20):
        """## param:
           * GAME => type Game OR type str promo_id
        """
        
        
        if  isinstance(GAME,str) :
            GAME=Games().GET(promo_id=GAME)
        
        
        if not GAME.promo_id:
            return
        
        
        PromoCodes=GAME.PromoCodes()
        
        new_keys=[]
       
        attempts=1
        headers = {"Content-Type": "application/json; charset=utf-8","Host": "api.gamepromo.io"}
        proxy_conn = aiohttp_proxy.ProxyConnector().from_url(proxy_url) if proxy_url else None
        async with aiohttp.ClientSession(headers=headers, connector=proxy_conn) as http_client:
            client=ApiClient(http_client,GAME)
            
            while True:
                
                    login=await client.login_client()
                    if login:
                        while attempts <= max_attempts:
                            logger.info(f" Sleep <lw>{GAME.event_timeout}s</lw> before <lr>{attempts}</lr> attempt to get promo code for <m>{GAME.name}</m>")
                            await asyncio.sleep(delay=GAME.event_timeout)
                            try:
                                has_code =await client.register_event()
                                if has_code:
                                    
                                    await asyncio.sleep(2)
                                    promo_code =await client.create_code()
                                    if promo_code:
                                        logger.success(f" Promo code is found in <m>{GAME.name}</m>: <lc>{promo_code}</lc>")
                                        PromoCodes.insert_one(promo_code,GAME.name)
                                        new_keys.append(promo_code)
                                        
                                        return promo_code
                                        
                            except Exception as error:
                                logger.error(f" <r>{GAME.name}</r> | Error while getting promo code: {error}")

                            attempts += 1

    
    async def get_all_geme_keys(self,proxy_url:str=None,max_attempts: int = 20):

        tasks=[ self.get_promo_code(game,proxy_url,max_attempts=max_attempts) for game in Games().ALL()]
        await asyncio.gather(*tasks)
       
        

