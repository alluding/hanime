from typing import List, Optional, Dict, Any
from pydantic import BaseModel, create_model

from bs4 import BeautifulSoup


class SearchPayload(BaseModel):
    search_text: str = ''
    tags: List[str] = []
    tags_mode: str = 'AND'
    brands: List[str] = []
    blacklist: List[str] = []
    order_by: str = 'created_at_unix'
    ordering: str = 'desc'
    page: int = 0

    @classmethod
    def create_default_payload(cls):
        return cls()

    @staticmethod
    def convert_ordering(ordering: str) -> str:
        return {
            'recent_uploads': 'desc',
            'old_uploads': 'asc',
            'most_views': 'desc',
            'least_views': 'asc',
            'most_likes': 'desc',
            'least_likes': 'asc',
            'newest_uploads': 'desc',
            'oldest_uploads': 'asc',
            'alphabetical (a-z)': 'asc',
            'alphabetical (z-a)': 'desc',
        }.get(ordering, 'desc')  # Default to 'desc'

    @staticmethod
    def convert_order_by(order_by: str) -> str:
        return {
            'most_views': 'views',
            'least_views': 'views',
            'most_likes': 'likes',
            'least_likes': 'likes',
            'newest_uploads': 'released_at_unix',
            'oldest_uploads': 'released_at_unix',
            'alphabetical (a-z)': 'title_sortable',
            'alphabetical (z-a)': 'title_sortable',
        }.get(order_by, 'created_at_unix')  # Default to 'created_at_unix'


class BaseHeaders(BaseModel):
    authority: str = 'search.htv-services.com'
    accept: str = 'application.json, text.plain, /'
    accept_language: str = 'en-US,en;q=0.9'
    content_type: str = 'application/json;charset=UTF-8'
    origin: str = 'https://hanime.tv'
    sec_ch_ua: str = '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"'
    sec_ch_ua_mobile: str = '?0'
    sec_ch_ua_platform: str = '"Chrome OS"'
    sec_fetch_dest: str = 'empty'
    sec_fetch_mode: str = 'cors'
    sec_fetch_site: str = 'cross-site'
    user_agent: str = 'Mozilla/5.0 (U; Linux i563 x86_64; en-US) AppleWebKit/601.43 (KHTML, like Gecko) Chrome/47.0.2859.132 Safari/602'


class ParsedData:
    def __init__(self, data: Dict[str, Any]):
        self.data = data

    def __getattr__(self, name: str) -> Any:
        return self.data.get(name, None)

    @property
    def description(self) -> Optional[str]:
        html_description = self.data.get('description', '')
        soup = BeautifulSoup(html_description, 'html.parser')
        return soup.get_text() if html_description else None

    def to_dict(self) -> Dict[str, Any]:
        return self.data.copy()
