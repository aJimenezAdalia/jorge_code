

import requests
import json
import logging
from datetime import datetime

today = datetime.now()

logger = logging.getLogger()

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

if str(response) == '<Response [200]>':
    logger.info('Response 200. OK')

    text_response = response.text
    dict_response = json.loads(response.text)

    eur_price = dict_response.get('bpi').get('EUR').get('rate_float')
    usd_price = eur_price - 1.08
    print(eur_price)

else:
    logger.error(response)

def send_mail(email):
    return 'Data successfully loaded'
