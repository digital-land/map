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
            "colour": "#EE7800",
        },
        {
            "dataset": "parish",
            "label": "Parishes",
            "active_zoom_level": 10,
            "colour": "#5694ca",
        },
        {
            "dataset": "conservation-area",
            "label": "Conservation areas",
            "colour": "#78AA00",
        },
        {
            "dataset": "brownfield-land",
            "label": "Brownfield land",
            "active_zoom_level": 13,
            "colour": "#0078ff",
        },
        {
            "dataset": "heritage-coast",
            "label": "Heritage coast",
            "colour": "#912b88",
        },
        {
            "dataset": "area-of-outstanding-natural-beauty",
            "label": "Areas of outstanding natural beauty",
            "colour": "#d53880",
        },
        {
            "dataset": "ancient-woodland",
            "label": "Ancient woodland",
            "active_zoom_level": 11,
            "colour": "#00703c",
        },
        {"dataset": "green-belt", "label": "Green belt", "colour": "#85994b"},
        {
            "dataset": "world-heritage-site",
            "label": "World heritage site",
            "colour": "#012169",
        },
        {"dataset": "battlefield", "label": "Battlefields", "colour": "#4d2942"},
        {
            "dataset": "park-and-garden",
            "label": "Parks and gardens",
            "colour": "#0EB951",
            "active_zoom_level": 10,
        },
        {
            "dataset": "protected-wreck-site",
            "label": "Protected wreck sites",
            "colour": "#0b0c0c",
        },
    ]
    render(
        "index.html",
        map_template,
        layers=sorted(
            [l for l in all_layers if l.get("active_zoom_level") is None],
            key=lambda x: x["label"],
        ),
        layers_with_constraint=sorted(
            [l for l in all_layers if l.get("active_zoom_level") is not None],
            key=lambda x: x["label"],
        ),
    )


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--local":
        env.globals["staticPath"] = "/static"
        env.globals["urlPath"] = ""

    render_bf_map()
    render_national_map()
