from typing import Optional, List

from .models import (
    HanimeVideo,
    ParsedData,
    BaseHeaders,
    SearchPayload
)
from .exceptions import InvalidTagsError
from .search import Search

from tls_client import Session, exceptions

import random
import time


class Video:
    BASE_URL = 'https://hanime.tv/api/v8'
    TAGS = [
        "3d", "ahegao", "anal", "bdsm", "big boobs", "blow job", "bondage", "boob job", "censored", "comedy", "cosplay",
        "creampie", "dark skin", "facial", "fantasy", "filmed", "foot job", "futanari", "gangbang", "glasses",
        "hand job", "harem", "hd", "horror", "incest", "inflation", "lactation", "loli", "maid", "masturbation", "milf",
        "mind break", "mind control", "monster", "nekomimi", "ntr", "nurse", "orgy", "plot", "pov", "pregnant",
        "public sex", "rape", "reverse rape", "rimjob", "scat", "school girl", "shota", "softcore", "swimsuit",
        "teacher", "tentacle", "threesome", "toys", "trap", "tsundere", "ugly bastard", "uncensored", "vanilla", "virgin",
        "watersports", "x-ray", "yaoi", "yuri"
    ]

    def __init__(self, cookies: dict = {'in_d4': '1', 'in_m4': '1'}, client_identifier: Optional[str] = "chrome_118"):
        self.session = Session(
            client_identifier=client_identifier, random_tls_extension_order=True)
        self.session.cookies.update(cookies)
        self.session.headers.update(
            self.create_default_headers(client_identifier))

    @ staticmethod
    def create_default_headers(client_identifier: Optional[str] = None) -> dict:
        headers = {
            'authority': 'hanime.tv',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Chrome OS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (U; Linux i563 x86_64; en-US) AppleWebKit/601.43 (KHTML, like Gecko) Chrome/47.0.2859.132 Safari/602'
        }

        if client_identifier:
            headers |= {'x-directive': 'api',
                        'user-agent': f'HanimeWrapper ({client_identifier})', 'x-time': str(time.time())}

        return headers

    def information(self, video_id: int) -> Optional[HanimeVideo]:
        url = f'{self.BASE_URL}/video?id={video_id}'
        try:
            response = self.session.get(url)
            data = response.json()
            return HanimeVideo(data['hentai_video'])
        except exceptions.TLSClientExeption as e:
            print(f"Error getting video info: {e}")
            return None

    def random_video(self) -> Optional[HanimeVideo]:
        url = f'{self.BASE_URL}/hentai_videos'
        params = {'source': 'randomize', 'r': str(int(time.time() * 1000))}

        try:
            response = self.session.get(url, params=params)
            data = response.json()
            return HanimeVideo(data['hentai_videos'][0]) if 'hentai_videos' in data else None
        except exceptions.TLSClientExeption as e:
            print(f"Error getting random video: {e}")
            return None

    def get_random_video_tag(
        self,
        num_tags: int = 1,
        include_tags: Optional[List[str]] = None,
        exclude_tags: Optional[List[str]] = None,
        page: int = 0
    ) -> List[ParsedData]:
        def is_valid_tag(tag): return tag in self.TAGS

        _include = [tag for tag in (
            include_tags or []) if not is_valid_tag(tag)]
        _exclude = [tag for tag in (
            exclude_tags or []) if not is_valid_tag(tag)]

        if _include or _exclude:
            raise InvalidTagsError(f"Invalid tags: {_include + _exclude}")

        filtered_tags = [
            tag for tag in self.TAGS
            if (include_tags is None or tag in include_tags) and (exclude_tags is None or tag not in exclude_tags)
        ]

        if not filtered_tags:
            raise ValueError("No tags available after filtering.")

        payload = SearchPayload(tags=random.sample(
            filtered_tags, min(num_tags, len(filtered_tags))), page=page)

        return Search._parse(Search().search(payload))
