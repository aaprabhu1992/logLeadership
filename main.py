import sys
import json
import argparse

import helper
import realityHub

parser = argparse.ArgumentParser()
parser.add_argument('-fileName',
                    type=str,
                    help='Event JSON')
parser.add_argument('-realityHub',
                    type=str,
                    help='Reality Hub Credential')
args = parser.parse_args()
fileName = args.fileName
realityHubCredFile = args.realityHub

eventObj = {}
try:
    with open(fileName, "r") as f:
        eventObj = json.load(f)
except OSError:
    print("File Read Error")
helper.PrettyPrintJSON(eventObj)


realityHubCred = {}
try:
    with open(realityHubCredFile, "r") as f:
        realityHubCred = json.load(f)
except OSError:
    print("Reality Hub Credentials File Read Error")
helper.PrettyPrintJSON(realityHubCred)


if "organize" in eventObj:
    allOrganizations = eventObj["organize"]
    for organizeObj in allOrganizations:
        realityHub.addOrganize(organizeObj, realityHubCred)
