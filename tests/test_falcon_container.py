"""
test_falcon_container.py - This class tests the falcon_container service class
"""
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import FalconContainer, APIHarness, APIHarnessV2

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = FalconContainer(auth_object=config, timeout=3)
uber = APIHarness(client_id=falcon.auth_object.creds["client_id"],
                  client_secret=falcon.auth_object.creds["client_secret"],
                  base_url=falcon.auth_object.base_url,
                  timeout=3
                  )
uber2 = APIHarnessV2(client_id=falcon.auth_object.creds["client_id"],
                     client_secret=falcon.auth_object.creds["client_secret"],
                     base_url=falcon.auth_object.base_url,
                     timeout=3
                     )
AllowedResponses = [200, 201, 204, 400, 403, 404, 429, 500, 502]  # Allowing no content returned as code paths are confirmed

SCAN_INVENTORY_SAMPLE_PAYLOAD = {
  "agent_uuid": "string",
  "agent_version": "string",
  "agent_version_hash": "string",
  "cluster_id": "string",
  "cluster_name": "string",
  "container_id": "string",
  "ephemeral_scan": True,
  "helm_version": "string",
  "high_entropy_strings": [
    {
      "LayerHash": "string",
      "LayerIndex": 0,
      "Path": "string",
      "Strings": [
        {
          "Line": 0,
          "RegexName": "string",
          "String": "string"
        }
      ]
    }
  ],
  "host_ip": "string",
  "host_name": "string",
  "inventory": {
    "ApplicationPackages": [
      {
        "libraries": [
          {
            "Hash": "string",
            "LayerHash": "string",
            "LayerIndex": 0,
            "License": "string",
            "Name": "string",
            "Path": "string",
            "Version": "string",
            "ai_related": True
          }
        ],
        "type": 0
      }
    ],
    "Config": {
      "architecture": "string",
      "author": "string",
      "config": {
        "ArgsEscaped": True,
        "Cmd": [
          "string"
        ],
        "Entrypoint": [
          "string"
        ],
        "Env": [
          "string"
        ],
        "ExposedPorts": {},
        "Labels": {
          "additionalProp1": "string",
          "additionalProp2": "string",
          "additionalProp3": "string"
        },
        "StopSignal": "string",
        "User": "string",
        "Volumes": {},
        "WorkingDir": "string"
      },
      "created": "2025-07-08T08:58:33.373Z",
      "history": [
        {
          "author": "string",
          "comment": "string",
          "created": "2025-07-08T08:58:33.373Z",
          "created_by": "string",
          "empty_layer": True
        }
      ],
      "os": "string",
      "os.features": [
        "string"
      ],
      "os.version": "string",
      "rootfs": {
        "diff_ids": [
          "string"
        ],
        "type": "string"
      },
      "variant": "string"
    },
    "ConfigInfo": {
      "Cmd": [
        "string"
      ],
      "Entrypoint": [
        "string"
      ],
      "Env": [
        "string"
      ],
      "ExposedPorts": {},
      "Labels": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "StopSignal": "string",
      "User": "string",
      "Volumes": {},
      "WorkingDir": "string"
    },
    "ELFBinaries": [
      {
        "Details": {},
        "Hash": "string",
        "LayerHash": "string",
        "LayerIndex": 0,
        "Malicious": True,
        "Path": "string",
        "Permissions": "string",
        "Size": 0
      }
    ],
    "ImageInfo": {
      "Architecture": "string",
      "CreatedAt": "string",
      "Digest": "string",
      "ID": "string",
      "Registry": "string",
      "Repository": "string",
      "Size": 0,
      "Tag": "string",
      "config_s3_key": "string",
      "manifest_s3_key": "string",
      "scan_request_s3_key": "string",
      "source": "string"
    },
    "InventoryEngineInfo": {
      "CWPPScannerVersion": "string",
      "CollectedAt": "string",
      "EngineVersion": "string",
      "MalwareMetadata": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      }
    },
    "Layers": [
      {
        "CreatedAt": "string",
        "CreatedBy": "string",
        "Digest": "string",
        "Size": 0,
        "layer_inventory_s3_key": "string",
        "layer_reference_key": "string",
        "layer_reference_type": 0,
        "type": 0
      }
    ],
    "MLModels": [
      {
        "Details": {},
        "DetectionName": "string",
        "Hash": "string",
        "LayerHash": "string",
        "LayerIndex": 0,
        "Malicious": True,
        "Path": "string",
        "Size": 0
      }
    ],
    "Manifest": {
      "config": {
        "annotations": {
          "additionalProp1": "string",
          "additionalProp2": "string",
          "additionalProp3": "string"
        },
        "digest": "string",
        "mediaType": "string",
        "platform": {
          "architecture": "string",
          "os": "string",
          "os.features": [
            "string"
          ],
          "os.version": "string",
          "variant": "string"
        },
        "size": 0,
        "urls": [
          "string"
        ]
      },
      "layers": [
        {
          "annotations": {
            "additionalProp1": "string",
            "additionalProp2": "string",
            "additionalProp3": "string"
          },
          "digest": "string",
          "mediaType": "string",
          "platform": {
            "architecture": "string",
            "os": "string",
            "os.features": [
              "string"
            ],
            "os.version": "string",
            "variant": "string"
          },
          "size": 0,
          "urls": [
            "string"
          ]
        }
      ],
      "mediaType": "string",
      "schemaVersion": 0
    },
    "OSInfo": {
      "Name": "string",
      "Version": "string"
    },
    "Packages": [
      {
        "LayerHash": "string",
        "LayerIndex": 0,
        "MajorVersion": "string",
        "PackageHash": "string",
        "PackageProvider": "string",
        "PackageSource": "string",
        "Product": "string",
        "SoftwareArchitecture": "string",
        "Status": "string",
        "Vendor": "string"
      }
    ],
    "ai_related": True,
    "high_entropy_s3_file_exists": True,
    "interesting_strings": [
      {
        "LayerHash": "string",
        "LayerIndex": 0,
        "Path": "string",
        "Strings": [
          {
            "Line": 0,
            "RegexName": "string",
            "String": "string"
          }
        ]
      }
    ],
    "whiteout_files": [
      "string"
    ]
  },
  "original_image_name": "string",
  "pod_id": "string",
  "pod_name": "string",
  "pod_namespace": "string",
  "runmode": "string",
  "runtime_type": "string",
  "scan_request": {
    "Config": {
      "architecture": "string",
      "author": "string",
      "config": {
        "ArgsEscaped": True,
        "Cmd": [
          "string"
        ],
        "Entrypoint": [
          "string"
        ],
        "Env": [
          "string"
        ],
        "ExposedPorts": {},
        "Labels": {
          "additionalProp1": "string",
          "additionalProp2": "string",
          "additionalProp3": "string"
        },
        "StopSignal": "string",
        "User": "string",
        "Volumes": {},
        "WorkingDir": "string"
      },
      "created": "2025-07-08T08:58:33.373Z",
      "history": [
        {
          "author": "string",
          "comment": "string",
          "created": "2025-07-08T08:58:33.373Z",
          "created_by": "string",
          "empty_layer": True
        }
      ],
      "os": "string",
      "os.features": [
        "string"
      ],
      "os.version": "string",
      "rootfs": {
        "diff_ids": [
          "string"
        ],
        "type": "string"
      },
      "variant": "string"
    },
    "ConfigInfo": {
      "Cmd": [
        "string"
      ],
      "Entrypoint": [
        "string"
      ],
      "Env": [
        "string"
      ],
      "ExposedPorts": {},
      "Labels": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "StopSignal": "string",
      "User": "string",
      "Volumes": {},
      "WorkingDir": "string"
    },
    "ImageInfo": {
      "Architecture": "string",
      "CreatedAt": "string",
      "Digest": "string",
      "ID": "string",
      "Registry": "string",
      "Repository": "string",
      "Size": 0,
      "Tag": "string",
      "config_s3_key": "string",
      "manifest_s3_key": "string",
      "scan_request_s3_key": "string",
      "source": "string"
    },
    "ImageMetadata": {
      "image_metadata_config_s3_key": "string",
      "image_metadata_high_entropy_strings_s3_key": "string",
      "image_metadata_image_inventory_s3_key": "string",
      "image_metadata_image_inventory_s3_path": "string",
      "image_metadata_manifest_s3_key": "string",
      "image_metadata_scan_report_s3_key": "string"
    },
    "Layers": [
      {
        "CreatedAt": "string",
        "CreatedBy": "string",
        "Digest": "string",
        "Size": 0,
        "layer_inventory_s3_key": "string",
        "layer_reference_key": "string",
        "layer_reference_type": 0,
        "type": 0
      }
    ],
    "Manifest": {
      "config": {
        "annotations": {
          "additionalProp1": "string",
          "additionalProp2": "string",
          "additionalProp3": "string"
        },
        "digest": "string",
        "mediaType": "string",
        "platform": {
          "architecture": "string",
          "os": "string",
          "os.features": [
            "string"
          ],
          "os.version": "string",
          "variant": "string"
        },
        "size": 0,
        "urls": [
          "string"
        ]
      },
      "layers": [
        {
          "annotations": {
            "additionalProp1": "string",
            "additionalProp2": "string",
            "additionalProp3": "string"
          },
          "digest": "string",
          "mediaType": "string",
          "platform": {
            "architecture": "string",
            "os": "string",
            "os.features": [
              "string"
            ],
            "os.version": "string",
            "variant": "string"
          },
          "size": 0,
          "urls": [
            "string"
          ]
        }
      ],
      "mediaType": "string",
      "schemaVersion": 0
    },
    "ScanInfo": {
      "CorrelationUUID": "string",
      "RequestedAt": "string",
      "ScanUUID": "string",
      "UserUUID": "string",
      "Username": "string",
      "cid": "string"
    },
    "high_entropy_strings_s3_key": "string",
    "image_inventory_s3_key": "string",
    "layer_inventory_s3_key": "string",
    "scan_report_s3_key": "string",
    "scan_request_s3_key": "string"
  }
}

