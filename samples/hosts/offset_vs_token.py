"""
offset_vs_token.py - Compares the results produced by the two operations
QueryDevicesByFilter and QueryDevicesByFilterScroll for equivalency.

For environments with more than 10K hosts, this routine will fail as the
operation QueryDevicesByFilter is limited to a maximum of 10K records.
(Setting your offset to 10K or higher will produce a 400 error.)

In order to run this routine in environments this large, add a filter
that limits the number of hosts returned. (See get_query_results method.)

9.6.2021 - jshcodes@CrowdStrike
"""
#  ___ ___             __
# |   Y   .-----.-----|  |_.-----.
# |.  1   |  _  |__ --|   _|__ --|
# |.  _   |_____|_____|____|_____|
# |:  |   |
# |::.|:. |     FalconPy v0.8.6+
# `--- ---'
import os
import collections
try:
    from falconpy import Hosts
except ImportError as no_falconpy:
    raise SystemExit(
        "CrowdStrike FalconPy must be installed in order to use this application.\n"
        "Please execute `python3 -m pip install crowdstrike-falconpy` and try again."
        ) from no_falconpy


class Indicator():
    """
    Silly progress indicator styled after a momentum ball toy.
    """

    def __init__(self,
                 start_position: int = -1,
                 start_direction: bool = True,
                 msg: str = "",
                 ):

        self.position = start_position
        self.direction = start_direction
        self.msg = msg
        self.indicator = [
            "ooooo   ",
            "oooo o  ",
            "oooo  o ",
            "oooo   o",
            "ooo o  o",
            "ooo  o o",
            "ooo   oo",
            "oo o  oo",
            "oo  o oo",
            "oo   ooo",
            "o o  ooo",
            "o  o ooo",
            "o   oooo",
            " o  oooo",
            "  o oooo",
            "   ooooo"
        ]

    def step(self):
        """
        Calculates the position and direction of the indicator.
        """
        if self.position >= len(self.indicator) - 1:
            # Too long - out of bounds
            self.direction = False
        if self.position <= 0:
            # Too short - out of bounds
            self.direction = True

        if self.direction:
            # Increment position by 1
            self.position += 1
        else:
            # Decrement position by 1
            self.position -= 1

    def value(self) -> str:
        """
        Increments the indicator position and returns its value.
        """
        # Step the indicator forward
        self.step()

        # Grab the next indicator
        ind = self.indicator[self.position]

        # Return the new indicator display
        return f"{' ' * 2}%s {self.msg}{ind} %s" % ("(", ")")

    def display(self) -> str:
        """
        Increments the indicator position
        and prints its value dynamically.
        """
        # Display the indicator
        print(
            "%-80s" % self.value(),
            end="\r",
            flush=True
            )


def ind_message(ind: object, msg: str):
    """
    Updates the indicator message while retaining
    its current direction and position.
    """
    indy = Indicator(msg=f"{msg} )( ",
                     start_position=ind.position,
                     start_direction=ind.direction
                     )
    indy.display()
    return indy


def check_list(left: list, right: list, ind: object):
    """
    Uses the collections module to compare the keys within the two
    lists provided. If all keys are present in both lists, the lists
    are considered equal. Ends the routine if any comparison fails.
    """
    if collections.Counter(left) == collections.Counter(right):
        new_ind = ind_message(ind, "Lists match")
    else:
        print(f"{left} vs {right}")
        raise SystemExit("Lists do not match")

    return new_ind


