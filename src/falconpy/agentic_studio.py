"""CrowdStrike Falcon AgenticStudio API interface class.

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

from .agents import Agents
from .agent_invocation import AgentInvocation
from .agent_templates import AgentTemplates
from .agent_versions import AgentVersions
from .knowledge_bases import KnowledgeBases
from .knowledge_base_files import KnowledgeBaseFiles
from .knowledge_base_audit_events import KnowledgeBaseAuditEvents
from .models import Models
from .skills import Skills
from .spans import Spans
from .tools import Tools
from .stream import Stream


class AgenticStudio(Agents,  # pylint: disable=too-many-ancestors
                    AgentInvocation,
                    AgentTemplates,
                    AgentVersions,
                    KnowledgeBases,
                    KnowledgeBaseFiles,
                    KnowledgeBaseAuditEvents,
                    Models,
                    Skills,
                    Spans,
                    Tools,
                    Stream):
    """Combined AgenticStudio service collection providing access to all agentic studio operations.

    This class aggregates all AgenticStudio sub-service collections into a single interface
    via multiple inheritance. Operations are provided by the following sub-services:

    - Agents
    - AgentInvocation
    - AgentTemplates
    - AgentVersions
    - KnowledgeBases
    - KnowledgeBaseFiles
    - KnowledgeBaseAuditEvents
    - Models
    - Skills
    - Spans
    - Tools
    - Stream

    The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (oauth2.py)
    """


# Backward compatibility alias
Agentic_Studio = AgenticStudio  # pylint: disable=C0103
