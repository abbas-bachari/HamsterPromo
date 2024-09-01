[![HamsterPromo](https://img.shields.io/badge/HamsterPromo%20-Version%201.0.0-green?style=plastic&logo=codemagic)](https://python.org)




# Hamster Kombat Promo Code Generator





## Installation guide

Install from source:
``` bash
pip install git+https://github.com/abbas-bachari/HamsterPromo.git
```



<!-- ## user manual -->

##  Generate a key 

```python
from HamsterPromo.utils import Games
import asyncio



async def main():
    app=Generator()
    games=Games()
    Zoopolis=games.GET(name='Zoopolis')
    proxy='http://127.0.0.1:10809'
    promo_key=await app.get_promo_code(GAME=Zoopolis,proxy_url=proxy,max_attempts=20)
    print(promo_key)


if __name__=="__main__":
    asyncio.run(main())

```
 



### Generate a key for all games

```python
from HamsterPromo import Generator
import asyncio



async def main():
    app=Generator()
    proxy='http://127.0.0.1:10809'
    await app.get_all_geme_keys(proxy_url=proxy,max_attempts=20)
    


if __name__=="__main__":
    asyncio.run(main())

```



#
### Get saved key

```python
from HamsterPromo.utils import Games

games=Games()

game=games.GET(name='Polysphere')

saved_keys=game.PromoCodes()

one_key=saved_keys.get_one().code
print(one_key)
# one_key: POLY-YB4-VR4D-XP7A-DH3

all_keys= [key.code for key in saved_keys.get_many()] 
print(all_keys)
# all_keys: ['POLY-YA3-DH1V-XWPX-TD2', 'POLY-YB4-VR4D-XP7A-DH3',...]

```
#
### Delete saved keys

```python
from HamsterPromo.utils import Games

games=Games()

game=games.GET(name='Polysphere')

saved_keys=game.PromoCodes()

promo_code='POLY-YB4-VR4D-XP7A-DH3'

# DELETE ONE KEY
result =saved_keys.delete_data(code=promo_code)

# DELETE ALL SAVED KEYS
result =saved_keys.delete_data(code='all')

```
Powered by [Abbas Bachari](https://github.com/abbas-bachari).
