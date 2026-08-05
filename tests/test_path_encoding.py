# test_path_encoding.py
# Tests URL path-segment encoding for caller-supplied path parameters.
#
# Path parameters are declared as a single path segment in the endpoint tables.
# A value containing a forward slash or a dot-segment sequence must not be able
# to introduce additional segments, because requests/urllib3 normalize the path
# before transmission and would otherwise retarget the call to a different route
# under the same host, method and authentication token. Closes #1488.
#
# These tests are fully mocked -- no live credentials and no network access.
import os
import sys
from requests import Request
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# flake8: noqa=E402
from falconpy import APIHarness
from falconpy._util import encode_path_segment
from falconpy._util._functions import handle_path_variables
from falconpy._util._uber import scrub_target

# A value documented as one object identifier that tries to escape its segment.
TRAVERSAL = "../integration_tasks/9"
ASPM_ROUTE = "https://api.example/aspm-api-gateway/api/v1/group/{}"


def wire_url(built: str) -> str:
    """Return the URL requests would actually transmit, after normalization."""
    return Request("DELETE", built).prepare().url


class TestEncodePathSegment:
    """Cover the encode_path_segment helper directly."""

    def test_benign_identifiers_are_unchanged(self):
        """Unreserved identifiers must survive byte-for-byte."""
        for benign in ["9", "abc-123", "0f7a2b9c4e5d6a7b8c9d0e1f2a3b4c5d"]:
            assert encode_path_segment(benign) == benign

    def test_integers_are_coerced_without_encoding(self):
        """Numeric identifiers stringify cleanly."""
        assert encode_path_segment(9) == "9"
        assert encode_path_segment(0) == "0"

    def test_separators_are_escaped(self):
        """A slash must not survive as a path separator."""
        assert encode_path_segment("a/b") == "a%2Fb"
        assert encode_path_segment(TRAVERSAL) == "..%2Fintegration_tasks%2F9"

    def test_braces_are_escaped(self):
        """Braces must not survive into a subsequent str.format call."""
        assert encode_path_segment("{evil}") == "%7Bevil%7D"


class TestServiceClassPathEncoding:
    """handle_path_variables is the Service Class chokepoint."""

    def test_benign_value_is_unchanged(self):
        assert handle_path_variables({"path_id": "9"}, ASPM_ROUTE).endswith("/group/9")

    def test_traversal_stays_within_its_segment(self):
        built = handle_path_variables({"path_id": TRAVERSAL}, ASPM_ROUTE)
        assert "/group/" in wire_url(built)
        assert not wire_url(built).endswith("/api/v1/integration_tasks/9")

    def test_partition_zero_is_still_interpolated(self):
        """Zero is falsy but a legitimate partition value."""
        built = handle_path_variables({"partition": 0}, "https://api.example/streams/{}")
        assert built.endswith("/streams/0")


class TestUberPathEncoding:
    """scrub_target covers both the single-field and multi-field branches."""

    def test_traversal_stays_within_its_segment(self):
        built = scrub_target("DeleteGroup", ASPM_ROUTE, {"id": TRAVERSAL})
        assert "/group/" in wire_url(built)

    def test_multi_field_object_key_cannot_escape(self):
        route = ("https://api.example/customobjects/v1/collections"
                 "/{collection_name}/objects/{object_key}")
        built = scrub_target("GetObject", route,
                             {"collection_name": "c", "object_key": "../../schemas/v1"})
        assert "/objects/" in wire_url(built)


class TestLegacyHarnessPathEncoding:
    """The legacy APIHarness interpolates path variables in its own handlers."""

    def setup_method(self):
        self.falcon = APIHarness(client_id="testing", client_secret="testing")

    def test_image_id_cannot_escape(self):
        built = self.falcon._handle_container_image_id(
            "https://api.example/container/images/{}", {"image_id": "../../v1/admin"}
        )
        assert "/images/" in wire_url(built)

    def test_partition_cannot_escape(self):
        built = self.falcon._handle_partition(
            "https://api.example/streams/partition/{}", {"partition": "../../v1/admin"}
        )
        assert "/partition/" in wire_url(built)

    def test_distinct_field_cannot_escape(self):
        built = self.falcon._handle_distinct_field(
            "https://api.example/policy/distinct/{}", {"distinct_field": "../../v1/admin"}
        )
        assert "/distinct/" in wire_url(built)
