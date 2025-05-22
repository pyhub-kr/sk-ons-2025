import os
import django
from asgiref.sync import sync_to_async

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "mysite.settings",
)
django.setup()

from mcp.server.fastmcp import FastMCP
from outlook.types import Email
from outlook.win import get_emails
from django.contrib.auth.models import User
mcp = FastMCP("mymcp")

# from typing import Optional
# def mysum(a: int, b: int | None = None) -> int:
#     return a + b

@mcp.tool()
async def get_users() -> list[str]:
    qs = User.objects.all()
    qs = qs.values_list("username", flat=True)
    return await sync_to_async(list)(qs)
    # return list(qs)


@mcp.tool()
def outlook_get_emails(max_hours: int) -> list[Email]:
    """
    Fetches emails from Outlook within the specified time frame.

    This function connects to the user's Outlook account and retrieves emails received
    within the last specified number of hours. Useful for processing or analyzing recent
    email communications.

    Args:
        max_hours (int): The number of hours in the past to search for emails.

    Returns:
        list[Email]: A list of Email objects representing the fetched emails.
    """

    return get_emails(max_hours)


if __name__ == "__main__":
    mcp.run("stdio")
