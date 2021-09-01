# GetDollarRate

Service based on the [Twirp framework](https://github.com/verloop/twirpy) for obtaining information about the dollar exchange rate.
Represents an application with one async GetDollarRate method for obtaining up-to-date information about the currency rate, which refers to the public API of the Central Bank of the Russian Federation. 
The response from the API is parsed, packed into a protobuf structure and returned to the client.
Protobuf-schema compiled into python library and loaded into [PyPI](https://pypi.org/project/valutes-protobuf/).
The service is built and run in Docker.


## Functional check

Up and build the server on docker-compose.
```
mkdir get_dollar_rate
git clone https://github.com/block2busted/get_dollar_rate.git
docker-compose build
docker-compose up -d
```


Test response by Twirp-client
```python
python3 -m venv env
source env/bin/activate
pip install -r valutes_rates/requirements.txt
pip install valutes-protobuf
python3 valutes_rates/client.py  # value_rate: ***
```

For run pytest use command
```
 python -m pytest
```
