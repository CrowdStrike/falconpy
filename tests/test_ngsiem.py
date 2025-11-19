"""
test_ngsiem.py - This class tests the NGSIEM service class
"""
import os
import sys
from requests import Response

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import NGSIEM

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = NGSIEM(auth_object=config)
AllowedResponses = [200, 201, 400, 403, 404, 429]  # Temp allow 403


class TestNGSIEM:
    def run_all_tests(self):
        test_search = {
            #"showQueryEventDistribution" : True,
            "isLive" : False,
            "start" : "1d",
            "queryString" : "#event_simpleName=*"
            }
        error_checks = True
        search_id = "bob"
        tests = {
            "UploadLookupV1" : falcon.upload_file(repository="search-all", lookup_file="tests/testfile.csv"),
            "UploadLookupV1" : falcon.upload_file(repository="search-all", lookup_file="tests/testfile.json"),
            "GetLookupFromPackageWithNamespaceV1": falcon.get_file_from_package_with_namespace(repository="search-all",
                                                                                               filename="manny",
                                                                                               package="moe",
                                                                                               namespace="jack"
                                                                                               ),
            "GetLookupFromPackageV1": falcon.get_file_from_package(repository="search-all",
                                                                   filename="manny",
                                                                   package="moe"
                                                                   ),
            "StartSearchV1": falcon.start_search(repository="search-all", search=test_search, is_live=False, start="1d", timezone_offset_minutes=0),
            "StartSearchV1B": falcon.start_search(repository="search-all", query_string="#event_simpleName=*", is_live=False, start="1d", timezone_offset_minutes=0),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
            else:
                if key == "StartSearchV1":
                    search_id = tests[key]["resources"].get("id", None)

        follow_up_tests = {
            "GetSearchStatusV1": falcon.get_search_status(repository="search-all", search_id=search_id),
            "GetSearchStatusV1": falcon.get_search_status(repository="search-all", id=search_id),
            "StopSearchV1": falcon.stop_search(repository="search-all", search_id=search_id)
        }
        for follow_key in follow_up_tests:
            if follow_up_tests[follow_key]["status_code"] not in AllowedResponses:
                error_checks = False

        fail_tests = {
            "UploadLookupV1-fail": falcon.upload_file(repository="search-all", lookup_file="tests/badfile.csv"),
            "UploadLookupV1-fail2": falcon.upload_file(repository="search-all"),
            "GetLookupV1-fail": falcon.get_file(),
            "GetLookupFromPackageWithNamespaceV1Fail": falcon.get_file_from_package_with_namespace(),
            "GetLookupFromPackageV1-fail": falcon.get_file_from_package(filename="manny",
                                                                        package="moe"
                                                                        ),
            "StartSearchV1-fail": falcon.start_search(search=test_search, is_live=False, start="1d", timezone_offset_minutes=0),
            "GetSearchStatusV1-fail": falcon.get_search_status(repository="search-all"),
            "StopSearchV1-fail": falcon.stop_search(repository="search-all")
        }
        for key in fail_tests:
            if fail_tests[key]["status_code"] != 500:
                error_checks = False
        # Test lookup file download
        # try:
        # Expanding result so we can retrieve the status code from a binary response
        binary_download_test = falcon.get_file(repository="search-all", filename="testfile.csv", expand_result=True)[0]
        # except Exception:
        #     pytest.skip("Skipping on failure")
        if binary_download_test not in AllowedResponses:
            error_checks = False
        # if not error_checks:
        #     pytest.skip("Skipping on failure")  # Skip on failure for now
        # Stream test
        result = falcon.get_file_from_package_with_namespace(repository="search-all",
                                                             filename="manny",
                                                             package="moe",
                                                             namespace="jack",
                                                             stream=True
                                                             )
        if not isinstance(result, Response):
            if result.status_code not in AllowedResponses:
                error_checks = False
        test_db = open("tests/test_dashboard.yml", "r", encoding="utf-8").read()
        more_tests = {
            "GetDashboardTemplate": falcon.get_dashboard_template(ids="12345678"),
            "CreateDashboardFromTemplate": falcon.create_dashboard_from_template(search_domain="all", name="whatever", yaml_template=test_db),
            "CreateDashboardFromTemplateFail": falcon.create_dashboard_from_template(search_domain="all", name="whatever"),
            "UpdateDashboardFromTemplate": falcon.update_dashboard_from_template(search_domain="all", name="whatever", yaml_template=test_db),
            "UpdateDashboardFromTemplateFail": falcon.update_dashboard_from_template(search_domain="all", name="whatever"),
            "DeleteDashboard": falcon.delete_dashboard(ids="12345678"),
            "GetLookupFile": falcon.get_lookup_file(ids="12345678"),
            "CreateLookupFile": falcon.create_lookup_file(search_domain="all", filename="testfile.yml", file=test_db),
            "CreateLookupFileFail": falcon.create_lookup_file(search_domain="all", filename="testfile.yml"),
            "UpdateLookupFile": falcon.update_lookup_file(search_domain="all", filename="testfile.yml", file=test_db),
            "UpdateLookupFileFail": falcon.update_lookup_file(search_domain="all", filename="testfile.yml"),
            "DeleteLookupFile": falcon.delete_lookup_file(ids="12345678"),
            "GetParserTemplate": falcon.get_parser_template(ids="12345678"),
            "CreateParserFromTemplate": falcon.create_parser_from_template(repository="whatever", name="whatever", yaml_template=test_db),
            "CreateParserFromTemplateFail": falcon.create_parser_from_template(repository="whatever", name="whatever"),
            "GetParser": falcon.get_parser(ids="12345678"),
            "CreateParser": falcon.create_parser(script=test_db, repository="whatever", fields_to_tag="bob,larry"),
            "UpdateParser": falcon.update_parser(script=test_db, repository="whatever", fields_to_tag="bob,larry", id="12345678"),
            "DeleteParser": falcon.delete_parser(ids="12345678"),
            "GetSavedQueryTemplate": falcon.get_saved_query_template(ids="12345678"),
            "CreateSavedQuery": falcon.create_saved_query(search_domain="all", yaml_template=test_db),
            "CreateSavedQueryFail": falcon.create_saved_query(search_domain="all"),
            "UpdateSavedQueryFromTemplate": falcon.update_saved_query_from_template(ids="12345678", search_domain="all", yaml_template=test_db),
            "UpdateSavedQueryFromTemplateFail": falcon.update_saved_query_from_template(ids="12345678", search_domain="all"),
            "DeleteSavedQuery": falcon.delete_saved_query(ids="12345678"),
            "ListDashboards": falcon.list_dashboards(limit="1"),
            "ListLookupFiles": falcon.list_lookup_files(limit="1"),
            "ListParsers": falcon.list_parsers(limit="1"),
            "ListSavedQueries": falcon.list_saved_queries(limit="1"),
        }

        for test in more_tests:
            if more_tests[test]["status_code"] not in AllowedResponses:
                error_checks = False
        return error_checks

    def test_all_functionality(self):
        assert self.run_all_tests() is True
