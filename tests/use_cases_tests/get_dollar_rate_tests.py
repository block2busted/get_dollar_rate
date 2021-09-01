import os
from aioresponses import aioresponses
from valutes_protobuf.get_dollar_rate_pb2 import GetDollarRateResponse

from valutes_rates.use_cases.get_dollar_rate import get_dollar_rate


async def test_valid_response():
    with aioresponses() as mocked:
        with open(
                f'{os.path.dirname(__file__)}/responses/get_dollar_rate.xml',
                mode='r',
                encoding='windows-1251'
        ) as xml_file:
            data = xml_file.read()

        mocked.get(
            'http://www.cbr.ru/scripts/XML_daily.asp',
            content_type='application/xml',
            body=data
        )
        dollar_rate = await get_dollar_rate()

        assert isinstance(dollar_rate.value_rate, float)
        assert dollar_rate == GetDollarRateResponse(
            value_rate=55.278099060058594
        )
