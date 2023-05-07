import connexion

from borValBadgeDbServer.models.user_request_check_get200_response import UserRequestCheckGet200Response  # noqa: E501
from borValBadgeDbServer.models.user_report_missing_get200_response import UserReportMissingGet200Response  # noqa: E501
from borValBadgeDbServer import util
from borValBadgeDbServer.db.db import dbLock, getCachedBadgeDB, getBadgeDB, getBadgeIdCache
from borValBadgeDbServer.db.checker import checkInProgress, startCheck, reportMissing


def user_dump_dbget():  # noqa: E501
    """Get a dump of the entire database. Updates every five minutes

     # noqa: E501


    :rtype: Union[Database, Tuple[Database, int], Tuple[Database, int, Dict[str, str]]
    """

    dbLock.acquire()
    ret = connexion.lifecycle.ConnexionResponse(
        status_code=200,
        content_type="application/json",
        mimetype="text/plain",
        body=getCachedBadgeDB()
    )
    dbLock.release()
    return ret


def user_report_missing_get(badge_ids):  # noqa: E501
    """Run checks based on missing/unknown badge ids

     # noqa: E501

    :param badge_ids: The CSV of badge ids
    :type badge_ids: List[int]

    :rtype: Union[UserReportMissingGet200Response, Tuple[UserReportMissingGet200Response, int], Tuple[UserReportMissingGet200Response, int, Dict[str, str]]
    """

    badge_ids = {str(x) for x in badge_ids}

    dbLock.acquire()
    for universeId in getBadgeDB().universes.keys():
        badge_ids -= getBadgeIdCache(universeId)
    dbLock.release()

    return UserReportMissingGet200Response(reportMissing(badge_ids))


def user_report_missing_post(body):  # noqa: E501
    """Run checks based on missing/unknown badge ids

     # noqa: E501

    :param body: The CSV of badge ids
    :type body: str

    :rtype: Union[UserReportMissingGet200Response, Tuple[UserReportMissingGet200Response, int], Tuple[UserReportMissingGet200Response, int, Dict[str, str]]
    """

    return user_report_missing_get(body.decode().split(","))


def user_request_check_get(universe_id):  # noqa: E501
    """Request a check/recheck of an universe. Gets ignored if the universe was last checked &lt;5 mins ago

     # noqa: E501

    :param universe_id: The universe id to check
    :type universe_id: int

    :rtype: Union[UserRequestCheckGet200Response, Tuple[UserRequestCheckGet200Response, int], Tuple[UserRequestCheckGet200Response, int, Dict[str, str]]
    """

    universe_id = str(universe_id)
    dbLock.acquire()
    lastChecked = 0
    if universe_id in getBadgeDB().universes:
        lastChecked = getBadgeDB().universes[universe_id].last_checked
    dbLock.release()

    if util.getTimestamp() - lastChecked >= 5 * 60 * 1000:
        startCheck(universe_id)

    return UserRequestCheckGet200Response(lastChecked, checkInProgress(universe_id))
