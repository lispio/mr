# -*- coding: utf-8 -*-
import logging

from src.db import run_query, run_update
from src.templates.QueryTemplates import qtUserGroups

log = logging.getLogger('mrSvr')


def createGroup(user_name, group_name):
    pass


def addMemberToGroup(group_name, member_id):
    pass


def getGroups(user_id):
    log.debug(qtUserGroups.getGroups.value % user_id)
    results = run_query(qtUserGroups.getGroups.value % user_id)
    if len(results) > 0:
        return results[0][0]


def getMembers(user_name, group_name):
    pass


def removeMemberFromGroup(group_name, member_id):
    pass


def removeGroup(user_name, group_name):
    pass
