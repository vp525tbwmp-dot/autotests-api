import asyncio
import websockets

async def main():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Привет, сервер!")

        try:
            while True:
                msg = await websocket.recv()
                print(msg)
        except websockets.exceptions.ConnectionClosedOK:
            print("Соединение закрыто сервером")

if __name__ == "__main__":
    asyncio.run(main())
