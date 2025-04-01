import argparse
from mcp.server.fastmcp import FastMCP

parser = argparse.ArgumentParser()
parser.add_argument("--transport", "-t", type=str, default="stdio")
args = parser.parse_args()

mcp = FastMCP()

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

if __name__ == "__main__":
    mcp.run(transport=args.transport)

