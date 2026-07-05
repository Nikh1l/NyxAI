from core.social.connector import SocialConnector

class InstagramConnector(SocialConnector):
    async def get_profile(self):
        # Implement logic to fetch user profile from Instagram API
        raise NotImplementedError

    async def get_media(self):
        # Implement logic to fetch media posts from Instagram API
        raise NotImplementedError
    
    async def get_comments(self, media_id: str):
        # Implement logic to fetch comments on a specific media post from Instagram API
        raise NotImplementedError

    async def post_reply(self, media_id: str, text: str):
        # Implement logic to post a reply to a specific media post on Instagram API
        raise NotImplementedError