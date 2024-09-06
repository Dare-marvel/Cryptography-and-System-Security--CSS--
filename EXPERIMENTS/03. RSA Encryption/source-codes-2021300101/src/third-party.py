import asyncio
import websockets

public_keys = {}


def register_public_key(name, key):
    public_keys[name] = key


def get_public_key(name):
    return public_keys[name]


async def handle_command(websocket, path):
    async for message in websocket:
        words = message.lower().strip().split(' ')
        command = words[0]

        if command == "register":
            register_public_key(words[1], words[2])
            response = "Public key registered for " + words[1]
            print(f"Public key {words[2]} registered for " + words[1])
            print()
        elif command == "get":
            response = get_public_key(words[1])
            print("Public key requested for " + words[1])
            print(public_keys)
        else:
            response = "Unknown command"

        await websocket.send(response)


async def main():
    server = await websockets.serve(handle_command, "localhost", 3000)
    print("WebSocket server started on ws://localhost:3000")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
