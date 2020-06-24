import logging

log = logging.getLogger(__name__)

import heapq
import itertools
from typing import Iterable, Tuple, Dict, Optional


class Feed(object):
    """Feed is a queue structure where each element is served in order of priority.

    Elements in the feed are popped based on the priority with higher priority
    elements being served before lower priority elements.  If two elements have
    the same priority, they will be served in the order they were added to the
    queue.

    Attributes:
        queue (list): Nodes added to the priority queue.
    """

    def __init__(self):
        """Initialize a new Feed."""

        self.queue = []
        self.counter = itertools.count()

    def pop(self) -> Tuple[int, Dict]:
        """
        Pop top priority data from feed.

        Returns:
            The data with the highest priority.
        """

        priorty, _count, data = heapq.heappop(self.queue)
        return priorty, data

    def __iter__(self) -> Iterable:
        """Queue iterator."""

        return iter(sorted(self.queue))

    def __str__(self) -> str:
        """Feed to string."""

        return f"Feed: {self.queue}"

    def append(self, data: Dict, priority: Optional[int] = 0):
        """
        Append a data point to the feed.

        Args:
            data: data to add to the feed.
        """

        count = next(self.counter)
        heapq.heappush(self.queue, [priority, count, data])

    def __contains__(self, key: Dict):
        """
        Containment Check operator for 'in'

        Args:
            key: The key to check for in the feed.

        Returns:
            True if key is found in feed, False otherwise.
        """

        return key in [n[-1] for n in self.queue]

    def size(self) -> int:
        """
        Get the current size of the feed.

        Returns:
            Integer of number of items in queue.
        """

        return len(self.queue)

    def clear(self):
        """Reset queue to empty."""

        self.queue = []

    def top(self) -> Tuple[int, int, Dict]:
        """
        Get the top item in the queue.

        Returns:
            The first item stored in the queue.
        """

        return self.queue[0]
