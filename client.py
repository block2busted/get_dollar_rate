from twirp.context import Context
from twirp.exceptions import TwirpServerException

from proto_package import get_dollar_rate_pb2, get_dollar_rate_twirp


client = get_dollar_rate_twirp.GetDollarServicesClient('http://localhost:8080')

try:
    response = client.GetDollarRate(ctx=Context(), request=get_dollar_rate_pb2.GetDollarRequest())
    print(response)
except TwirpServerException as e:
    print(e.code, e.message, e.meta, e.to_dict())
