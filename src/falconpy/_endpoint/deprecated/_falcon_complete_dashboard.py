"""Internal API endpoint constant library (deprecated operations)."""

_falcon_complete_dashboard_endpoints = [
  [
    "AggregateFCIncidents",
    "POST",
    "/falcon-complete-dashboards/aggregates/incidents/GET/v1",
    "Retrieve aggregate incident values based on the matched filter",
    "falcon_complete_dashboard",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "QueryIncidentIdsByFilter",
    "GET",
    "/falcon-complete-dashboards/queries/incidents/v1",
    "Retrieve incidents that match the provided filter criteria with scrolling enabled",
    "falcon_complete_dashboard",
    [
      {
        "type": "integer",
        "description": "The maximum records to return. [1-500]",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The property to sort on, followed by a dot (.), followed by the sort direction, either "

        "\"asc\" or \"desc\".",

        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Optional filter and sort criteria in the form of an FQL query. For more information "

        "about FQL queries, see [our FQL documentation in "

        "Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide).",

        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Starting index of overall result set from which to return ids.",
        "name": "offset",
        "in": "query"
      }
    ]
  ]
]
