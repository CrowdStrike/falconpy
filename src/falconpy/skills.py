"""CrowdStrike Falcon Skills API interface class.

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
from typing import Dict, Union
from ._util import force_default, process_service_request, handle_single_argument, generate_error_result, params_to_keywords
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._skills import _skills_endpoints as Endpoints


class Skills(ServiceClass):
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
    def download_studio_skill(self: object,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Download a single skill blob as a zip archive.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/skills/EntitiesSkillsDownloadV2

        Keyword arguments
        -----------------
        id : str
            ID of the skill to download.
        include_deleted : bool
            Include deleted skills in the result. Defaults to false.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesSkillsDownloadV2",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_studio_skills(self: object,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve skill entities for the provided IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/skills/EntitiesSkillsV1

        Keyword arguments
        -----------------
        ids : list
            IDs of skills to retrieve.
        include_deleted : bool
            Include deleted skills in the result. Defaults to false.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesSkillsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_studio_skill(self: object,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update an existing skill with a new zip archive.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/skills/EntitiesSkillsUpdateV1

        Keyword arguments
        -----------------
        file_name : str
            Name to use for the uploaded file.
        id : str
            ID of the skill to update.
        skill_blob : str
            Updated skill zip archive.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        kwargs = params_to_keywords(["id", "skill_blob"],
                                    parameters,
                                    kwargs
                                    )
        file_name = kwargs.get("file_name", None)
        file_data = kwargs.get("skill_blob", None)
        if not file_data:
            return generate_error_result("You must provide a file to upload.", code=400)
        file_extended = {}
        if kwargs.get("id", None) is not None:
            file_extended["id"] = kwargs.get("id")
        file_uploads = []
        if file_data:
            file_uploads = [("skill_blob", (file_name, file_data))]
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesSkillsUpdateV1",
            data=file_extended,
            files=file_uploads
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def create_studio_skill(self: object,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Upload a new skill as a zip archive.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/skills/EntitiesSkillsCreateV1

        Keyword arguments
        -----------------
        file_name : str
            Name to use for the uploaded file.
        skill_blob : str
            Skill zip archive to upload.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        kwargs = params_to_keywords(["skill_blob"],
                                    parameters,
                                    kwargs
                                    )
        file_name = kwargs.get("file_name", None)
        file_data = kwargs.get("skill_blob", None)
        if not file_data:
            return generate_error_result("You must provide a file to upload.", code=400)
        file_extended = {}
        file_uploads = []
        if file_data:
            file_uploads = [("skill_blob", (file_name, file_data))]
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesSkillsCreateV1",
            data=file_extended,
            files=file_uploads
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_studio_skill(self: object,
                            *args,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete a skill by its ID.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/skills/EntitiesSkillsDeleteV1

        Keyword arguments
        -----------------
        id : str or list[str]
            ID of the skill to delete.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'id'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesSkillsDeleteV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_studio_skills(self: object,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query skills based on the provided filters.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/skills/QueriesSkillsV1

        Keyword arguments
        -----------------
        offset : int
            Starting index of overall result set from which to return ids.
        limit : int
            Number of IDs to return.
        sort : str
            Possible order by String.
            fields:
                  'name|asc'.         Ex:
        filter : str
            FQL query specifying the filter parameters.
        include_deleted : bool
            Include deleted skills in the result. Defaults to false.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueriesSkillsV1",
            keywords=kwargs,
            params=parameters
            )
    EntitiesSkillsDownloadV2 = download_studio_skill
    EntitiesSkillsV1 = get_studio_skills
    EntitiesSkillsUpdateV1 = update_studio_skill
    EntitiesSkillsCreateV1 = create_studio_skill
    EntitiesSkillsDeleteV1 = delete_studio_skill
    QueriesSkillsV1 = query_studio_skills
