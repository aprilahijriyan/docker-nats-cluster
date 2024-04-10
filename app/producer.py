import asyncio
import os
from nats.aio.client import Client
from nats.errors import ConnectionClosedError, TimeoutError, NoServersError

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
NATS_SUBJECT = os.environ.get("NATS_SUBJECT", "foo")
nc = Client()


async def main():
    print(f"NATS URLS: {NATS_URLS}")
    print(f"NATS USER CREDENTIALS: {NATS_USER_CREDENTIALS}")
    print("Connecting to NATS...")
    await nc.connect(servers=NATS_URLS, user_credentials=NATS_USER_CREDENTIALS)
    print("Connected to NATS!")
    try:
        print(f"Producing messages to subject: {NATS_SUBJECT}")
        for i in range(10):
            await nc.request(NATS_SUBJECT, f"Message {i}!".encode())
            print(f"> Message {i}!")
            await asyncio.sleep(1)
        await nc.flush()
    except ConnectionClosedError as e:
        print("Connection closed: ", e)
    except TimeoutError as e:
        print("Timeout: ", e)
    except NoServersError as e:
        print("No servers: ", e)

    await nc.drain()

if __name__ == "__main__":
    asyncio.run(main())
