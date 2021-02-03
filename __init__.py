# coding: utf-8

from flask import Flask, request, redirect, abort
from flask_cors import CORS
from bs4 import BeautifulSoup
import json
import datetime
import urllib

app = Flask(__name__)
CORS(app)
ZTM = "http://sdip.metropoliaztm.pl"
lineURL = ZTM + "/web/ml/line/"
routeURL = ZTM + "/web/map/vehicles/gj/A?route_id="
vehiceStatusURL = ZTM + "/web/ml/map/vehicles/"
journeyURL = ZTM + "/web/ml/timetable/journey/"


@app.route("/", methods=["POST", "GET"])
def index():
    abort(501)
    return "501"


@app.route("/line/list")
def line_list():
    response = list()
    ZTMrespo = urllib.request.urlopen(lineURL).read()
    bs = BeautifulSoup(str(ZTMrespo, "utf-8"), "html.parser")
    for line in bs.findAll("li"):
        data = dict()
        data["name"] = line.text
        data["id"] = line.findAll("a")[0]["href"].split("/")[4]
        response.append(data)
    return json.dumps(response)


@app.route("/route/vehicles", methods=["GET", "POST"])
def route_vehicles(*inID):
    response = list()
    idOfLine = get_id(inID)
    ZTMrespo = urllib.request.urlopen(routeURL + idOfLine).read()
    ZTMrespo = json.loads(ZTMrespo)
    for vehicle in ZTMrespo["features"]:
        response.append(vehicle["id"])
    return json.dumps(response)


@app.route("/vehicle/state", methods=["GET", "POST"])
def vehicle_state(*inID):
    response = dict()
    idOfVehicle = get_id(inID)
    ZTMrespo = urllib.request.urlopen(vehiceStatusURL + idOfVehicle).read()
    bs = BeautifulSoup(str(ZTMrespo, "utf-8"), "html.parser")
    response["next"] = bs.findAll("td")[3].text
    try:
        response["delay"] = (
            bs.findAll("td")[4]
                .text.replace("\t", "")
                .replace("\n", "")
                .replace("\r", "")
        )
    except IndexError:
        response["next"] = "Brak danych"
        response["delay"] = "Brak danych"

    if response["delay"] == "\n" or response["delay"] == "":
        response["delay"] = "Brak opóźnienia"

    response["journey"] = bs.findAll("a")[1].attrs["href"].split("/")[5]
    # we need to get last bus stop so we need use journey got get it
    response["last"] = json.loads(vehicle_journey(response["journey"]))["last"]
    return json.dumps(response, ensure_ascii=False)


@app.route("/vehicle/journey", methods=["GET", "POST"])
def vehicle_journey(*inID):
    response = dict()
    idOfJourney = get_id(inID)
    ZTMrespo = urllib.request.urlopen(journeyURL + idOfJourney).read()
    bs = BeautifulSoup(str(ZTMrespo, "utf-8"), "html.parser")
    response["last"] = bs.findAll("span")[0].text
    stops = list()
    for busStop in bs.findAll("tr"):
        if not busStop.find("td") is None:
            tr = busStop.findAll("td")
            if len(tr) == 3:
                if tr[2].text == "\xa0":
                    continue
                stop = dict()
                stop["name"] = tr[0].text.replace("\n", "")
                time = datetime.datetime.now() + datetime.timedelta(
                    minutes=int(tr[2].text.split(" ", 1)[0])
                )
                stop["time"] = time.strftime("%H:%M")
                stop["inTime"] = tr[2].text
                stops.append(stop)
    response["stops"] = stops
    return json.dumps(response, ensure_ascii=False)

# For testing, not recommended to use
@app.route("/vehicle/status", methods=["GET", "POST"])
def vehice_status(*inID):
    idOfVehicle = get_id(inID)
    vehicle = json.loads(vehicle_state(idOfVehicle))
    journey = json.loads(vehicle_journey(vehicle["journey"]))
    response = {**vehicle, **journey}
    return json.dumps(response, ensure_ascii=False)

# For testing, not recommended to use
@app.route("/line/details", methods=["GET", "POST"])
def lineDetail(*inID):
    idOfLine = get_id(inID)
    listOfLines = json.loads(line_list())
    for line in listOfLines:
        if line["name"] == idOfLine:
            ID = line["id"]
            break
    ids = json.loads(route_vehicles(ID))
    response = list()
    for vehicle in ids:
        response.append(json.loads(vehice_status(vehicle)))
    return json.dumps(response, ensure_ascii=False)


def get_id(inID):
    if request.method == "GET":
        if not len(inID):
            return request.args["ID"]
        else:
            return str(inID[0])
    elif request.method == "POST":
        return request.json["ID"]

