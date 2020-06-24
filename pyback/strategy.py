import logging

log = logging.getLogger(__name__)

import itertools
from typing import Union, List, Callable, Optional


class Strategy:
    """Holds the trading algorithm. A strategy consumes data feeds
    and returns trading orders.

    Args:
        name: the name of the strategy
    """

    def __init__(self, name: str):

        log.info(f"Initiating Strategy. name={name}")

        self.name = name
        self.feed = list()
        self.algo = None
        self.orders = list()
        self.order_counter = itertools.count(1)

    def subscribe(self, feed_id: Union[str, List[str]]):
        """Subscribes to data feed

        Args:
            feed_id: A single, or a list of ``feed_id`` to subscribe to.
        """

        if type(feed_id) == str:
            log.debug(f"Converting feed_id to list. feed_id={feed_id}")
            feed_id = [feed_id]

        log.info(f"Adding feed. feed_id={feed_id}")
        self.feed += feed_id

    def set_algo(self, algo: Callable):
        """Sets the strategy's trading algorithm.

        Args:
            algo: An algorithm which consumes data feed and produces
                trading signals
        """

        log.info(f"Setting algorithm for strategy. name={self.name}")
        self.algo = algo

    def order(
        self,
        security_id: str,
        weight: float,
        limit: Optional[float] = None,
        stop: Optional[float] = None,
    ) -> str:
        """Creates a trade order

        Args:
            security: unique identifier of the security to trade
            weight: amount to order, as a percentage of the portfolio value;
                If ``weight`` is positive, this means the weight of the security
                to buy. Otherwise it means the the weight of the security to sell.
            limit: The limit price of the order. Defaults to None.
            stop: The stop price of the order. Defaults to None.

        Returns:
            str: a unique identifier of the order
        """

        order_id = f"{self.name}_{next(self.order_counter)}"

        order = {
            "order_id": order_id,
            "security_id": security_id,
            "weight": weight,
            "limit": limit,
            "stop": stop,
        }

        log.info(f"Adding order. order={order}")
        self.orders.append(order)

        return order_id
