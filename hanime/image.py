from typing import List, Optional, Dict, Any
from .models import HanimeImage
from .exceptions import InvalidChannel

from tls_client import Session, exceptions
import time


class Image:
    BASE_URL = 'https://community-uploads.highwinds-cdn.com/api/v9/community_uploads'
    ALLOWED_CHANNELS = {
        'nsfw-general',
        'furry',
        'futa',
        'yaoi',
        'yuri',
        'traps',
        'media'
    }
    session = Session(
        client_identifier="chrome_118", random_tls_extension_order=True
    )

    @staticmethod
    def create_default_headers() -> Dict[str, Any]:
        return {
            'authority': 'hanime.tv',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Chrome OS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'x-directive': 'api',
            'x-session-token': '',
            'x-signature': None,
            'x-time': str(time.time()),
        }

    @staticmethod
    def build_query(channel_names: List[str], offset: int) -> Dict[str, Any]:
        valid_channels = set(channel_names) & Image.ALLOWED_CHANNELS
        if not valid_channels:
            raise InvalidChannel("Invalid channel names provided")

        return {
            'query_method': 'offset',
            '_offet': offset,
            'loc': 'https://hanime.tv',
            **{f'channel_name__in[]': name for name in valid_channels}
        }

    @staticmethod
    def _parse(data: Dict[str, Any]) -> List[HanimeImage]:
        uploads = data.get('data', [])
        return [HanimeImage(**upload) for upload in uploads]

    @classmethod
    def get_uploads(cls, channel_names: List[str], offset: int) -> Optional[Dict[str, Any]]:
        url = cls.BASE_URL
        headers = cls.create_default_headers()
        query = cls.build_query(channel_names, offset)

        try:
            response = cls.session.get(url, headers=headers, params=query)
            return response.json()
        except exceptions.TLSClientExeption as e:
            print(f"Error getting community uploads: {e}")
            return None
