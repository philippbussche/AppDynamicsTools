__author__ = 'philipp'

# Please verify what the post has to look like for the renaming.
# From 4.0.6 to 4.0.8 was a change in parameters / payload.

from btRenameHandler import BTRenameHandler

btrh = BTRenameHandler("http", "localhost", "7090", "339f7a258f1d51c4020fcc081ae3")

mappingDict = {
    "/mbb/platformevent" : "",
    "/mbb/vehicleusers" : "",
    "/mbb/menu" : "",
    "/mbb/weathergrid" : "",
    "/mbb/services" : "",
    "/mbb/logon" : "",
    "/mbb/dictation" : "",
    "/mbb/applist" : "",
    "/mbb/ownerverification" : "",
    "/mbb/users" : "",
    "/mbb/tss" : "",
    "/mbb/poivoice" : "",
    "/mbb/jobs" : "",
    "/mbb/vehicles" : "",
    "/mbb/echarge" : "",
    "/mbb/notifications" : "",
    "/mbb/identitystatus" : "",
    "/mbb/ccpoi" : "",
    "/mbb/capabilities" : "",
    "/mbb/obd" : "",
    "/mbb/primaryuser" : "",
    "/mbb/devicereset" : "",
    "/mbb/logoff" : "",
    "/mbb/communicationConf" : "",
    "/mbb/devicestatus" : "",
    "/mbb/ccpoi_detail" : "",
    "/mbb/license" : "",
    "/mbb/news" : "Newsservice",
    "/mbb/twitterStepup" : "Twitter Stepup",
    "/mbb/personalpoi" : "Personal POI (VW)",
    "/mbb/rbc" : "Remote Battery Charge",
    "/mbb/traffic-online" : "Traffic",
    "/mbb/fpi" : "Fuel Price Information",
    "/mbb/poi" : "Points of intererst",
    "/mbb/flightinfo" : "Fluginformationen",
    "/mbb/remoteupdate" : "Remote Update Security Manager",
    "/mbb/traininfo" : "Zuginfo",
    "/mbb/rpc" : "Remote Pretrip Climatisation",
    "/mbb/disclaimer" : "Disclaimer",
    "/mbb/parkinfo" : "Parkempfehlung",
    "/mbb/destinationfeedservice" : "Destinationimport / Zieleinspeisung",
    "/mbb/rts" : "Remote Trip Statistics",
    "/mbb/cityevents" : "City-Events",
    "/mbb/rs" : "Remote Standheizung",
    "/mbb/countryinfo" : "Landesinformationen",
    "/mbb/rdt" : "Remote Depature Time Programming",
    "/mbb/cityevents_rev3" : "City-Events Rev3",
    "/mbb/loggingandaccounting" : "Logging",
    "/mbb/parkinfo_rev3" : "Parkempfehlung Rev3",
    "/mbb/geofencing" : "Geofencing",
    "/mbb/otv" : "Online Terminvereinbarung",
    "/mbb/speedalert" : "Speed Alert",
    "/mbb/opr" : "Online Pannenruf",
    "/mbb/valetalert" : "Valet Alert",
    "/mbb/rlu" : "Remote Lock Unlock",
    "/mbb/picturenav" : "Picture Navigation",
}


btList = btrh.getBTPageList("4")
for bt in btList["btListEntries"]:
    originalName = bt["originalName"]
    if originalName != "_APPDYNAMICS_DEFAULT_TX_" and originalName != None:
            id = bt["id"]
            name = bt["name"]
            if name.startswith("/mbb"):
                # print "\"" + name + "\"" + " : " + "\"\","
                if name in mappingDict:
                    if mappingDict[name] != "":
                        print "Renaming: "+name+" (ID:" + str(id) + ") --> " + mappingDict[name]
                        btrh.renameBT(id, mappingDict[name])



