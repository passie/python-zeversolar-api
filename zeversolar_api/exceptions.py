"""
Copyright (c) 2017-2018 Pascal Osinga

Licensed under MIT. All rights reserved.
"""


class ZeversolarApiError(Exception):
    """General ZeversolarApiErrorError exception occurred."""

    pass


class ZeversolarApiConnectionError(ZeversolarApiError):
    """When a connection error is encountered."""

    pass


class ZeversolarApiNoDataAvailable(ZeversolarApiError):
    """When no data is available."""

    pass
