# test_helper.py
# This class tests SDK helpers

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import (
    find_operation,
    Hosts,
    InvalidOperation,
    InvalidOperationSearch,
    InvalidRoute,
    InvalidServiceCollection
    )

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Hosts(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 429]


class TestHelper:
    def test_find_operation(self):
        error_checks = False
        result = find_operation("GetDeviceDetails")
        if result["operation"] == "GetDeviceDetails":
            error_checks = True
        result = find_operation("/devices/entities/devices/v2", "route")
        if result["operation"] == "GetDeviceDetails":
            error_checks = True
        result = find_operation("Hosts", "collection")
        if len(result) == 18:
            error_checks = True
        result = find_operation("GetOnlineState", exact=False)
        if len(result) == 2:
            error_checks = True
        result = find_operation("host", "collection", False)
        if len(result) == 3:
            error_checks = True
        result = find_operation("/filevantage/", "route", False)
        if len(result) == 18:
            error_checks = True
        try:
            find_operation("whatever", "whatever", True)
        except InvalidOperationSearch:
            error_checks = True
        try:
            find_operation("whatever")
        except InvalidOperation:
            error_checks = True
        try:
            find_operation("/banana", "route")
        except InvalidRoute:
            error_checks = True
        try:
            find_operation("banana", "collection", exact=False)
        except InvalidServiceCollection:
            error_checks = True

        assert error_checks
