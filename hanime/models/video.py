from typing import List, Optional
from pydantic import BaseModel

from bs4 import BeautifulSoup


class HanimeVideoData(BaseModel):
    title: str
    duration: int
    tags: List[str]
    description: Optional[str]


class HanimeVideo:
    def __init__(self, data: dict):
        self.data = data

    def __getattr__(self, name: str):
        return self.data.get(name, None)

    @property
    def description(self) -> Optional[str]:
        html_description = self.data.get('description', '')
        soup = BeautifulSoup(html_description, 'html.parser')
        return soup.get_text() if html_description else None
