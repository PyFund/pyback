from pyback.strategy import Strategy


def test_init():
    """Test Strategy instances can be initialized correctly
    """

    strategy = Strategy("SMA")

    assert strategy.name == "SMA"


def test_add_feed_str():
    """Test Strategy instances can subscribe to feeds with single str
    """

    strategy = Strategy("SMA")
    strategy.subscribe("Stock-AAPL")

    assert strategy.feed == set(["Stock-AAPL"])


def test_add_feed_list():
    """Test Strategy instances can subscribe to a list of feeds
    """

    strategy = Strategy("SMA")
    strategy.subscribe(["Stock-AAPL", "Stock-MSFT"])

    assert strategy.feed == set(["Stock-AAPL", "Stock-MSFT"])


def test_add_feed_mixed():
    """Test Strategy instances can subscribe to both single string feed_id
    and list of feed_id's
    """

    strategy = Strategy("SMA")
    strategy.subscribe("Stock-AAPL")
    strategy.subscribe(["Stock-GOOGL", "Stock-MSFT"])

    assert strategy.feed == set(["Stock-AAPL", "Stock-GOOGL", "Stock-MSFT"])
