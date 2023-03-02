from typing import Callable

from fastapi import FastAPI
from loguru import logger

from src.core.settings.app import AppSettings

from src.bot import send_to_channel


def create_start_app_handler(
    app: FastAPI,
    settings: AppSettings,
) -> Callable:  # type: ignore
    async def start_app() -> None:
        print('start_app')
        await send_to_channel('start fast api test app')

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    @logger.catch
    async def stop_app() -> None:
        print('stop_app')
        await send_to_channel('stop fast api test app')

    return stop_app
