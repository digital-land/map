#!/usr/bin/env python3
import sys

from digital_land_frontend.jinja import setup_jinja
from bin.utils import render, read_in_json


env = setup_jinja()
env.globals["includeAutocomplete"] = True


def render_bf_map():
    bf_map_template = env.get_template("brownfield-land-map.html")
    data = read_in_json("data/organisation_boundary_data.json")
    render("brownfield-land/index.html", bf_map_template, data=data)


def render_national_map():
    map_template = env.get_template("national-map.html")
    layers = [
        {"dataset": "local-authority-district", "label": "Local authority districts"},
        {"dataset": "conservation-area", "label": "Conservation areas"},
        {"dataset": "brownfield-land", "label": "Brownfield land"},
        {"dataset": "heritage-coast", "label": "Heritage coast"},
        {
            "dataset": "area-of-outstanding-natural-beauty",
            "label": "Areas of outstanding natural beauty",
        },
    ]
    render("index.html", map_template, layers=layers)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--local":
        env.globals["staticPath"] = "/static"
        env.globals["urlPath"] = ""

    render_bf_map()
    render_national_map()
