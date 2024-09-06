import asyncio
import websockets
import rsa
import polyalphabetic

rsa_private_key = None
shared_key = None


async def sender():
    while True:
        print("\n1) Register public key - register <name> <key>")
        print("2) Get public key - get <name>")
        print("3) Send message - connect <name> <ip:port>")
        print("4) Exit - exit\n")
        command = input("Enter command: ")
        print()

        await send_command(command)


async def send_command(command):
    cmd = command.split(' ')[0]
    if cmd == "register":
        await register(command)
    elif cmd == "get":
        await get(command)
    elif cmd == "connect":
        await connect(command)
    else:
        print("Unknown command")


async def register(command):
    global rsa_private_key
    words = command.split(' ')
    prime_nums = words[2]
    p, q = prime_nums.split(',')
    p, q = int(p), int(q)
    n, e, d = rsa.key_gen(p, q)
    public_key = f"{n},{e}"
    rsa_private_key = f"{n},{d}"

    print(f"Public key generated for {words[1]}")
    print(f"n: {n}, e: {e}")
    print()

    async with websockets.connect('ws://localhost:3000') as websocket:
        await websocket.send(f"{words[0]} {words[1]} {public_key}")
        response = await websocket.recv()
        print(response)


async def get(command):
    async with websockets.connect('ws://localhost:3000') as websocket:
        await websocket.send(command)
        response = await websocket.recv()
        print(response)
        return response


async def connect(command):
    _, name, address = command.split(' ')
    ip, port = address.split(':')
    public_key = None
    try:
        public_key = await get("get " + name)
    except:
        print("Public key not found")
        return

    n, e = public_key.split(',')
    n, e = int(n), int(e)
    print(f"Public key received for {name}")
    print(f"n: {n}, e: {e}")
    print()

    key = input("Enter shared key: ")
    print()

    global shared_key
    shared_key = key

    async with websockets.connect(f"ws://{ip}:{port}") as websocket:
        await websocket.send(f"{rsa.rsa_encrypt(key, n, e)}")
        response = await websocket.recv()
        print(response)

        if response == "OK":
            while True:
                msg = input("Enter message: ")
                if msg == "exit":
                    break
                cip = polyalphabetic.encrypt(msg, key)
                await websocket.send(cip)
                response = await websocket.recv()
                print(response)

asyncio.run(sender())
