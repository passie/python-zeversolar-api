"""
Copyright (c) 2017-2018 Pascal Osinga

Licensed under MIT. All rights reserved.
"""
import asyncio
import logging

import aiohttp
import async_timeout

from . import exceptions

_LOGGER = logging.getLogger(__name__)
_RESOURCE = 'https://{host}/api/v{version}/getPlantOverview?key='


class Zeversolar(object):
    """A class for handling the data retrieval."""

    def __init__(self, loop, session, host='www.zevercloud.com', version=1):
        """Initialize the connection."""
        self._loop = loop
        self._session = session
        self.url = _RESOURCE.format(host=host, version=version)
        self.data = None
        self.values = None
        self.plugins = None

    async def get_data(self):
        """Retrieve the data."""
        url = '{}/{}'.format(self.url, 'all')

        try:
            with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.get(url)

            _LOGGER.debug("Response from Zeversolar API: %s", response.status)
            self.data = await response.json()
            _LOGGER.debug(self.data)
        except (asyncio.TimeoutError, aiohttp.ClientError):
            _LOGGER.error("Can not load data from Zeversolar API")
            raise exceptions.ZeversolarApiConnectionError()

    async def get_metrics(self, element):
        """Get all the metrics for a monitored element."""
        await self.get_data()
        await self.get_plugins()

        if element in self.plugins:
            self.values = self.data[element]
        else:
            raise exceptions.ZeversolarApiError("Element data not available")

    async def get_plugins(self):
        """Retrieve the available plugins."""
        url = '{}/{}'.format(self.url, 'pluginslist')

        try:
            with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.get(url)

            _LOGGER.debug("Response from Zeversolar API: %s", response.status)
            self.plugins = await response.json()
            _LOGGER.debug(self.plugins)
        except (asyncio.TimeoutError, aiohttp.ClientError):
            _LOGGER.error("Can not load plugins from Zeversolar API")
            raise exceptions.ZeversolarApiConnectionError()
