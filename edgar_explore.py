import json

docs = ["aggregates.json", "companyfacts.json", "submissions.json"]
for x in docs:
    infile = open(x, "r")
    outfile = open(f"readable_{x}", "w")

    edgar_data = json.load(infile)

    json.dump(edgar_data, outfile, indent=4)
