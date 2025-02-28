import os
import sys
import json
import traceback
from threading import Lock
import shutil
import gzip
import requests

from borValBadgeDbServer.models.database import Database
from borValBadgeDbServer.util import getTimestamp

dbPath = None
dbLock = Lock()
badgeDB: Database = None
badgeIdCache = {}
nvlList = set()


def getBadgeDB():
    return badgeDB


def isNVL(badgeId):
    global nvlList
    return str(badgeId) in nvlList


def getBadgeIdCache():
    return badgeIdCache


def updateBadgeIdCache(universeId):
    for badgeId in map(int, badgeDB.universes[universeId].badges.keys()):
        badgeIdCache[badgeId] = universeId

    for badgeId in badgeDB.universes[universeId].free_badges:
        badgeIdCache[badgeId] = universeId


def loadDatabase():
    dbLock.acquire()
    global nvlList
    for nvl in open("nonvaluablelegacybadges.txt").read().replace(",", " ").split():
        if nvl in ["20006347", "20006350", "20006359", "17911219"] or int(nvl) < 17170400:
            continue
        nvlList.add(nvl)
    print(f"loadDatabase: Loaded {len(nvlList)} NVLs")

    global dbPath
    if len(sys.argv) < 2:
        dbPath = "borValBadgeDB.json.gz"
        if not os.path.isfile(dbPath):
            data = requests.get('https://dl.dropboxusercontent.com/scl/fi/q3e3x95sy95sjdoy5bs0e/xrow1h.gz?rlkey=m68nef65p22vp1khwjjf9sm0w&st=ru15owl4&dl=0')
            with open(dbPath, 'wb') as f:
                f.write(data.content)
    else:
        dbPath = sys.argv[1]
    global badgeDB
    try:
        badgeDB = Database.from_dict(json.load(gzip.open(dbPath, "r")))
        totalBadgeCount = 0
        for universe in badgeDB.universes.values():
            totalBadgeCount += universe.badge_count
        print(f"loadDatabase: Loaded {dbPath} with {len(badgeDB.universes)} universes and {totalBadgeCount} badges", file=sys.stderr)
    except Exception:
        traceback.print_exc()
        print(f"loadDatabase: Failed to load {dbPath}! Using default", file=sys.stderr)
        badgeDB = Database.from_dict({"universes": {}})

        if os.path.isfile(dbPath):
            bakPath = dbPath + f"-{getTimestamp()}.bak"
            shutil.copy2(dbPath, bakPath)
            print(f"loadDatabase: Copied {dbPath} to {bakPath}", file=sys.stderr)

    for universeId in badgeDB.universes.keys():
        updateBadgeIdCache(universeId)
    dbLock.release()

    """
    try:
        from guppy import hpy
        h = hpy()
        heap = h.heap()
        print(heap, file=sys.stderr)
        print(heap.byrcs, file=sys.stderr)
    except ModuleNotFoundError:
        pass
    """
