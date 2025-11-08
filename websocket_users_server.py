import asyncio
import websockets

async def handler(websocket):
    msg = await websocket.recv()
    print("получили от клиента:", msg)

    # шлём 5 ответов
    for i in range(5):
        await websocket.send(f"Сообщение #{i+1} от сервера")
        await asyncio.sleep(0.1)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Server started on ws://localhost:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
