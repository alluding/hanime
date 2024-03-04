from typing import Dict, Any, Optional
from pydantic import BaseModel

class HanimeImage(BaseModel):
    id: int
    channel_name: str
    username: str
    url: str
    proxy_url: str
    extension: str
    width: int
    height: int
    filesize: int
    created_at_unix: int
    updated_at_unix: int
    discord_user_id: str
    user_avatar_url: str
    canonical_url: str

    def to_dict(self) -> Dict[str, Any]:
        return self.dict()