from typing import Union

import nextcord
from nextcord.ext.commands import Context
from nextcord.ext.commands import view

__all__ = ("ApplicationContext",)

Interaction = nextcord.Interaction
StringView = view.StringView

class ApplicationContext:

    def __init__(self, cls: Union[Context, Interaction]) -> None:
        self.message = cls.message
        self.bot = getattr(cls, "bot", None)
        self.author = getattr(cls, "author", "user")

        for attr in (
            "prefix",
            "clean_prefix",
            "guild",
            "channel",
            "clean_content",
            "command",
            "view",
            "cog",
            "command_failed",
            "guild_id",
            "channel_id", 
            "permissions", 

         ):
            setattr(self, attr, getattr(cls, attr, None))

        self.send = cls.send
        self.edit = getattr(cls, "edit", self.__empty_function)
        self.invoke = getattr(cls, "invoke", self.__empty_function)
        self.reinvoke = getattr(cls, "reinvoke", self.__empty_function)
        self.send_help = getattr(cls, "send_help", self.__empty_function)
        self.followup = getattr(cls, "followup", self.__empty_function)
        self.edit_original_message = getattr(cls, "edit_original_message", self.__empty_function)
        self.delete_original_message = getattr(cls, "delete_original_message", self.__empty_function)
        self.response = getattr(cls, "response", self.__empty_function)

    async def __empty_function(self, *args, **kwargs) -> None:
        return None
