r"""Identity Protection pagination example.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |       FalconPy v1.2.11
`-------'                         `-------'

_____ ______  _______ __   _ _______ _____ _______ __   __
  |   |     \ |______ | \  |    |      |      |      \_/
__|__ |_____/ |______ |  \_|    |    __|__    |       |

 _____   ______  _____  _______ _______ _______ _______ _____  _____  __   _
|_____] |_____/ |     |    |    |______ |          |      |   |     | | \  |
|       |    \_ |_____|    |    |______ |_____     |    __|__ |_____| |  \_|

This sample demonstrates pagination within the IDP service collection using GraphQL syntax.

Creation: 02.15.23 - jshcodes@CrowdStrike

This example requires crowdstrike-falconpy v1.2.11+.
"""
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from falconpy import IdentityProtection, _VERSION


EXAMPLE_QUERY = """
query ($after: Cursor) {
  entities(types: [USER], archived: false, learned: false, first: ~LIMIT~, after: $after) {
    nodes {
      primaryDisplayName
      secondaryDisplayName
      accounts {
        ... on ActiveDirectoryAccountDescriptor {
          domain
        }
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
"""
def version_check():
    """Confirm the version of FalconPy we're running supports the syntax we're using."""
    valid_version = False
    vers = _VERSION.split(".")
    major_minor = float(f"{vers[0]}.{vers[1]}")
    if major_minor >= 1.2 and int(vers[2]) >= 11:
        valid_version = True

    if not valid_version:
        raise SystemExit("This example requires crowdstrike-falconpy v1.2.11 or greater.")


def consume_arguments():
    """Consume any command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    req = parser.add_argument_group("required arguments")
    req.add_argument("-k", "--falcon_client_id",
                     help="CrowdStrike Falcon API client ID",
                     required=True
                     )
    req.add_argument("-s", "--falcon_client_secret",
                     help="CrowdStrike Falcon API client Secret",
                     required=True
                     )
    parser.add_argument("-l", "--limit",
                        help="Number of records to handle per batch",
                        default=5
                        )
    return parser.parse_args()


def open_sdk(cmd: Namespace):
    """Open and return the Identity Protection service collection."""
    return IdentityProtection(client_id=cmd.falcon_client_id,
                              client_secret=cmd.falcon_client_secret
                              )


def paginate_results(cmd: Namespace, idp: IdentityProtection):
    """Paginate through all results returned and then display the output."""
    # Apply the limit provided by the command line
    idp_query = EXAMPLE_QUERY.replace("~LIMIT~", str(cmd.limit))
    running = True       # Loop boolean
    returned_nodes = []  # Nodes returned
    query_vars = {}      # Used to provide the pagination token in subsequent requests
    while running:
        print(f"Requesting a page of {cmd.limit} results")
        result = idp.graphql(query=idp_query, variables=query_vars)
        if result["status_code"] != 200:
            raise SystemExit("API error, check query contents.")
        if result["body"]["data"].get("entities"):
            if "nodes" in result["body"]["data"]["entities"]:
                returned_nodes.extend(result["body"]["data"]["entities"]["nodes"])
                page_info = result["body"]["data"]["entities"]["pageInfo"]
                if page_info["hasNextPage"]:  # Pagination token is present
                    # Provide this token to our subsequent API request
                    query_vars["after"] = page_info["endCursor"]
                else:
                    running = False
            else:
                running = False
        else:
            raise SystemExit("No results returned.")

    for node in returned_nodes:
        print(node["primaryDisplayName"])
    print(f"{len(returned_nodes)} results returned.")


if __name__ == "__main__":
    # Check to make sure we're running a valid version of FalconPy
    version_check()
    # Retrieve our command line arguments
    cmd_line = consume_arguments()
    # Open the SDK and run the pagination example
    paginate_results(cmd_line, open_sdk(cmd_line))
