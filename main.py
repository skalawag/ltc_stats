#! /usr/bin/env python

import logging
import sys

from stats_app.ticker_store import TickerStore, MiningHistoryStore, TradeStore, GPUStore, MinerPoolStore
from stats_app.settings import API_URL, POOL, TRADE_API_URL

log = logging.getLogger(__name__)

if __name__ == "__main__":
    # try:
    #     mstore = MiningHistoryStore(POOL)
    #     mstore.save()
    # except:
    #     e = sys.exc_info()[0]
    #     log.error("Unable to save MiningHistory. %s" % e)
    #     raise

    # try:
    #     tstore = TickerStore(API_URL)
    #     tstore.save()
    # except:
    #     e = sys.exc_info()[0]
    #     log.error("Unable to save Ticker. %s" % e)

    # try:
    #     tradestore = TradeStore(TRADE_API_URL)
    #     tradestore.save()
    # except:
    #     e = sys.exc_info()[0]
    #     log.error("Unable to save Trade. %s" % e)

    try:
        gpustore = GPUStore('stats')
        gpustore.save()
    except:
        e = sys.exc_info()[0]
        log.error("Unable to save GPU stats. %s" % e)

        #    try:
    poolstore = MinerPoolStore('stats')
    poolstore.save()
    # except:
    #     e = sys.exc_info()[0]
    #     log.error("Unable to save Miner pool stats. %s" % e)
