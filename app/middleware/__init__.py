from aiogram import Dispatcher

from .context import ContextMiddleware
from .postgres import UserExistsMiddleware, ActiveChatExistsMiddleware
from .logging import LoggingMiddleware


def setup_middleware(dp: Dispatcher) -> None:
    dp.message.outer_middleware(ContextMiddleware())
    dp.message.outer_middleware(LoggingMiddleware())
    dp.message.outer_middleware(UserExistsMiddleware())
    dp.message.outer_middleware(ActiveChatExistsMiddleware())


__all__ = [
    "setup_middleware",
    "ContextMiddleware",
    "LoggingMiddleware",
    "UserExistsMiddleware",
    "ActiveChatExistsMiddleware",
]
