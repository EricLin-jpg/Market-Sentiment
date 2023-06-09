"""
This class stores all the information for the companies and their stocks,
as well as the news data and their sentiments.
"""


class Data:
    """This class stores all the information for the companies and their stocks,
        as well as the news data and their sentiments."""

    def __init__(self):
        self.companies = {}  # dict {name : ticker} and {ticker : name}
        self.tickers = []  # list [ticker]
        self.tickers_info = None  # Ticker object

        self.previous_closing = {}  # dict {ticker : previous_closing}
        self.closings = {}  # dict {ticker : [date, previous_closing]}, 14 days
        self.closings_date_logged = None  # datetime, last logged for all companies

        self.current_prices = {}  # dict {ticker : current_price}
        self.current_prices_date_logged = None  # datetime, last logged

        self.analyst_recommendations = {}  # dict {ticker : {recommendation : count}}

        self.news = {}  # dict {ticker : [news]}
        self.sentiment = {}  # dict {ticker : sentiment}
        self.news_count = {}  # dict {ticker : [news_count]}
        self.news_date_logged = {}  # {ticker : datetime}
        self.news_date_logged_all = None  # datetime, last logged for all companies
        self.news_is_complete = False  # bool, True if all news data is logged
