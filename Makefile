DATASET_PATH := data/dataset.csv
REMOTE_FRONTEND :=https://raw.githubusercontent.com/digital-land/frontend/main/
LOCAL_FRONTEND :=../frontend
SOURCE_URL=https://raw.githubusercontent.com/digital-land/
LFS_SOURCE_URL=https://media.githubusercontent.com/media/digital-land/

# current git branch
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

black:
	black .

init::
	python3 -m pip install -r requirements.txt

clobber clean:
	rm -rf docs .cache

collect:
	mkdir -p data
	curl -qsL '$(LFS_SOURCE_URL)brownfield-land-collection/main/dataset/brownfield-land.csv' > $(DATASET_PATH)

#prepare: collect
prepare:
	python3 prepare_data.py

map:
	mkdir -p docs/
	python3 render.py

commit-docs::
	git add docs data
	git diff --quiet && git diff --staged --quiet || (git commit -m "Rebuilt docs $(shell date +%F)"; git push origin $(BRANCH))

map/local:
	mkdir -p docs/
	python3 render.py --local

assets: latest/css latest/js

latest/css:
	mkdir -p docs/static/stylesheets
	cd $(LOCAL_FRONTEND) && gulp stylesheets
	rsync -r $(LOCAL_FRONTEND)/digital_land_frontend/static/stylesheets/ docs/static/stylesheets/

latest/js:
	mkdir -p docs/static/javascripts/vendor/
	cd $(LOCAL_FRONTEND) && gulp js
	rsync -r $(LOCAL_FRONTEND)/digital_land_frontend/static/javascripts/ docs/static/javascripts/
	cp $(LOCAL_FRONTEND)/digital_land_frontend/static/javascripts/dl-maps.js docs/static/javascripts/
	cp $(LOCAL_FRONTEND)/digital_land_frontend/static/javascripts/vendor/leaflet.permalink.min.js docs/static/javascripts/vendor/leaflet.permalink.min.js
	cp $(LOCAL_FRONTEND)/digital_land_frontend/static/javascripts/dl-national-map-controller.js docs/

local: assets map/local

fetch-js:
	mkdir -p docs/
	curl -qsL '$(REMOTE_FRONTEND)digital_land_frontend/static/javascripts/dl-national-map-controller.js' > docs/dl-national-map-controller.js

copy-base-json:
	cp static/base-tile.json docs/

render: fetch-js map copy-base-json

local: latest/js map/local copy-base-json