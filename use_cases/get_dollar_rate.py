import asyncio
import aiohttp

import xmltodict
import json

DOLLAR_ID = 'R01235'


async def get_dollar_rate() -> float:
    async with aiohttp.ClientSession() as session:
        async with session.get(
                'http://www.cbr.ru/scripts/XML_daily.asp'
        ) as response:
            body = await response.text()
            json_body = json.loads(
                json.dumps(
                    xmltodict.parse(body, process_namespaces=True),
                    indent=2
                )
            )

            valutes_by_id = {
                valute['@ID']: valute['Value']
                for valute
                in json_body['ValCurs']['Valute']
            }
            dollar_rate = float(valutes_by_id[DOLLAR_ID].replace(',', '.'))
            return dollar_rate


if __name__ == '__main__':
    asyncio.run(get_dollar_rate())
