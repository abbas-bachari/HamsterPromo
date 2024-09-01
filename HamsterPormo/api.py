


from .utils import *
import asyncio
import aiohttp
class ApiClient:
    def __init__(self,http_client:aiohttp.ClientSession,GAME:Game):
        self.http_client=http_client
        self.GAME=GAME
    
    
    async def login_client(self):
        response_text=''
        try:
            client_id = generate_client_id()
            json_data = {"appToken": self.GAME.app_token,"clientId": client_id,"clientOrigin": "deviceid"}
            response = await self.http_client.post(url="https://api.gamepromo.io/promo/login-client", json=json_data)
            response_text=await response.text()
            response_json = json.loads(response_text)
            access_token = response_json.get("clientToken")
            if not access_token:
                error_code=response_json.get("error_code",'error')         
                error_text=response_json.get("error_message")
                if not error_text:
                    error_text=escape_html(response_text)[:256]
                    
                logger.error(f" <lr>{self.GAME.name:<14}</lr> | Error while login : {error_text}...")
                if error_code=="TooManyIpRequest":
                    ss=60*3
                    logger.info(f" Sleep <lw>{ss}s</lw> before retray ...")
                    await asyncio.sleep(delay=ss)
                return

            self.http_client.headers["Authorization"] = f"Bearer {access_token}"
            return True
        except Exception as error:
            logger.error(f' <lr>{self.GAME.name:<14}</lr> | Error while login: {error} | Response text: {escape_html(response_text)[:256]}...')
            await asyncio.sleep(3)
        
    async def register_event(self):
        response_text=''
        try:
            event_id = generate_event_id()
            json_data = {"promoId": self.GAME.promo_id,"eventId": event_id,"eventOrigin": "undefined"}
            response = await self.http_client.post(url="https://api.gamepromo.io/promo/register-event", json=json_data)
            response_text=await response.text()
            response_json = json.loads(response_text)
            has_code = response_json.get("hasCode", False)
            return has_code
        except Exception as error:
            logger.error(f' <lr>{self.GAME.name:<14}</lr> | Error while Register event: {error} | Response text: {escape_html(response_text)[:256]}...')
            await asyncio.sleep(3)
    async def create_code(self):
        response_text=''
        try:
            json_data = {"promoId": self.GAME.promo_id}
            response = await self.http_client.post(url="https://api.gamepromo.io/promo/create-code", json=json_data)
            response_text=await response.text()
            response_json = json.loads(response_text)
            promo_code = response_json.get("promoCode")
            return promo_code

        except Exception as error:
            logger.error(f' <lr>{self.GAME.name:<14}</lr> | Error while Create code: {error} | Response text: {escape_html(response_text)[:256]}...')
            await asyncio.sleep(3)
        
