"""
test_results.py -  This class tests the Results class
"""
import os
import sys
import pytest
import hashlib
import warnings
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
# We'll use Hosts to retrieve data to test results with
from falconpy import (
    Hosts,
    CloudConnectAWS,
    Result,
    APIError,
    RegionSelectError,
    SSLDisabledWarning,
    BaseDictionary,
    RawBody,
    ResponseComponent,
    BaseResource,
    Errors,
    SampleUploads,
    CSPMRegistration,
    UnnecessaryEncodingUsed,
    DeprecatedOperation,
    DeprecatedClass,
    SDKDeprecationWarning
    )
from falconpy._result._base_dictionary import UnsupportedPythonVersion

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
# Force debug logging here so we can test those code paths
falcon = Hosts(auth_object=config, debug=True, pythonic=True)
#samples = SampleUploads(auth_object=config, debug=True, pythonic=True)
AllowedResponses = [200, 202, 429]  # Adding rate-limiting as an allowed response for now
_OBJECT: Result = None
_RATE_LIMITED: bool = False
not_supported = pytest.mark.skipif(
    sys.version_info.minor <= 7, reason="Experimental functionality unavailable in this version of Python."
)
experimental = pytest.mark.xfail
_DATA = ["This", "is", "a", "test", "of", "the", "list", "functionality"]
_DICT_DATA = {"Thing1": "Not very helpful",
              "Thing2": "Extremely unhelpful",
              "Thing3": "Maliciously unhelpful"
              }
_SAMPLES: SampleUploads = None



class SimpleResource(BaseResource):
    """Simple resource example"""
    pass


