from twirp.asgi import TwirpASGIApp

from valutes_protobuf import get_dollar_rate_twirp

from use_cases.get_dollar_rate import get_dollar_rate


class GetDollarService:

    async def GetDollarRate(self, context, size):
        response = await get_dollar_rate()
        return response


app = TwirpASGIApp()
app.add_service(
    get_dollar_rate_twirp.GetRateServer(service=GetDollarService())
)
