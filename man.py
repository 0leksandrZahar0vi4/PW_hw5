import asyncio
from datetime import datetime, timedelta
import httpx
import platform
import sys
import tabulate

class HttpError(Exception):
    pass


async def request(url: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
       # test = await client.get('https://www.google.com')
        # print(test.text)
        if r.status_code == 200:
            result = r.json()
            return result
        else:
            raise HttpError(f"Error status: {r.status_code} for {url}")


async def exchange_currency(result: dict, currensy: str):
    currensy = await input("Enter currensy: ")
    async for key, valume in result.items():
        
            if isinstance(valume, list):
                for val in valume:
                    if isinstance(val, dict):
                        for valum in val.values():
                            if currensy==valum:
                                valu = val # dict
                                for kk, vv in valu.items():
                                    valu[kk]=str(vv).split()
                                    head = ["baseCurrency", "currency", "sale", "purchase"]
                                    data = await tabulate(valu, headers=head, tablefmt="grid")
                                    print(data)
            
                                
        
        

async def main(index_day):
    date_new = datetime.now() - timedelta(days=int(index_day))
    date_ques = date_new.strftime("%d.%m.%Y")
    print(date_ques)
    try:
        response = await request(f'https://api.privatbank.ua/p24api/exchange_rates?date={date_ques}')
        return response
    except HttpError as err:
        print(err)
        return None


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main(sys.argv[1]))
    # rr = exchange_currency(result=r)
    print(r)
