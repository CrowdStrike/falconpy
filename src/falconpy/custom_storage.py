"""Falcon Custom Storage API Interface Class.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
import json
from typing import Dict, Union
from ._util import process_service_request, force_default, generate_error_result
from ._service_class import ServiceClass
from ._endpoint._custom_storage import _custom_storage_endpoints as Endpoints


class CustomStorage(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (oauth2.py)
    """

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list(self, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """List the object keys in the specified collection in alphabetical order.

        HTTP Method: GET

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-storage/ListObjects

        Keyword arguments
        ----
        collection_name : string (required)
            The name of the collection to list objects for.
        end : string
            The ending key to use for the end of the listing.
        limit : integer
            The maximum number of results to return.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        start : string
            The starting key to begin listing from.

        This method only supports keywords for providing arguments.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        collection_name = kwargs.get("collection_name", None)
        if collection_name:
            # Pop the path variable from the keywords dictionary
            # before processing query string arguments.
            kwargs.pop("collection_name")
            returned = process_service_request(calling_object=self,
                                               endpoints=Endpoints,
                                               operation_id="ListObjects",
                                               keywords=kwargs,
                                               params=parameters,
                                               collection_name=collection_name
                                               )
        else:
            returned = generate_error_result("You must provide a collection_name "
                                             "argument in order to use this operation."
                                             )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def search(self, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Search for objects that match the specified filter creteria.

        Object metadata is returned, not actual objects.

        HTTP Method: POST

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-storage/SearchObjects

        Keyword arguments
        ----
        collection_name : string (required)
            The name of the collection to search.
        filter : string (required)
            The FQL formatted filter to use to limit returned results.
        limit : integer
            The maximum number of results to return.
        offset : integer
            The pagination offset to use for returned results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : string
            Sort order for returned results in FQL format.

        This method only supports keywords for providing arguments.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        collection_name = kwargs.get("collection_name", None)
        if collection_name:
            # Pop the path variable from the keywords dictionary
            # before processing query string arguments.
            kwargs.pop("collection_name")
            returned = process_service_request(calling_object=self,
                                               endpoints=Endpoints,
                                               operation_id="SearchObjects",
                                               keywords=kwargs,
                                               params=parameters,
                                               collection_name=collection_name
                                               )
        else:
            returned = generate_error_result("You must provide a collection_name "
                                             "argument in order to use this operation."
                                             )
        return returned

    def get(self, **kwargs) -> Union[bytes, Dict[str, Union[int, dict]]]:
        """Retrieve an object in binary format.

        HTTP Method: GET

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-storage/GetObject

        Keyword arguments
        ----
        collection_name : string (required)
            The name of the collection where the object resides.
        object_key : string (required)
            The key of the object to be retrieved.

        This method only supports keywords for providing arguments.

        Returns
        ----
        bytes or dict
            Binary (success) or Dictionary (failure) object containing API response.
        """
        collection_name = kwargs.get("collection_name", None)
        object_key = kwargs.get("object_key", None)
        if collection_name and object_key:
            # Pop the path variables from the keywords dictionary
            # before processing query string arguments.
            kwargs.pop("collection_name")
            kwargs.pop("object_key")
            returned = process_service_request(calling_object=self,
                                               endpoints=Endpoints,
                                               operation_id="GetObject",
                                               keywords=kwargs,
                                               collection_name=collection_name,
                                               object_key=object_key
                                               )
        else:
            returned = generate_error_result("You must provide a collection_name and an "
                                             "object_key argument in order to use this operation."
                                             )
        return returned

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def upload(self, body: dict = None, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Upload a new or overwrite an existing object at the given key.

        HTTP Method: PUT

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-storage/PutObject

        Keyword arguments
        ----
        body : binary [application/octet-stream] (required)
            The object to be uploaded.
        collection_name : string (required)
            The name of the collection to upload to.
        dry_run : boolean
            Boolean flag indicating if this is a dry run. If set to True, the
            request is validated if it would succeed, but not actually executed.
        object_key : string (required)
            The key of the object to be uploaded.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        schema_version : string
            The version of the collection schema.

        This method only supports keywords for providing arguments.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        collection_name = kwargs.get("collection_name", None)
        object_key = kwargs.get("object_key", None)
        if collection_name and object_key:
            # Pop the path variables from the keywords dictionary
            # before processing query string arguments.
            kwargs.pop("collection_name")
            kwargs.pop("object_key")
            # Create a copy of our default header dictionary
            header_payload = json.loads(json.dumps(self.headers))
            # Set our content-type header
            header_payload["Content-Type"] = "application/octet-stream"
            returned = process_service_request(calling_object=self,
                                               endpoints=Endpoints,
                                               operation_id="PutObject",
                                               keywords=kwargs,
                                               body=body,
                                               params=parameters,
                                               collection_name=collection_name,
                                               object_key=object_key
                                               )
        else:
            returned = generate_error_result("You must provide a collection_name and an "
                                             "object_key argument in order to use this operation."
                                             )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete(self, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Delete an existing object at the given key.

        HTTP Method: DELETE

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-storage/DeleteObject

        Keyword arguments
        ----
        collection_name : string (required)
            The name of the collection to upload to.
        dry_run : boolean
            Boolean flag indicating if this is a dry run. If set to True, the
            request is validated if it would succeed, but not actually executed.
        object_key : string (required)
            The key of the object to be uploaded.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        collection_name = kwargs.get("collection_name", None)
        object_key = kwargs.get("object_key", None)
        if collection_name and object_key:
            # Pop the path variables from the keywords dictionary
            # before processing query string arguments.
            kwargs.pop("collection_name")
            kwargs.pop("object_key")
            returned = process_service_request(calling_object=self,
                                               endpoints=Endpoints,
                                               operation_id="DeleteObject",
                                               keywords=kwargs,
                                               params=parameters,
                                               collection_name=collection_name,
                                               object_key=object_key
                                               )
        else:
            returned = generate_error_result("You must provide a collection_name and an "
                                             "object_key argument in order to use this operation."
                                             )
        return returned

    def metadata(self, **kwargs) -> Dict[str, Union[int, dict]]:
        """Retrieve the metadata for a specified object.

        HTTP Method: GET

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-storage/GetObjectMetadata

        Keyword arguments
        ----
        collection_name : string (required)
            The name of the collection where the object resides.
        object_key : string (required)
            The key of the object to be retrieved.

        This method only supports keywords for providing arguments.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        collection_name = kwargs.get("collection_name", None)
        object_key = kwargs.get("object_key", None)
        if collection_name and object_key:
            # Pop the path variables from the keywords dictionary
            # before processing query string arguments.
            kwargs.pop("collection_name")
            kwargs.pop("object_key")
            returned = process_service_request(calling_object=self,
                                               endpoints=Endpoints,
                                               operation_id="GetObjectMetadata",
                                               keywords=kwargs,
                                               collection_name=collection_name,
                                               object_key=object_key
                                               )
        else:
            returned = generate_error_result("You must provide a collection_name and an "
                                             "object_key argument in order to use this operation."
                                             )
        return returned

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes.
    ListObjects = list
    SearchObjects = search
    GetObject = get
    PutObject = upload
    DeleteObject = delete
    GetObjectMetadata = metadata
