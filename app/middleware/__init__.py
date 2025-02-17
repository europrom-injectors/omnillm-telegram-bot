from aiogram import Dispatcher

from .context import ContextMiddleware
from .postgres import DatabaseInstance, UserExistsMiddleware, ActiveChatExistsMiddleware
from .logging import LoggingMiddleware


def setup_middleware(dp: Dispatcher) -> None:
    middlewaries = [
        ContextMiddleware,
        LoggingMiddleware,
        DatabaseInstance,
        UserExistsMiddleware,
        ActiveChatExistsMiddleware,
    ]

    for middleware in middlewaries:
        dp.message.outer_middleware(middleware())
        dp.callback_query.outer_middleware(middleware())


__all__ = [
    "setup_middleware",
    "ContextMiddleware",
    "LoggingMiddleware",
    "UserExistsMiddleware",
    "ActiveChatExistsMiddleware",
]
