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


class TestArgsToParamsCoverage:
    """Cover _util/_functions.py args_to_params URL-encoded warning with log."""

    def test_urlencoded_warning_with_log(self):
        """args_to_params URL-encoded arg non-pythonic with logger."""
        h = Hosts(client_id="fake", client_secret="fake", debug=True, pythonic=False)
        result = h.query_devices(filter="platform_name%3A'Windows'")
        assert isinstance(result, dict)
