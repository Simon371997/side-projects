from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import mcp.server.stdio

# Server erstellen
app = Server("example-server")


# Tool definieren
@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="get_time",
            description="Gibt die aktuelle Zeit zurück",
            inputSchema={
                "type": "object",
                "properties": {},
            },
        )
    ]


# Tool-Handler
@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "get_time":
        from datetime import datetime

        current_time = datetime.now().strftime("%H:%M:%S")
        return [TextContent(type="text", text=f"Die aktuelle Zeit ist: {current_time}")]


# Server starten
async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
