#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'philipp'

from eumRenameHandler import EUMRenameHandler
import re

erh = EUMRenameHandler("http",
                       "localhost",
                       "7090",
                       "a37ba392852abd10273bfea4b169",
                       True)

renamingPatterns = {
    ".*/content/[a-z]+/sales/[a-z]+/poster-view\.html": "STARTSEITE",
    "configuration\?[a-z]+\&set": "ADDCONFIGURATION",
    "configuration\?[a-z]+\&remove": "REMOVECONFIGURATION",
    "configuration\?[a-z]+\&action\=accept": "ACCEPTCONFLICT",
    "configuration\?[a-z]+\&action\=abort": "ABORTCONFLICT",
    "content/[a-z]+/sales/[a-z]+/poster-view/edit-configuration/edit-[a-z]+.carline": "DETAILPAGE",
    "content/[a-z]+/sales/[a-z]+/poster-view/edit-configuration.carline": "CONFIGURATIONPAGE"
}

processedPages = []

def renameStartpage(id, name):
    print ("Renaming: " + name)
    m = re.search("(.*)/content/([a-z]+)/sales/[a-z]+/poster-view\.html", name)
    if m.groups:
        newName = "Startseite." + m.group(2) + " (" + m.group(1) + ")"
        print "POST: " + str(id) + "--> " + newName
        erh.renamePage(id,newName)

def renameAddConfiguration(id, name):
    print ("Renaming: " + name)
    m = re.search("configuration\?([a-z]+)\&set", name)
    if m.groups:
        newName = "Ausstattung hinzuf%C3%BCgen." + m.group(1)
        print "POST: " + str(id) + "--> " + newName
        erh.renamePage(id,newName)

def renameRemoveConfiguration(id, name):
    print ("Renaming: " + name)
    m = re.search("configuration\?([a-z]+)\&remove", name)
    if m.groups:
        newName = "Ausstattung l%C3%B6schen." + m.group(1)
        print "POST: " + str(id) + "--> " + newName
        erh.renamePage(id,newName)

def renameAcceptConflict(id, name):
    print ("Renaming: " + name)
    m = re.search("configuration\?([a-z]+)\&action\=accept", name)
    if m.groups:
        newName = "Konflikt annehmen." + m.group(1)
        print "POST: " + str(id) + "--> " + newName
        erh.renamePage(id,newName)

def renameAbortConflict(id, name):
    print ("Renaming: " + name)
    m = re.search("configuration\?([a-z]+)\&action\=abort", name)
    if m.groups:
        newName =  "Konflikt ablehnen." + m.group(1)
        print "POST: " + str(id) + "--> " + newName
        erh.renamePage(id,newName)

def renameDetailpage(id, name):
    print ("Renaming: " + name)
    m = re.search("content/([a-z]+)/sales/[a-z]+/poster-view/edit-configuration/edit-([a-z]+).carline", name)
    if m.groups:
        newName = m.group(2).capitalize() + "." + m.group(1)
        print "POST: " + str(id) + "--> " + newName
        erh.renamePage(id,newName)

def renameConfigurationpage(id, name):
    print ("Renaming: " + name)
    m = re.search("content/([a-z]+)/sales/[a-z]+/poster-view/edit-configuration.carline", name)
    if m.groups:
        newName = "Konfiguration" + "." + m.group(1)
        print "POST: " + str(id) + "--> " + newName
        erh.renamePage(id,newName)

pageProcessed = False
notProcessedPages = []

pageList = erh.getEUMPageList("28")
for page in pageList["pageList"]:
    id = page["addId"]
    if id not in processedPages:
        name = page["name"]
        print "Processing: " + name
        for pattern in renamingPatterns:
            p = re.compile(pattern)
            if p.match(name):
                pageProcessed = True
                type = renamingPatterns[pattern]
                processedPages.append(id)
                if(type == "STARTSEITE"):
                    renameStartpage(id, name)
                if(type == "ADDCONFIGURATION"):
                    renameAddConfiguration(id,name)
                if(type == "REMOVECONFIGURATION"):
                    renameRemoveConfiguration(id,name)
                if(type == "ACCEPTCONFLICT"):
                    renameAcceptConflict(id,name)
                if(type == "ABORTCONFLICT"):
                    renameAbortConflict(id,name)
                if(type == "DETAILPAGE"):
                    renameDetailpage(id,name)
                if(type == "CONFIGURATIONPAGE"):
                    renameConfigurationpage(id,name)
        if pageProcessed is False:
            notProcessedPages.append(name)

if(len(notProcessedPages) > 0):
    print "These pages were not processed: ".join(notProcessedPages)
else:
    print "All pages processed."


