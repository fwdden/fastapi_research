from typing import Callable

from fastapi import FastAPI
from loguru import logger

from src.core.settings.app import AppSettings


def create_start_app_handler(
    app: FastAPI,
    settings: AppSettings,
) -> Callable:  # type: ignore
    async def start_app() -> None:
        print('start_app')

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    @logger.catch
    async def stop_app() -> None:
        print('stop_app')

    return stop_app
