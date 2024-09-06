import asyncio
import websockets
import rsa
import polyalphabetic

rsa_private_key = None
shared_key = None


async def sender():
    while True:
        print("\n1) Register public key - register <name> <key>")
        print("2) Wait for messages - receive")
        print("3) Exit - exit\n")
        command = input("Enter command: ")
        print()

        await send_command(command)


async def send_command(command):
    cmd = command.split(' ')[0]
    if cmd == "register":
        await register(command)
    elif cmd == "receive":
        await receive(command)
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


async def receive_and_print_server(websocket):
    global shared_key
    got_shared_key = False
    while not got_shared_key:
        response = await websocket.recv()
        key = rsa.rsa_decrypt(response, int(rsa_private_key.split(',')[
                              0]), int(rsa_private_key.split(',')[1]))
        shared_key = key
        got_shared_key = True
        await websocket.send("OK")

    print(f"Shared key received: {shared_key}")
    while True:
        response = await websocket.recv()
        message = polyalphabetic.decrypt(response, shared_key)
        print(f"Received message: {message}")
        await websocket.send("OK")


async def receive(command):
    server = await websockets.serve(receive_and_print_server, "localhost", 4000)
    print("Receive server started on ws://localhost:4000")
    await server.wait_closed()


asyncio.run(sender())