class TestResults:
    """
    Results Class test harness
    """

    @not_supported
    def test_python_result_object(self):
        global _OBJECT, _RATE_LIMITED
        # _OBJECT = Result(full=falcon.query_devices_by_filter(limit=50))
        try:
            _OBJECT = falcon.query_devices_by_filter(limit=50)
        except APIError as api_error:
            if api_error.code == 429:
                _RATE_LIMITED = True
                pytest.skip("Rate limited")
        assert bool(_OBJECT.total)


    @not_supported
    def test_property_offset(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.offset)


    @not_supported
    def test_property_limit(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.limit)


    @not_supported
    def test_property_query_time(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.query_time)


    @not_supported
    def test_property_powered_by(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.powered_by)


    @not_supported
    def test_property_trace_id(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.trace_id)


    @not_supported
    def test_property_content_encoding(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.content_encoding)


    @not_supported
    def test_property_content_length(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.content_length)


    @not_supported
    def test_property_content_type(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.content_type)


    @not_supported
    def test_property_date(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.date)


    @not_supported
    def test_property_region(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.region)


    @not_supported
    def test_property_ratelimit_limit(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.ratelimit_limit)


    @not_supported
    def test_property_ratelimit_remaining(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.ratelimit_remaining)


    @not_supported
    def test_property_based_result_expansion(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.tupled)


    @not_supported
    def test_property_data(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.data)


    @not_supported
    def test_property_full_return(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.full_return)


    @not_supported
    def test_property_status_code(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.status_code)


    @not_supported
    def test_property_meta_object(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(not _OBJECT.meta_object)


    @not_supported
    def test_property_headers_object(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(not _OBJECT.headers_object)
    

    @not_supported
    def test_property_meta_binary(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(not _OBJECT.meta.binary)
    

    @not_supported
    def test_property_meta_data(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.meta.data)
    

    @not_supported
    def test_property_meta_expires_at(self):
        # QueryDevicesByFilter doesn't return `expires_at`
        # _temp = Result(full=falcon.query_devices_by_filter_scroll(limit=50))
        global _RATE_LIMITED
        try:
            _temp = falcon.query_devices_by_filter_scroll(limit=50)
        except APIError as api_error:
            if api_error.code == 429:
                _RATE_LIMITED = True
                pytest.skip("Rate limited")
        if _RATE_LIMITED:
            pytest.skip("Rate limited")                
        assert bool(_temp.meta.expires_at)
    

    @not_supported
    def test_property_meta_limit(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.meta.limit)
    

    @not_supported
    def test_property_meta_offset(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.meta.offset)
    
    
    @not_supported
    # def test_property_meta_limit(self):
    #     assert bool(_OBJECT.meta.limit)
    

    @not_supported
    def test_property_meta_pagination(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.meta.pagination)
    

    @not_supported
    def test_property_meta_query_time(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.meta.query_time)
    

    @not_supported
    def test_property_meta_powered_by(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.meta.powered_by)
    

    @not_supported
    def test_property_meta_trace_id(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.meta.trace_id)


    @not_supported
    def test_property_debug_mode(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(falcon.debug)


    @not_supported
    def test_property_headers_content_encoding(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.headers.content_encoding)


    @not_supported
    def test_property_headers_content_length(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.headers.content_length)


    @not_supported
    def test_property_headers_content_type(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.headers.content_type)


    @not_supported
    def test_property_headers_date(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.headers.date)


    @not_supported
    def test_property_headers_region(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.headers.region)


    @not_supported
    def test_property_headers_ratelimit_limit(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.headers.ratelimit_limit)


    @not_supported
    def test_property_headers_ratelimit_remaining(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.headers.ratelimit_remaining)


    @not_supported
    def test_property_body(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.body)


    @not_supported
    def test_property_length(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(len(_OBJECT))


    @not_supported
    def test_contains_search(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")
        search_for = _OBJECT.data[0]
 
        assert bool(search_for in _OBJECT)


    @not_supported
    def test_object_repr(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(str(_OBJECT))


    @not_supported
    def test_prune(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")
        search_for = _OBJECT.data[0]

        assert(bool(len(_OBJECT.prune(search_for)) == 1))


    @not_supported
    def test_deprecated_result_expansion(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")
        resp = _OBJECT.tupled
        assert bool(isinstance(resp, tuple))
        # resp = _OBJECT.full_return
        # assert bool(ExpandedResult()(resp.get("status_code"),
        #                              resp.get("headers"),
        #                              resp
        #                              ))


    @not_supported
    def test_forward_iteration(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")
        _success = False
        _count = 0
        for _ in _OBJECT:
            if _:
                _success = True
                break
            _count += 1
        assert bool(_success)


    @not_supported
    def test_reverse_iteration(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")
        _success = False
        _count = 0
        for _ in reversed(_OBJECT):
            if _:
                _success = True
                break
            _count += 1



        assert bool(_success)



    @not_supported
    def test_bad_component_property(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")
        assert bool(not _OBJECT.headers.get_property("a_new_car"))


    @not_supported
    def test_component_repr(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(str(_OBJECT.headers))



    @not_supported
    def test_component_data(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")        
        assert bool(_OBJECT.headers.data)


    @not_supported
    def test_object_next(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")
        _success = False
        _success2 = False
        _success3 = False
        global _OBJECT
        try:
            while True:
                next(_OBJECT)
        except StopIteration:
            _success = True
        _success2 = bool(_OBJECT[0])
        # try to iterate an empty list
        _OBJECT = Result(full=falcon.query_devices(filter="hostname:'ThisWontMatch'"))
        try:
            while True:
                print(f"|{next(_OBJECT)}|")
        except StopIteration:
            _success3 = True

        assert bool((_success and _success2 and _success3))

    @not_supported
    def test_error_simple_response(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")
        try:
            raise RegionSelectError(code=418,
                                    message="Don't worry, this is only a test.",
                                    headers={"CrowdStrike": "WE STOP BREACHES"})
        except RegionSelectError as oopsies:
            assert bool((oopsies and oopsies.simple))


    @not_supported
    def test_warning_simple_response(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")
        try:
            raise SSLDisabledWarning(code=418,
                                     message="SSL verification isn't really turned off. I mean... unless you did it?",
                                     headers={"CrowdStrike": "WE STOP BREACHES"})
        except SSLDisabledWarning as kerblammo:
            assert bool((kerblammo and kerblammo.simple))

    @not_supported
    def test_base_resource_iteration(self):
        count = 0
        for word in SimpleResource(data=_DATA):
            if count >= 2 and word == _DATA[count]:
                break
            count += 1
        if _RATE_LIMITED:
            pytest.skip("Rate limited")            
        assert bool(count)

    @not_supported
    def test_base_resource_reverse_iteration(self):
        count = len(_DATA) - 1
        _success = False
        for word in reversed(SimpleResource(data=_DATA)):
            if count <= 1 and word == _DATA[count]:
                _success = True
                break
            count -= 1
        if _RATE_LIMITED:
            pytest.skip("Rate limited")            
        assert (_success)

    @not_supported
    def test_base_resource_next(self):
        _resource = SimpleResource(data=_DATA)
        listlen = len(_resource)
        endmark = 2 if listlen >= 2 else listlen
        _success = False
        for count in range(0, endmark):
            _success = bool(next(_resource))
        if _RATE_LIMITED:
            pytest.skip("Rate limited")            
        assert bool((_success and count))

    @not_supported
    def test_base_resource_next_stop_empty(self):
        _success = False
        try:
            _success = bool(next(SimpleResource(data=[])))
        except StopIteration:
            _success = True
        if _RATE_LIMITED:
            pytest.skip("Rate limited")            
        assert bool(_success)

    @not_supported
    def test_base_resource_next_stop(self):
        _success = False
        try:
            _resource = SimpleResource(data=["Just One Thing"])
            for _ in range(0, 2):
                _success = bool(next(_resource))
        except StopIteration:
            _success = True
        if _RATE_LIMITED:
            pytest.skip("Rate limited")            
        assert bool(_success)

    @not_supported
    def test_base_dictionary_iteration(self):
        _dictionary = BaseDictionary(data=_DICT_DATA)
        count = 0
        for _ in _dictionary:
            if count == 2:
                break
            count += 1
        if _RATE_LIMITED:
            pytest.skip("Rate limited")            
        assert bool(count)

    @not_supported
    def test_base_dictionary_reverse_iteration(self):
        _success = False
        try:
            _dictionary = BaseDictionary(data=_DICT_DATA)
            count = len(_dictionary) -1
            for _ in reversed(_dictionary):
                if count == 3:
                    break
                count -= 1
            _success = bool(count and _dictionary["Thing1"])
        except UnsupportedPythonVersion:
            _success = True

        if _RATE_LIMITED:
            pytest.skip("Rate limited")
        assert bool(_success)

    @not_supported
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

        if _RATE_LIMITED:
            pytest.skip("Rate limited")
        assert bool((_success and _dictionary.data))

    @not_supported
    def test_base_dictionary_next(self):
        _dictionary = BaseDictionary(data=_DICT_DATA)
        listlen = len(_dictionary)
        endmark = 2 if listlen >= 2 else listlen
        _success = False
        for count in range(0, endmark):
            _success = bool(next(_dictionary))
        if _RATE_LIMITED:
            pytest.skip("Rate limited")            
        assert bool((_success and count))

    @not_supported
    def test_base_dictionary_next_stop(self):
        _success = False
        _dictionary = BaseDictionary(data={})
        try:
            _success = bool(next(_dictionary))
        except StopIteration:
            _success = True
        if _RATE_LIMITED:
            pytest.skip("Rate limited")            
        assert bool(_success)

    @not_supported
    def test_raw_body_next(self):
        _dictionary = RawBody(data=_DICT_DATA)
        listlen = len(_dictionary)
        endmark = 2 if listlen >= 2 else listlen
        _success = False
        for count in range(0, endmark):
            _success = bool(next(_dictionary))
        if _RATE_LIMITED:
            pytest.skip("Rate limited")            
        assert bool((_success and count and _dictionary["Thing1"]))

    @not_supported
    def test_raw_body_reverse_iteration(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")
        _success = False
        try:
            _dictionary = RawBody(data=_DICT_DATA)
            count = len(_dictionary) -1
            for _ in reversed(_dictionary):
                if count == 3:
                    break
                count -= 1
            _success = bool(count and _dictionary["Thing2"])
        except UnsupportedPythonVersion:
            _success = True

        assert bool(_success)
    
    @not_supported
    def test_response_component_data(self):
        thing = ResponseComponent(data=_DATA)
        assert thing.data

    @not_supported
    def test_errors_fallback(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")
        thing = Errors(data=_DATA)

        assert bool(thing.data)

    @not_supported
    def test_init_variations(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")
        _headers ={"X-Something-Something-Something": "Darkside"}
        _access_body = {"access_token": "OneSingularIndividualGoldenTicket"}
        result1 = Result(status_code=204, headers=_headers, body="  ")
        result2 = Result(status_code=204, headers=_headers, body=_access_body)

        assert bool((result1.full_return and result2.full_return))


    @not_supported
    def test_retrieve_and_confirm_binary(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")
        global _SAMPLES
        _SAMPLES = SampleUploads(auth_object=config, pythonic=True, debug=True)

        hash1 = hashlib.sha256()
        with open("tests/testfile.png", 'rb') as file_to_hash:
            while True:
                data = file_to_hash.read(65536)
                if not data:
                    break
                hash1.update(data)
        hash1 = hash1.hexdigest()
        # download_parts = _SAMPLES.get_sample(hash1, expand_result=True)
        # result: Result = Result(status_code=download_parts[0],
        #                         headers=download_parts[1],
        #                         body=download_parts[2]
        #                         )
        #print(_SAMPLES.get_sample(hash1))
        try:
            result: Result = _SAMPLES.get_sample(hash1)
        except APIError as not_found:
            pytest.skip(not_found.message)
        #print(result)

        assert bool((result.full_return and result.binary))


    @not_supported
    def test_pythonic_error(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")
        _success = False
        try:
            _SAMPLES.get_sample("ThisIDDoesNotExit")
        except APIError:
            _success = True

        assert bool(_success)

    @not_supported
    def test_batch_init_id_without_a_session(self):
        if _RATE_LIMITED:
            pytest.skip("Rate limited")
        test_object: Result = Result(status_code=200, headers={"someheader": "somevalue"}, body={"batch_id": "123456"})
        assert bool(test_object.full_return.get("body", {}).get("batch_id")=="123456")

    @not_supported
    @pytest.mark.skipif("us-2" in config.base_url, reason="This unit test is not supported in US-2.")
    def test_unusual_response_formatting(self):
        _returned = False
        cspm = CSPMRegistration(auth_object=config)
        try:
            result = cspm.get_configuration_detections(limit=1)["body"]["resources"]
        except KeyError:
            result = Result(status_code=200, headers={}, body={"something": "different"}).full_return
        if isinstance(result, dict):
            _returned = True
        assert _returned

    @not_supported
    def test_unnecessary_encoding_used_warning(self):
        with pytest.warns(UnnecessaryEncodingUsed):
            # warnings.warn("Debug", UnnecessaryEncodingUsed)
            _success = True
            try:
                hosts = Hosts(auth_object=config, pythonic=True)
                hosts.query_devices_by_filter_scroll(filter="hostname%3A%27falconpy%27")
            except APIError:
                _success = True
            hosts = Hosts(auth_object=hosts, pythonic=False)
            hosts.query_devices_by_filter_scroll(filter="hostname%3A%27falconpy%27")
            assert _success

    @not_supported
    @pytest.mark.skipif(config.base_url != "https://api.crowdstrike.com", reason="This unit test is only supported in US-1.")
    def test_pythonic_deprecation_warnings(self):
        _success = False
        with pytest.warns(SDKDeprecationWarning):
            warnings.warn(SDKDeprecationWarning(message="This is a generic deprecation warning", code=187))
        with pytest.warns(DeprecatedClass):
            warnings.warn(DeprecatedClass(code=187))
        with pytest.warns(DeprecatedOperation):
            warnings.warn(DeprecatedOperation(code=187))
        with pytest.warns(DeprecatedClass):
            try:
                old_discover = CloudConnectAWS(auth_object=config, pythonic=True)
            except APIError:
                pass

        with pytest.warns(DeprecatedOperation):
            try:
                old_discover.get_aws_settings()
                _success = True
            except APIError as bad_class:
                if bad_class.code == 500:
                    _success = True  # This op is fully deprecated

        assert _success
