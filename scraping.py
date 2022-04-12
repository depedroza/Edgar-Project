import json

"""For single doc"""

infile = open("submissions.json", "r")
submissions = json.load(infile)

print(submissions["filings"]["recent"].keys())

for key, value in submissions["filings"]["recent"].items():
    print("key: ", key, "value: ", value)


'''
"""Multi-doc"""
docs = ["aggregates.json", "companyfacts.json", "submissions.json"]
for x in docs:
    infile = open(x, "r")
    dictionary = json.load(infile)
    print(f"{x.upper()} Keys: {dictionary.keys()}")
'''
