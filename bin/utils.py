import os
import json
import pandas as pd
import requests

from cachecontrol import CacheControl
from cachecontrol.caches.file_cache import FileCache

session = CacheControl(requests.session(), cache=FileCache(".cache"))


def get(url):
    r = session.get(url)
    r.raise_for_status()
    return r.text


def render(path, template, docs="docs", **kwargs):
    path = os.path.join(docs, path)
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(path, "w") as f:
        print(f"creating {path}")
        f.write(template.render(**kwargs))


def read_in_json(path):
    file = open(path, mode="r")
    s = file.read()
    return json.loads(s)
