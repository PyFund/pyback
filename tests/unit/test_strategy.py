from pyback.strategy import Strategy


def test_init():
    """Test Strategy instances can be initialized correctly
    """

    strategy = Strategy("SMA")

    assert strategy.name == "SMA"
    assert strategy.orders == list()
    assert strategy.feed == list()
    assert strategy.algo is None


def test_add_feed_str():
    """Test Strategy instances can subscribe to feeds with single str
    """

    strategy = Strategy("SMA")

    strategy.subscribe("Stock-AAPL")

    assert strategy.feed == ["Stock-AAPL"]


def test_add_feed_list():
    """Test Strategy instances can subscribe to a list of feeds
    """

    strategy = Strategy("SMA")

    strategy.subscribe(["Stock-AAPL", "Stock-MSFT"])

    assert strategy.feed == ["Stock-AAPL", "Stock-MSFT"]


def test_add_feed_mixed():
    """Test Strategy instances can subscribe to both single string feed_id
    and list of feed_id's
    """

    strategy = Strategy("SMA")

    strategy.subscribe("Stock-AAPL")
    strategy.subscribe(["Stock-GOOGL", "Stock-MSFT"])

    assert strategy.feed == ["Stock-AAPL", "Stock-GOOGL", "Stock-MSFT"]


def test_create_order():
    """Test Strategy can create an order
    """

    strategy = Strategy("SMA")

    strategy.order("AAPL", 0.5, 200)

    assert strategy.orders == [
        {
            "order_id": "SMA_1",
            "security_id": "AAPL",
            "weight": 0.5,
            "limit": 200,
            "stop": None,
        }
    ]


def test_create_orders():
    """Test Strategy can create multiple orders
    """

    strategy = Strategy("SMA")

    strategy.order("AAPL", 0.5, 200)
    strategy.order("GOOGL", 0.3, stop=1000)

    assert strategy.orders == [
        {
            "order_id": "SMA_1",
            "security_id": "AAPL",
            "weight": 0.5,
            "limit": 200,
            "stop": None,
        },
        {
            "order_id": "SMA_2",
            "security_id": "GOOGL",
            "weight": 0.3,
            "limit": None,
            "stop": 1000,
        },
    ]
