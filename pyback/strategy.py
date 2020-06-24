import logging
from typing import Union, List

log = logging.getLogger(__name__)


class Strategy:
    """ Holds the trading algorithm. A strategy consumes data feeds
    and returns trading orders.

    Args:
        name: the name of the strategy
    """

    def __init__(self, name: str):

        log.info(f"Initiating Strategy. name={name}")
        self.name = name
        self.feed = set()

    def subscribe(self, feed_id: Union[str, List[str]]):
        """Subscribe to data feed

        Args:
            feed_id: A single, or a list of ``feed_id`` to subscribe to.
        """

        if type(feed_id) == str:
            log.debug(f"Converting feed_id to list. feed_id={feed_id}")
            feed_id = [feed_id]

        log.info(f"Adding feed. feed_id={feed_id}")
        self.feed.update(feed_id)
