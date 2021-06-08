# Digital land map

This repo renders the map at [digital-land.github.io/map](https://digital-land.github.io/map/).

If working locally we recommend working in a virtualenv. Then to get set up run

    make init
    make render

## Add polygon layers to the map

The layers are listed in `render.py`.

Add a new layer by adding an entry like

```
{
    "dataset": "park-and-garden",
    "label": "Parks and gardens",
    "colour": "#0EB951",
    "active_zoom_level": 10,
}
````

**dataset** - the name of the dataset, it must match the pipeline name
**label** - the text that will be shown next to the layer checkbox
**colour** - the colour to use for the polygons, must be a hex code. OPTIONAL.
**active_zoom_level** - use for large datasets where you want to only show the data when a user is zoomed in, integer. OPTIONAL. 


