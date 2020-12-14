#!/usr/bin/env python3
import sys

from digital_land_frontend.jinja import setup_jinja
from bin.utils import render, read_in_json


env = setup_jinja()
env.globals["includeAutocomplete"] = True
map_template = env.get_template("brownfield-land-map.html")

data = read_in_json("data/organisation_boundary_data.json")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--local":
        env.globals["staticPath"] = "/static"
        env.globals["urlPath"] = ""

    render("index.html", map_template, data=data)
