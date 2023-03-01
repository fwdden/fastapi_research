import logging
import sys
from typing import Any, Dict, List, Tuple

from loguru import logger
from pydantic import PostgresDsn, SecretStr

from src.core.logging import InterceptHandler
from src.core.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    debug: bool = False
    title: str = "FastAPI example application"
    version: str = "0.0.0"

    api_prefix: str = "/api"

    allowed_hosts: List[str] = ["*"]

    logging_level: int = logging.INFO
    loggers: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    class Config:
        validate_assignment = True

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "title": self.title,
            "version": self.version,
        }

    def configure_logging(self) -> None:
        logging.getLogger().handlers = [InterceptHandler()]
        for logger_name in self.loggers:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler(level=self.logging_level)]

        logger.configure(handlers=[{"sink": sys.stderr, "level": self.logging_level}])
