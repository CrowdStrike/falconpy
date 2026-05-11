# test_knowledge_base_audit_events.py
# This class tests the knowledge_base_audit_events service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import KnowledgeBaseAuditEvents

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = KnowledgeBaseAuditEvents(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestKnowledgeBaseAuditEvents:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "AggregatesKnowledgeBaseAuditEventsV1": falcon.aggregates_knowledge_base_audit_events_v1(include_deleted=True,
                                                                                                     date_ranges=[{"from": "string", "to": "string"}],
                                                                                                     field="string",
                                                                                                     filter="string",
                                                                                                     interval="string",
                                                                                                     min_doc_count=0,
                                                                                                     missing="string",
                                                                                                     name="string",
                                                                                                     q="string",
                                                                                                     ranges=[{"From": 0, "To": 0}],
                                                                                                     size=0, sort="string",
                                                                                                     sub_aggregates=["string"],
                                                                                                     time_zone="string",
                                                                                                     type="string"),
            "CombinedKnowledgeBaseAuditEventsV1": falcon.combined_knowledge_base_audit_events_v1(knowledge_base_id="string",
                                                                                                 offset=1, limit=1,
                                                                                                 sort="string",
                                                                                                 filter="string",
                                                                                                 include_deleted=True),
            "EntitiesKnowledgeBaseAuditEventsV1": falcon.entities_knowledge_base_audit_events_v1(knowledge_base_id="string",
                                                                                                 ids=["string"],
                                                                                                 include_deleted=True),
            "QueriesKnowledgeBaseAuditEventsV1": falcon.queries_knowledge_base_audit_events_v1(knowledge_base_id="string",
                                                                                               offset=1, limit=1,
                                                                                               sort="string", filter="string",
                                                                                               include_deleted=True),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
