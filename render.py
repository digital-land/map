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
    all_layers = [
        {
            "dataset": "local-authority-district",
            "label": "Local authority districts",
            "checked": True,
            "zoom_constraint": False,
        },
        {
            "dataset": "parish",
            "label": "Parishes",
            "active_zoom_level": 10,
            "zoom_constraint": True,
        },
        {
            "dataset": "conservation-area",
            "label": "Conservation areas",
            "zoom_constraint": False,
        },
        {
            "dataset": "brownfield-land",
            "label": "Brownfield land",
            "active_zoom_level": 13,
            "zoom_constraint": True,
        },
        {
            "dataset": "heritage-coast",
            "label": "Heritage coast",
            "zoom_constraint": False,
        },
        {
            "dataset": "area-of-outstanding-natural-beauty",
            "label": "Areas of outstanding natural beauty",
            "zoom_constraint": False,
        },
        {
            "dataset": "ancient-woodland",
            "label": "Ancient woodland",
            "active_zoom_level": 11,
            "zoom_constraint": True,
        },
    ]
    render(
        "index.html",
        map_template,
        layers=[l for l in all_layers if not l["zoom_constraint"]],
        layers_with_constraint=[l for l in all_layers if l["zoom_constraint"]],
    )


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--local":
        env.globals["staticPath"] = "/static"
        env.globals["urlPath"] = ""

    render_bf_map()
    render_national_map()
