API_URL = "https://btc-e.com/api/2/ltc_usd/ticker"
MINING_API_URL = ""
TRADE_API_URL = "https://btc-e.com/api/2/ltc_usd/trades"

import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(PROJECT_ROOT, '../ticker.db')

DATABASE = {'drivername': 'sqlite',  # postgresql
            'database': DB_PATH}
            # 'host': '',
            # 'port': '',
            # 'username': '',
            # 'password': ''}


try:
    from local_settings import *
except ImportError, exp:
    pass
