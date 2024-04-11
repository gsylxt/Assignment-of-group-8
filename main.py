import math
import Arctan
import Arcsin
import Sin
import Cos
import test
import asyncio
import websockets
import json


async def hello(websocket, path):
    display_handle = {
        'display_1': 0,
        'display_2': '',
    }
    answer = 0

    while True:
        receive = await websocket.recv()
        # display = json.dumps(receive)
        rec_1 = json.loads(receive)
        # print(receive)
        # print(f"<{display}")
        print(f"<{rec_1}")
        number = rec_1['display_1']
        method = rec_1['display_2']
        if method == 'sin':
            answer = Sin.sin(number)
        elif method == 'cos':
            answer = Cos.cos(number)
        elif method == 'arcsin':
            answer = Arcsin.arcsin(number)
        elif method == 'arctan':
            answer = Arctan.arctan(number)
        else: answer = 'er'
        display_handle['display_1'] = answer
        display_handle['display_2'] = method
        greeting = json.dumps(display_handle)
        # print(f"> {greeting}")
        print(greeting)
        await websocket.send(greeting)
        print(f">{greeting}")


# async def hello(websocket, path):
#     while True:
#         name= await websocket.recv()
#         print(f"<{name}")
#         greeting=f"Hello{name}!"
#         await websocket.send(greeting)
#         print(f">{greeting}")

if __name__ == "__main__":
    start_server = websockets.serve(hello, "localhost", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
