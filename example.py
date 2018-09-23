"""
Copyright (c) 2017-2018 Pascal Osinga

Licensed under MIT. All rights reserved.
"""
import asyncio

import aiohttp

from zeversolar_api import Zeversolar

HOST = 'www.zevercloud.com'


async def main():
    """The main part of the example script."""
    async with aiohttp.ClientSession() as session:
        data = Zeversolar(loop, session)

        # Get the metrics for the sid
        await data.get_sid('sid')

        # Print the values
        print("ID values:", data.values)

        # Get the metrics about the E-Today
        await data.get_E-Today('E-Today')

        # Print the values
        print("E-Today values:", data.values)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