def get_query_results(style: str, max_rows: int):
    """
    Performs a QueryDevicesByFilter or QueryDevicesByFilterScroll
    operation depending on the style selected. Loops thru all
    results available (up to 10K for QueryDevicesByFilter) and
    populates the compare dictionary with the resulting IDs.
    """
    # Higher than offset so our loop starts
    total = 1
    # Start with the first record
    offset = 0
    # Running counter for QueryDevicesByFilterScroll
    counter = 0
    # List to hold all of the IDs returned by calls
    returning = []
    if style.lower == "token_style":
        # Since the scrolling offset value is a string,
        # we will need to use a second variable to track
        # it's value when using this method
        offset_value = ""
    # Update the progress indicator
    indicator.display()
    # This loop works for both operations as the offset variable
    # is set to the value of the running counter used for the
    # QueryDevicesByFilterScroll operation.
    while offset < total:
        # Update the progress indicator
        indicator.display()
        if style.lower == "token_style":
            # Scrolling offset token, no maximum record count
            # We use the offset token string, not the offset integer
            result = falcon.query_devices_by_filter_scroll(
                sort="hostname|asc",
                limit=max_rows,
                offset=offset_value,
                # filter="platform_name:'Linux'"   # Uncomment to add filter
            )["body"]
        else:
            # Static offset, maxes out at 10K records
            # This is the same integer we use to control our loop
            result = falcon.query_devices_by_filter(
                sort="hostname|asc",
                limit=max_rows,
                offset=offset,
                # filter="platform_name:'Linux'"   # Uncomment to add filter
            )["body"]
        # Increment our counter by the value of our limit
        counter += max_rows
        # Retrieve the value of the offset.
        # QueryDevicesByFilter - This will be an integer.
        # QueryDevicesByFilterScroll - This will be a token string.
        offset_value = result["meta"]["pagination"]["offset"]
        if style.lower() == "token_style":
            # Set the value of offset to be our new counter value
            offset = counter
        else:
            # Set the value of offset to be the offset returned
            offset = offset_value
        # This will be the same every time,
        # overrides our init value of 1
        total = result["meta"]["pagination"]["total"]
        # Retrieve the list of IDs returned
        id_list = result["resources"]
        # Append this list to our running list of all IDs
        returning.extend(id_list)

    return returning


# Connect to the Hosts API
falcon = Hosts(client_id=os.environ["FALCON_CLIENT_ID"],
               client_secret=os.environ["FALCON_CLIENT_SECRET"]
               )

# Dictionary to hold our results
compare = {}
# Number of records to return per call, max is 5000
LIMIT = 100

# Standard offset handling using QueryDevicesByFilter
indicator = Indicator(msg="Offset method )( ")
indicator.display()
compare["offset_style"] = get_query_results("offset_style", LIMIT)

# "After" style offset handling using QueryDevicesByFilterScroll
indicator = ind_message(indicator, "Token method")
indicator.display()
compare["token_style"] = get_query_results("token_style", LIMIT)

# Comparing our resulting list lengths
indicator = ind_message(indicator, "Comparing results")
if len(compare["token_style"]) == len(compare["offset_style"]):
    indicator = ind_message(indicator, "Lengths match")
else:
    raise SystemExit("Lists do not match")

# Compare our resulting list keys
indicator = ind_message(indicator, "Comparing results")
indicator = check_list(
    compare["offset_style"],
    compare["token_style"],
    indicator
    )

# Success, the list match
print("%-80s" % "Lists are equivalent")


# ░█████╗░███████╗███████╗░██████╗███████╗████████╗
# ██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝╚══██╔══╝
# ██║░░██║█████╗░░█████╗░░╚█████╗░█████╗░░░░░██║░░░
# ██║░░██║██╔══╝░░██╔══╝░░░╚═══██╗██╔══╝░░░░░██║░░░
# ╚█████╔╝██║░░░░░██║░░░░░██████╔╝███████╗░░░██║░░░
# ░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═════╝░╚══════╝░░░╚═╝░░░
#
#             ██╗░░░██╗░██████╗░░░
#             ██║░░░██║██╔════╝░░░
#             ╚██╗░██╔╝╚█████╗░░░░
#             ░╚████╔╝░░╚═══██╗░░░
#             ░░╚██╔╝░░██████╔╝██╗
#             ░░░╚═╝░░░╚═════╝░╚═╝
#
#   ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗
#   ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║
#   ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║
#   ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║
#   ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║
#   ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝
