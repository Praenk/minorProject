import os
import json
from django.shortcuts import render

# Create your views here.


class Lab():
    def __init__(self):
        self.loc = "static/labs"

    def getAllLabs(self):
        return os.listdir(self.loc)

    def getImagesOfLabs(self, lab, equip):
        imageLoc = os.path.join(self.loc, lab, equip, "images")
        return os.listdir(imageLoc)

    def getAllEquip(self, lab):
        equipLoc = os.path.join(self.loc, lab)
        return os.listdir(equipLoc)

    def getData(self, lab, equip):
        dataLoc = os.path.join(self.loc, lab, equip, "data.json")
        with open(dataLoc, 'r') as f:
            data = f.read()
        data = json.loads(data)
        return data

    def getAllData(self):
        data = {}
        allLabs = self.getAllLabs()

        for lab in allLabs:
            data[lab] = {}
            equipments = {}

            for equip in self.getAllEquip(lab):
                equipments[equip] = []
                equipments[equip] = self.getImagesOfLabs(lab, equip)

            data[lab] = equipments

        return data


obj = Lab()


def home(request):
    context = {
        "title": "MINOR PROJECT",
        "allData": obj.getAllData(),
    }
    return render(request, 'equipments/home.html', context)


def details(request, labName, equip):
    loc = os.path.join("/static/labs/", labName, equip, "images")

    context = {
        "title": "MINOR PROJECT",
        "lab": labName,
        "product": equip,
        "img": os.path.join(loc,obj.getImagesOfLabs(labName, equip)[0]),
        "details": obj.getData(labName, equip),
    }

    return render(request, 'equipments/details.html', context)
