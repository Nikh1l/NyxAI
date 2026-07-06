import httpx

class InstagramClient:
    
    BASE_URL = "https://graph.instagram.com/v25.0"


    def __init__(self, access_token: str):
        self.access_token = access_token
        self.MEDIA_FIELDS = ",".join([
            "id",
            "caption",
            "media_type",
            "media_url",
            "thumbnail_url",
            "timestamp",
            "permalink",
            "comments_count",
        ])
        self.COMMENT_FIELDS = ",".join([
            "id",
            "text",
            "timestamp",
            "username",
        ])

    async def _get(self, endpoint: str, **params):
        params.setdefault("access_token", self.access_token)

        try:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.get(
                    f"{self.BASE_URL}{endpoint}",
                    params=params,
                )

            if response.status_code >= 400:
                print(response.text)

            response.raise_for_status()

            return response.json()
        except Exception as e:
            print(type(e))
            print(e)
            raise
    
    async def _paginate(self ,endpoint: str ,fields: str ,limit: int = 100):
        items = []

        params = {
            "fields": fields,
            "limit": limit,
        }
        
        page = 1

        while True:
            print(f"Fetching page {page}...")
            response = await self._get(endpoint, **params)

            items.extend(response.get("data", []))

            paging = response.get("paging", {})
            cursors = paging.get("cursors", {})

            after = cursors.get("after")

            if not after:
                break

            params["after"] = after
            page += 1

        return items
        

    async def me(self):
        return await self._get(
            "/me",
            fields="id,username,name,account_type,media_count",
        )
    
    async def media(self):
        return await self._paginate(
            endpoint="/me/media",
            fields=self.MEDIA_FIELDS,
    )
    
    async def comments(self, media_id: str):
        return await self._paginate(
            f"/{media_id}/comments",
            fields=self.COMMENT_FIELDS,
    )

    async def reply(self, comment_id: str, message: str):
        endpoint = f"/{comment_id}/replies"

        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                f"{self.BASE_URL}{endpoint}",
                data={
                    "message": message,
                    "access_token": self.access_token
                },
            )
        
        response.raise_for_status()
        
        return response.json()
        