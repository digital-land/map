DATASET_PATH := data/dataset.csv
LOCAL_FRONTEND :=../frontend

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
	wget -O $(DATASET_PATH) https://media.githubusercontent.com/media/digital-land/brownfield-land-collection/main/dataset/brownfield-land.csv

prepare: collect
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
	mkdir -p docs/static/javascripts
	cd $(LOCAL_FRONTEND) && gulp js
	rsync -r $(LOCAL_FRONTEND)/digital_land_frontend/static/javascripts/ docs/static/javascripts/

local: assets map/local

copy:
	mkdir -p docs/
	cp -r src/ docs/

render: copy map