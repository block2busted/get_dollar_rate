import aiohttp

import xmltodict
import json
from .constants import DOLLAR_ID

from valutes_protobuf import get_dollar_rate_pb2


async def get_dollar_rate() -> get_dollar_rate_pb2.GetDollarRateResponse:
    async with aiohttp.ClientSession() as session:
        async with session.get(
                'http://www.cbr.ru/scripts/XML_daily.asp'
        ) as response:
            body = await response.text()
            json_body = json.loads(
                json.dumps(
                    xmltodict.parse(
                        body,
                        process_namespaces=True
                    ),
                    indent=2
                )
            )

            dollar_rate = {
                valute['@ID']: valute['Value']
                for valute
                in json_body['ValCurs']['Valute']
            }[DOLLAR_ID]
            return get_dollar_rate_pb2.GetDollarRateResponse(
                value_rate=float(dollar_rate.replace(',', '.'))
            )
