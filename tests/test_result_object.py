"""
test_results.py -  This class tests the Results class
"""
import os
import sys
import pytest
import hashlib
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
# We'll use Hosts to retrieve data to test results with
from falconpy import (
    Hosts,
    Result,
    ExpandedResult,
    RegionSelectError,
    SSLDisabledWarning,
    BaseDictionary,
    RawBody,
    ResponseComponent,
    BaseResource,
    Errors,
    SampleUploads
    )

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
# Force debug logging here so we can test those code paths
falcon = Hosts(auth_object=config, debug=True)
samples = SampleUploads(auth_object=config, debug=True)
AllowedResponses = [200, 202, 429]  # Adding rate-limiting as an allowed response for now
_OBJECT: Result = None
_RATE_LIMITED: bool = False
rate_limited = pytest.mark.skipif(
    _RATE_LIMITED, reason="Rate limit met, skipping"
)
experimental = pytest.mark.xfail
_DATA = ["This", "is", "a", "test", "of", "the", "list", "functionality"]
_DICT_DATA = {"Thing1": "Not very helpful",
              "Thing2": "Extremely unhelpful",
              "Thing3": "Maliciously unhelpful"
              }



class SimpleResource(BaseResource):
    """Simple resource example"""
    pass


class TestResults:
    """
    Results Class test harness
    """
    @rate_limited
    @experimental
    def test_python_result_object(self):
        global _OBJECT, _RATE_LIMITED
        _OBJECT = Result(full=falcon.query_devices_by_filter(limit=50))
        if _OBJECT.status_code == 429:
            _RATE_LIMITED = True
        assert bool(_OBJECT.total)

    @rate_limited
    @experimental
    def test_property_offset(self):
        assert bool(_OBJECT.offset)

    @rate_limited
    @experimental
    def test_property_limit(self):
        assert bool(_OBJECT.limit)

    @rate_limited
    @experimental
    def test_property_query_time(self):
        assert bool(_OBJECT.query_time)

    @rate_limited
    @experimental
    def test_property_powered_by(self):
        assert bool(_OBJECT.powered_by)

    @rate_limited
    @experimental
    def test_property_trace_id(self):
        assert bool(_OBJECT.trace_id)

    @rate_limited
    @experimental
    def test_property_content_encoding(self):
        assert bool(_OBJECT.content_encoding)

    @rate_limited
    @experimental
    def test_property_content_length(self):
        assert bool(_OBJECT.content_length)

    @rate_limited
    @experimental
    def test_property_content_type(self):
        assert bool(_OBJECT.content_type)

    @rate_limited
    @experimental
    def test_property_date(self):
        assert bool(_OBJECT.date)

    @rate_limited
    @experimental
    def test_property_region(self):
        assert bool(_OBJECT.region)

    @rate_limited
    @experimental
    def test_property_ratelimit_limit(self):
        assert bool(_OBJECT.ratelimit_limit)

    @rate_limited
    @experimental
    def test_property_ratelimit_remaining(self):
        assert bool(_OBJECT.ratelimit_remaining)

    @rate_limited
    @experimental
    def test_property_based_result_expansion(self):
        assert bool(_OBJECT.tupled)

    @rate_limited
    @experimental
    def test_property_data(self):
        assert bool(_OBJECT.data)

    @rate_limited
    @experimental
    def test_property_full_return(self):
        assert bool(_OBJECT.full_return)

    @rate_limited
    @experimental
    def test_property_status_code(self):
        assert bool(_OBJECT.status_code)

    @rate_limited
    @experimental
    def test_property_meta_object(self):
        assert bool(not _OBJECT.meta_object)

    @rate_limited
    @experimental
    def test_property_headers_object(self):
        assert bool(not _OBJECT.headers_object)
    
    @rate_limited
    @experimental
    def test_property_meta_binary(self):
        assert bool(not _OBJECT.meta.binary)
    
    @rate_limited
    @experimental
    def test_property_meta_data(self):
        assert bool(_OBJECT.meta.data)
    
    @rate_limited
    @experimental
    def test_property_meta_expires_at(self):
        # QueryDevicesByFilter doesn't return `expires_at`
        _temp = Result(full=falcon.query_devices_by_filter_scroll(limit=50))
        assert bool(_temp.meta.expires_at)
    
    @rate_limited
    @experimental
    def test_property_meta_limit(self):
        assert bool(_OBJECT.meta.limit)
    
    @rate_limited
    @experimental
    def test_property_meta_offset(self):
        assert bool(_OBJECT.meta.offset)
    
    @rate_limited
    @experimental
    def test_property_meta_limit(self):
        assert bool(_OBJECT.meta.limit)
    
    @rate_limited
    @experimental
    def test_property_meta_pagination(self):
        assert bool(_OBJECT.meta.pagination)
    
    @rate_limited
    @experimental
    def test_property_meta_query_time(self):
        assert bool(_OBJECT.meta.query_time)
    
    @rate_limited
    @experimental
    def test_property_meta_powered_by(self):
        assert bool(_OBJECT.meta.powered_by)
    
    @rate_limited
    @experimental
    def test_property_meta_trace_id(self):
        assert bool(_OBJECT.meta.trace_id)

    @rate_limited
    @experimental
    def test_property_debug_mode(self):
        assert bool(falcon.debug)

    @rate_limited
    @experimental
    def test_property_headers_content_encoding(self):
        assert bool(_OBJECT.headers.content_encoding)

    @rate_limited
    @experimental
    def test_property_headers_content_length(self):
        assert bool(_OBJECT.headers.content_length)

    @rate_limited
    @experimental
    def test_property_headers_content_type(self):
        assert bool(_OBJECT.headers.content_type)

    @rate_limited
    @experimental
    def test_property_headers_date(self):
        assert bool(_OBJECT.headers.date)

    @rate_limited
    @experimental
    def test_property_headers_region(self):
        assert bool(_OBJECT.headers.region)

    @rate_limited
    @experimental
    def test_property_headers_ratelimit_limit(self):
        assert bool(_OBJECT.headers.ratelimit_limit)

    @rate_limited
    @experimental
    def test_property_headers_ratelimit_remaining(self):
        assert bool(_OBJECT.headers.ratelimit_remaining)

    @rate_limited
    @experimental
    def test_property_body(self):
        assert bool(_OBJECT.body)

    @rate_limited
    @experimental
    def test_property_length(self):
        assert bool(len(_OBJECT))

    @rate_limited
    @experimental
    def test_contains_search(self):
        search_for = _OBJECT.data[0]
        assert bool(search_for in _OBJECT)

    @rate_limited
    @experimental
    def test_object_repr(self):
        assert bool(str(_OBJECT))

    @rate_limited
    @experimental
    def test_prune(self):
        search_for = _OBJECT.data[0]
        assert(bool(len(_OBJECT.prune(search_for)) == 1))

    @rate_limited
    @experimental
    def test_deprecated_result_expansion(self):
        resp = _OBJECT.full_return
        assert bool(ExpandedResult()(resp.get("status_code"),
                                     resp.get("headers"),
                                     resp
                                     ))

    @rate_limited
    @experimental
    def test_forward_iteration(self):
        _success = False
        _count = 0
        for _ in _OBJECT:
            if _count > 2:
                _success = True
                break
            _count += 1

        assert _success

    @rate_limited
    @experimental
    def test_reverse_iteration(self):
        _success = False
        _count = 0
        for _ in reversed(_OBJECT):
            if _count > 2:
                _success = True
                break
            _count += 1


        assert _success

    @rate_limited
    @experimental
    def test_object_next(self):
        _success = False
        _success2 = False
        _success3 = False
        global _OBJECT
        try:
            while True:
                next(_OBJECT)
        except StopIteration:
            _success = True
        _success2 = bool(_OBJECT[2])
        # try to iterate an empty list
        _OBJECT = Result(full=falcon.query_devices(filter="hostname:'ThisWontMatch'"))
        try:
            while True:
                print(f"|{next(_OBJECT)}|")
        except StopIteration:
            _success3 = True

        assert bool(_success and _success2 and _success3)

    @rate_limited
    @experimental    
    def test_component_repr(self):
        assert bool(str(_OBJECT.headers))

    @rate_limited
    @experimental
    def test_bad_component_property(self):
        assert bool(not _OBJECT.headers.get_property("a_new_car"))

    @rate_limited
    @experimental
    def test_component_data(self):
        assert bool(_OBJECT.headers.data)

    @rate_limited
    @experimental
    def test_error_simple_response(self):
        try:
            raise RegionSelectError(code=418,
                                    message="Don't worry, this is only a test.",
                                    headers={"CrowdStrike": "WE STOP BREACHES"})
        except RegionSelectError as oopsies:
            assert bool(oopsies and oopsies.simple)

    @rate_limited
    @experimental
    def test_warning_simple_response(self):
        try:
            raise SSLDisabledWarning(code=418,
                                     message="SSL verification isn't really turned off. I mean... unless you did it?",
                                     headers={"CrowdStrike": "WE STOP BREACHES"})
        except SSLDisabledWarning as kerblammo:
            assert(bool(kerblammo and kerblammo.simple))

    @experimental
    def test_base_resource_iteration(self):
        count = 0
        for word in SimpleResource(data=_DATA):
            if count >= 2 and word == _DATA[count]:
                break
            count += 1
        assert bool(count)

    @experimental
    def test_base_resource_reverse_iteration(self):
        count = len(_DATA) - 1
        _success = False
        for word in reversed(SimpleResource(data=_DATA)):
            if count <= 1 and word == _DATA[count]:
                _success = True
                break
            count -= 1
        assert _success

    @experimental
    def test_base_resource_next(self):
        _resource = SimpleResource(data=_DATA)
        listlen = len(_resource)
        endmark = 2 if listlen >= 2 else listlen
        _success = False
        for count in range(0, endmark):
            _success = bool(next(_resource))
        assert bool(_success and count)

    @experimental
    def test_base_resource_next_stop(self):
        _success = False
        try:
            _success = bool(next(SimpleResource(data=[])))
        except StopIteration:
            _success = True
        assert _success

    @experimental
    def test_base_dictionary_iteration(self):
        _dictionary = BaseDictionary(data=_DICT_DATA)
        count = 0
        for _ in _dictionary:
            if count == 2:
                break
            count += 1
        assert bool(count)

    @experimental
    def test_base_dictionary_reverse_iteration(self):
        _dictionary = BaseDictionary(data=_DICT_DATA)
        count = len(_dictionary) -1
        for _ in reversed(_dictionary):
            if count == 3:
                break
            count -= 1
        assert bool(count and _dictionary["Thing1"])

    @experimental
    def test_base_dictionary_item_iteration(self):
        _dictionary = BaseDictionary(data=_DICT_DATA)
        count = 1
        _success = False
        for item, value in _dictionary.items():
            if count == 3:
                break
            if item and value is _DICT_DATA[item]:
                if item == f"Thing{count}":
                    _success = True
            count += 1

        assert bool(_success and _dictionary.data)

    @experimental
    def test_base_dictionary_next(self):
        _dictionary = BaseDictionary(data=_DICT_DATA)
        listlen = len(_dictionary)
        endmark = 2 if listlen >= 2 else listlen
        _success = False
        for count in range(0, endmark):
            _success = bool(next(_dictionary))
        assert bool(_success and count)

    @experimental
    def test_base_dictionary_next_stop(self):
        _success = False
        _dictionary = BaseDictionary(data={})
        try:
            _success = bool(next(_dictionary))
        except StopIteration:
            _success = True
        assert _success

    @experimental
    def test_raw_body_next(self):
        _dictionary = RawBody(data=_DICT_DATA)
        listlen = len(_dictionary)
        endmark = 2 if listlen >= 2 else listlen
        _success = False
        for count in range(0, endmark):
            _success = bool(next(_dictionary))
        assert bool(_success and count and _dictionary["Thing1"])

    @experimental
    def test_raw_body_reverse_iteration(self):
        _dictionary = RawBody(data=_DICT_DATA)
        count = len(_dictionary) -1
        for _ in reversed(_dictionary):
            if count == 3:
                break
            count -= 1
        assert bool(count and _dictionary["Thing2"])
    
    @experimental
    def test_response_component_data(self):
        thing = ResponseComponent(data=_DATA)
        assert thing.data

    @experimental
    def test_errors_fallback(self):
        thing = Errors(data=_DATA)
        assert thing.data

    @experimental
    def test_init_variations(self):
        _headers ={"X-Something-Something-Something": "Darkside"}
        _access_body = {"access_token": "OneSingularIndividualGoldenTicket"}
        result1 = Result(status_code=204, headers=_headers, body="  ")
        result2 = Result(status_code=204, headers=_headers, body=_access_body)
        assert bool(result1.full_return and result2.full_return)

    @experimental
    def test_retrieve_and_confirm_binary(self):
        hash1 = hashlib.sha256()
        with open("tests/testfile.png", 'rb') as file_to_hash:
            while True:
                data = file_to_hash.read(65536)
                if not data:
                    break
                hash1.update(data)
        hash1 = hash1.hexdigest()
        download_parts = samples.get_sample(hash1, expand_result=True)
        result: Result = Result(status_code=download_parts[0],
                                headers=download_parts[1],
                                body=download_parts[2]
                                )

        assert bool(result.full_return and result.binary)
