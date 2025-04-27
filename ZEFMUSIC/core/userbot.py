from pyrogram import Client
import asyncio
import config
from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="RadharaniMusic1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
            max_concurrent_transmissions=1,
            workers=1,
        )
        self.two = Client(
            name="RadharaniMusic2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
            max_concurrent_transmissions=1,
            workers=1,
        )
        self.three = Client(
            name="RadharaniMusic3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
            max_concurrent_transmissions=1,
            workers=1,
        )
        self.four = Client(
            name="RadharaniMusic4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
            max_concurrent_transmissions=1,
            workers=1,
        )
        self.five = Client(
            name="RadharaniMusic5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
            max_concurrent_transmissions=1,
            workers=1,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")
        tasks = []
        
        if config.STRING1:
            tasks.append(self._start_assistant(self.one, 1))
        if config.STRING2:
            tasks.append(self._start_assistant(self.two, 2))
        if config.STRING3:
            tasks.append(self._start_assistant(self.three, 3))
        if config.STRING4:
            tasks.append(self._start_assistant(self.four, 4))
        if config.STRING5:
            tasks.append(self._start_assistant(self.five, 5))
            
        await asyncio.gather(*tasks)

    async def _start_assistant(self, client, num):
        try:
            await client.start()
            try:
                await client.join_chat("zefronmusic")
            except:
                pass
            assistants.append(num)
            try:
                await client.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    f"Assistant Account {num} has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                return
            client.id = client.me.id
            client.name = client.me.mention
            client.username = client.me.username
            assistantids.append(client.id)
            LOGGER(__name__).info(f"Assistant {num} Started as {client.name}")
        except Exception as e:
            LOGGER(__name__).error(f"Failed to start Assistant {num}: {str(e)}")

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
        tasks = []
        if config.STRING1:
            tasks.append(self.one.stop())
        if config.STRING2:
            tasks.append(self.two.stop())
        if config.STRING3:
            tasks.append(self.three.stop())
        if config.STRING4:
            tasks.append(self.four.stop())
        if config.STRING5:
            tasks.append(self.five.stop())
        await asyncio.gather(*tasks)
