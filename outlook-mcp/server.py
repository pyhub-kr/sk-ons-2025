# server.py

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mymcp")

@mcp.tool()
def outlook_get_emails() -> list[str]:
    """최근 아웃룩 이메일을 읽어 반환합니다."""

    return [
        f"샘플 이메일 #{i}"
        for i in range(1, 11)
    ]


if __name__ == "__main__":
    mcp.run("stdio")