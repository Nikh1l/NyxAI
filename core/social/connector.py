from abc import ABC, abstractmethod

class SocialConnector(ABC):
    
    @abstractmethod
    async def get_profile(self):
        raise NotImplementedError
    
    @abstractmethod
    async def get_media(self):
       raise NotImplementedError
    
    @abstractmethod
    async def get_comments(self, media_id: str):
        raise NotImplementedError
    
    @abstractmethod
    async def post_reply(self, media_id: str, text: str):
        raise NotImplementedError