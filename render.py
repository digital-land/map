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
            "paint_options": {
              "colour": "#0b0c0c",
              "opacity": "0.1",
              "weight": 5
            }
        },
        {
            "dataset": "conservation-area",
            "label": "Conservation areas",
            "paint_options": {
              "colour": "#78AA00",
            }
        },
        {
            "dataset": "brownfield-land",
            "label": "Brownfield land",
            "paint_options": {
              "colour": "#745729",
            },
            "type": "point",
        },
        {
            "dataset": "parish",
            "label": "Parishes",
            "paint_options": {
              "colour": "#5694ca",
            }
        },
        {
            "dataset": "heritage-coast",
            "label": "Heritage coast",
            "paint_options": {
              "colour": "#912b88",
            }
        },
        {
            "dataset": "area-of-outstanding-natural-beauty",
            "label": "Areas of outstanding natural beauty",
            "paint_options": {
              "colour": "#d53880",
            }
        },
        {
            "dataset": "ancient-woodland",
            "label": "Ancient woodland",
            "paint_options": {
              "colour": "#00703c",
              "opacity": 0.2
            }
        },
        {
            "dataset": "green-belt",
            "label": "Green belt", 
            "paint_options": {
                "colour": "#85994b"
            }
        },
        {
            "dataset": "world-heritage-site",
            "label": "World heritage site",
            "paint_options": {
              "colour": "#012169",
            }
        },
        {
            "dataset": "battlefield",
            "label": "Battlefields",
            "paint_options": {
                "colour": "#4d2942",
                "opacity": 0.2
            }
        },
        {
            "dataset": "park-and-garden",
            "label": "Parks and gardens",
            "paint_options": {
              "colour": "#0EB951",
            }
        },
        {
            "dataset": "protected-wreck-site",
            "label": "Protected wreck sites",
            "paint_options": {
              "colour": "#0b0c0c",
            }
        },
        {
            "dataset": "listed-building",
            "label": "Listed buildings",
            "paint_options": {
              "colour": "#F9C744",
            },
            "type": "point",
        },
        {
            "dataset": "special-area-of-conservation",
            "label": "Special areas of conservation",
            "paint_options": {
              "colour": "#7A8705",
            }
        },
        {
            "dataset": "scheduled-monument",
            "label": "Scheduled monuments",
            "paint_options": {
              "colour": "#0F9CDA",
            }
        },
        {
            "dataset": "heritage-at-risk",
            "label": "Heritage at risk",
            "paint_options": {
              "colour": "#8D73AF",
            }
        },
        {
            "dataset": "certificate-of-immunity",
            "label": "Certificate of immunity",
            "paint_options": {
              "colour": "#D8760D",
            }
        },
        {
            "dataset": "building-preservation-notice",
            "label": "Building preservation notices",
            "paint_options": {
              "colour": "#f944c7",
            }
        },
        {
            "dataset": "ramsar",
            "label": "Ramsar", 
            "paint_options": {
                "colour": "#7fcdff"
            }
        },
        {
            "dataset": "site-of-special-scientific-interest",
            "label": "Sites of special scientific interest",
            "paint_options": {
              "colour": "#308fac",
            }
        },
    ]
    render(
        "index.html",
        map_template,
        layers=sorted(
            [l for l in all_layers if l.get("active_zoom_level") is None],
            key=lambda x: x["label"],
        ),
    )


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--local":
        env.globals["staticPath"] = "/static"
        env.globals["urlPath"] = ""

    render_bf_map()
    render_national_map()
