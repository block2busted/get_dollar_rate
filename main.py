from twirp.asgi import TwirpASGIApp
from twirp.exceptions import InvalidArgument

from proto_package import get_dollar_rate_pb2, get_dollar_rate_twirp
from use_cases.get_dollar_rate import get_dollar_rate


class GetDollarService(object):
    async def GetDollarRate(self, context, size):
        response = await get_dollar_rate()
        return get_dollar_rate_pb2.GetDollarResponse(
            value_rate=response
        )


app = TwirpASGIApp()
app.add_service(
    get_dollar_rate_twirp.GetDollarServicesServer(service=GetDollarService())
)
