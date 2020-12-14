#!/usr/bin/env python3

import json


from bin.analyse_dataset import BrownfieldDatasetAnalyser
from bin.organisation import fetch_organisations


da = BrownfieldDatasetAnalyser("data/brownfield-land.csv")


def process_org(org):
    sites = da.get_data_for_organisation(org.get("organisation"))
    return {
        "id": org.get("organisation"),
        "statistical_geography": org.get("statistical-geography"),
        "name": org.get("name"),
        "count": len(sites),
    }


def brownfield_map(orgs):
    orgs_data = []
    for o_id in orgs:
        if organisations.get(o_id) is not None:
            orgs_data.append(process_org(organisations.get(o_id)))
        else:
            print("no match for", o_id)
    return orgs_data


organisations = fetch_organisations()
orgs_with_bfs = da.organisations()
# need to remove any pesky None organisation values
orgs_with_bfs = [o for o in orgs_with_bfs if o is not None]
d = brownfield_map(orgs_with_bfs)

with open("data/organisation_boundary_data.json", "w") as file:
    file.write(json.dumps(d))