class TestFalconContainer:
    def run_tests(self):
        error_checks = True

        tests = {
            "GetAssessment": falcon.get_assessment(repository="misp", tag="latest"),
            "GetCombinedImages": falcon.get_combined_images(),
            "DeleteImageDetails": falcon.delete_image_details("whatever"),
            "ImageMatchesPolicy": falcon.image_matches_policy(repository="whatever", tag="whatever", body={}),
            "GetAssessmentUber": uber.command("GetImageAssessmentReport", repository="misp", tag="latest"),
            "DeleteImageDetailsUber": uber.command("DeleteImageDetails", image_id="12345678"),
            "ImageMatchesPolicyUber": uber.command("ImageMatchesPolicy", repository="whatever", tag="whatever"),
            "GetAssessmentUber2": uber2.command("GetImageAssessmentReport", repository="misp", tag="latest"),
            "DeleteImageDetailsUber2": uber2.command("DeleteImageDetails", image_id="12345678"),
            "ImageMatchesPolicyUber2": uber2.command("ImageMatchesPolicy", repository="whatever", tag="whatever"),
            "read_image_vulnerabilities": falcon.read_image_vulnerabilities(osversion="Windows", packages={"LayerIndex": 1}),
            "ReadRegistryEntities": falcon.read_registry_entities(),
            "ReadRegistryEntitiesByUUID": falcon.read_registry_entities_by_uuid(ids="12345678"),
            "DeleteRegistryEntities": falcon.delete_registry_entities(ids="12345678"),
            "UpdateRegistryEntities": falcon.update_registry_entities(credential={}, type="gcr", url="https://whatevs",
                                                                      url_uniqueness_key="banana", user_defined_alias="BoB",
                                                                      details={"aws_iam_role":"aws:arn::whatevs", "aws_external_id": "yellow"}
                                                                      ),
            "CreateRegistryEntities": falcon.create_registry_entities(type="github", url="https://somewheres", username="larry",
                                                                      password="top_secret"),
            "QueryExportJobs": falcon.query_export_jobs(filter="whatever"),
            "DownloadExportFile": falcon.download_export_file(id="12345678"),
            "ReadExportJobs": falcon.read_export_jobs(ids="12345678"),
            "LaunchExportJob": falcon.launch_export_job(format="json", resource="assets.clusters"),
            "HeadImageScanInventory": falcon.get_scan_headers(),
            "PostImageScanInventory": falcon.scan_inventory(**SCAN_INVENTORY_SAMPLE_PAYLOAD),
            "PolicyChecks": falcon.check_prevention_policies(),
            "GetReportByReference": falcon.get_report_by_reference(),
            "GetReportByScanID": falcon.get_report_by_id()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(tests[key])
                # print(f"{key} operation returned a {tests[key]['status_code']} status code")

        return error_checks

    def test_get_credentials(self):
        """Pytest harness hook"""
        assert bool(falcon.get_credentials()["status_code"] in AllowedResponses) is True

    @pytest.mark.skipif(os.getenv("DEBUG_API_BASE_URL", "us1").lower() in ["https://api.eu-1.crowdstrike.com", "eu1", "https://api.laggar.gcw.crowdstrike.com", "usgov1"],
                        reason="Unit testing unavailable on US-GOV-1 / EU-1"
                        )
    def test_remaining_code_paths(self):
        """Pytest harness hook"""
        assert self.run_tests() is True
