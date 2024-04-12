import asyncio
import os
import signal
from nats.aio.client import Client
from nats.aio.msg import Msg

NATS_URLS = list(
    filter(
        lambda x: len(x) > 0,
        map(
            lambda x: x.strip(),
            os.environ.get("NATS_URLS", "nats://localhost:4222").split(","),
        ),
    )
)
NATS_USER_CREDENTIALS = os.environ.get("NATS_USER_CREDENTIALS", "")
nc = Client()

async def disconnected_cb():
    print("Got disconnected...")

async def reconnected_cb():
    print("Got reconnected...")

async def handler(msg: Msg):
    subject = msg.subject
    reply = msg.reply
    data = msg.data.decode()
    print(f"Headers: {msg.headers}")
    print(
        "Received a message on '{subject} -> {reply}': {data}".format(
            subject=subject, reply=reply, data=data
        )
    )
    print("-" * 20)
    await msg.respond(b"OK")

def signal_handler():
    print("Signal received, disconnecting...")
    if nc.is_closed:
        asyncio.get_running_loop().stop()
        return

    async def stop():
        await nc.drain()
        asyncio.get_running_loop().stop()

    asyncio.create_task(stop())

async def main():
    print(f"NATS URLS: {NATS_URLS}")
    print(f"NATS USER CREDENTIALS: {NATS_USER_CREDENTIALS}")
    print("Connecting to NATS...")
    await nc.connect(
        servers=NATS_URLS,
        user_credentials=NATS_USER_CREDENTIALS,
        reconnected_cb=reconnected_cb,
        disconnected_cb=disconnected_cb,
    )
    print("Connected to NATS!")
    print("Listening for RPC requests...")
    await nc.subscribe("rpc.hello", cb=handler, queue="hello_queue")
    await nc.subscribe("rpc.echo", cb=handler, queue="echo_queue")
    await nc.subscribe("rpc.ping", cb=handler, queue="ping_queue")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    for sig in ("SIGINT", "SIGTERM"):
        loop.add_signal_handler(
            getattr(signal, sig), signal_handler
        )

    loop.run_until_complete(main())
    try:
        loop.run_forever()
    finally:
        loop.close()
