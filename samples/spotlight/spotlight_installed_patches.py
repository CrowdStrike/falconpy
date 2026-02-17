r"""Spotlight installed patches query sample.

Query Spotlight installed patch data and print the JSON response.

Required API scopes
    Vulnerabilities: READ
"""
import json
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from falconpy import SpotlightVulnerabilities


def consume_arguments() -> Namespace:
    """Consume and validate command-line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    required = parser.add_argument_group("required arguments")
    required.add_argument("-k", "--client_id", help="CrowdStrike Falcon API client ID.", required=True)
    required.add_argument("-s", "--client_secret",
                          help="CrowdStrike Falcon API client secret.",
                          required=True
                          )
    required.add_argument("-f", "--filter",
                          help="FQL filter used to query installed patch records.",
                          required=True
                          )
    parser.add_argument("-b", "--base_url",
                        help="CrowdStrike API region (us1, us2, eu1, usgov1).",
                        default=None
                        )
    parser.add_argument("-l", "--limit",
                        help="Number of records to request per page.",
                        default=100,
                        type=int
                        )
    parser.add_argument("--sort",
                        help="Sort expression (example: hostname|asc).",
                        default=None
                        )
    parser.add_argument("--after",
                        help="Pagination token from a previous response.",
                        default=None
                        )
    parser.add_argument("-a", "--all",
                        help="Retrieve all pages by following the `after` token.",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-o", "--output_file",
                        help="Optional output file path for JSON results.",
                        default=None
                        )

    return parser.parse_args()


def extract_error_message(response: dict) -> str:
    """Extract a meaningful error message from a Falcon API response."""
    fallback = "The request failed and no error message was returned."
    errors = response.get("body", {}).get("errors", [])
    if not errors:
        return fallback

    messages = []
    for item in errors:
        if item.get("message", None):
            messages.append(item["message"])

    if not messages:
        return fallback

    return " | ".join(messages)


def run_query(client: SpotlightVulnerabilities, args: Namespace, after_token: str = None) -> dict:
    """Run one page query for installed patches."""
    query = {
        "filter": args.filter,
        "limit": args.limit
    }
    if args.sort:
        query["sort"] = args.sort
    if after_token:
        query["after"] = after_token

    returned = client.query_installed_patches_combined(**query)
    if returned["status_code"] >= 400:
        raise SystemExit(extract_error_message(returned))

    return returned


def collect_results(client: SpotlightVulnerabilities, args: Namespace) -> dict:
    """Collect one or more pages of installed patches data."""
    current_after = args.after
    pages = 0
    all_resources = []
    last_response = {}
    while True:
        page = run_query(client, args, current_after)
        pages += 1
        last_response = page
        all_resources.extend(page.get("body", {}).get("resources", []))
        next_after = page.get("body", {}).get("meta", {}).get("pagination", {}).get("after")
        if not args.all or not next_after:
            break
        current_after = next_after

    if not args.all:
        return last_response

    return {
        "status_code": last_response.get("status_code"),
        "headers": last_response.get("headers", {}),
        "body": {
            "meta": {
                "pagination": {
                    "limit": args.limit,
                    "after": last_response.get("body", {}).get("meta", {}).get("pagination", {}).get("after"),
                    "pages": pages,
                    "total_retrieved": len(all_resources)
                }
            },
            "resources": all_resources,
            "errors": []
        }
    }


def main():
    """Execute the sample."""
    args = consume_arguments()
    auth = {
        "client_id": args.client_id,
        "client_secret": args.client_secret
    }
    if args.base_url:
        auth["base_url"] = args.base_url
    spotlight = SpotlightVulnerabilities(**auth)
    response = collect_results(spotlight, args)

    if args.output_file:
        with open(args.output_file, "w", encoding="utf-8") as output:
            json.dump(response, output, indent=4)
        print(f"Output written to {args.output_file}")

    print(json.dumps(response, indent=4))


if __name__ == "__main__":
    main()
