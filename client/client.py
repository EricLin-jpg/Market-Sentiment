"""Main file for the client."""

from flask import Blueprint, render_template, request, url_for
import requests

import utils.html_builder as html_builder

# register a client blueprint
client_bp = Blueprint("client", __name__)

client_bp.static_folder = "static"
client_bp.template_folder = "templates"

# ==============================================================================


@client_bp.route("/")
def index():
    """Return the index page."""
    return render_template("index.html")


@client_bp.route("/load-index")
def load_index():
    """Return the index page."""
    print("Loading index...", flush=True)
    stock_api_url = request.host_url.rstrip('/') + url_for("API.get_stock")
    news_api_url = request.host_url.rstrip('/') + url_for("API.get_news")

    stock_data = requests.get(stock_api_url, timeout=300).json()
    news_data = requests.get(news_api_url, timeout=300).json()

    # raw time data
    current_prices_update_time = stock_data["meta"]["current_prices_date_logged"]
    previous_closing_prices_update_time = stock_data["meta"]["closings_date_logged"]
    news_update_time = news_data["meta"]["news_date_logged_all"]

    # format time data
    current_prices_update_time = current_prices_update_time.split(".")[0]
    previous_closing_prices_update_time = previous_closing_prices_update_time.split(".")[
        0]
    news_update_time = news_update_time.split(".")[0]

    return render_template("template.html",
                           buttons=html_builder.build_buttons(
                               stock_data["data"]),
                           current_prices_update_time=current_prices_update_time,
                           previous_closing_prices_update_time=previous_closing_prices_update_time,
                           news_update_time=news_update_time,
                           panes=html_builder.build_panes(
                               stock_data["data"], news_data=news_data["data"]),
                           rec_charts_script=html_builder.build_rec_charts_scripts(
                               stock_data["data"]),
                           sent_charts_script=html_builder.build_sent_charts_scripts(
                               news_data["data"]))

# testing


@client_bp.route("/template")
def template():
    """Return the template page."""
    return render_template("template.html")


@client_bp.route("/how_it_works")
def how_it_works():
    """Return the how_it_works page."""
    return render_template("how_it_works.html")


@client_bp.route("/script.js")
def script():
    """Return the script.js file."""
    return client_bp.send_static_file("script.js")


@client_bp.route("/update.js")
def update():
    """Return the update.js file."""
    return client_bp.send_static_file("update.js")


@client_bp.route("/styles.css")
def styles():
    """Return the styles.css file."""
    return client_bp.send_static_file("styles.css")


@client_bp.route("/favicon.ico")
def favicon():
    """Return the favicon.ico file."""
    return client_bp.send_static_file("favicon.ico")
