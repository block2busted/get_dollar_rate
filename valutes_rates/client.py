from twirp.context import Context
from twirp.exceptions import TwirpServerException

from valutes_protobuf import get_dollar_rate_pb2, get_dollar_rate_twirp

from settings import GRPC_HOST, GRPC_PORT


client = get_dollar_rate_twirp.GetRateClient(
    address=f'{GRPC_HOST}:{GRPC_PORT}'
)

try:
    response = client.GetDollarRate(
        ctx=Context(),
        request=get_dollar_rate_pb2.GetDollarRateRequest()
    )
    print(response)
except TwirpServerException as e:
    print(f'Code: {e.code}\n')
    print(f'Message {e.message}\n')
    print(f'Meta: {e.meta}\n')
    print(e.to_dict())
    print()
