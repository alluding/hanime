from typing import Dict, Any, Optional, Union

from tls_client import Session, exceptions
import time


class User:
    BASE_URL = 'https://hanime.tv/rapi/v7'

    def __init__(self, cookies: dict = {'in_d4': '1', 'in_m4': '1'}, headers: Optional[Dict[str, str]] = None):
        self.session = Session(
            client_identifier="chrome_118", random_tls_extension_order=True)
        self.session.cookies.update(cookies)
        self.session.headers.update(
            self.create_default_headers() if not headers else headers)

    @staticmethod
    def create_default_headers() -> Dict[str, str]:
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
            'user-agent': 'Mozilla/5.0 (U; Linux i563 x86_64; en-US) AppleWebKit/601.43 (KHTML, like Gecko) Chrome/47.0.2859.132 Safari/602',
            'x-directive': 'api',
            'x-session-token': '',
            'x-signature': None,
            'x-time': str(time.time()),
        }

    def get_channel(self, channel: Union[int, str]) -> Optional[Dict[str, Any]]:
        url = f'{self.BASE_URL}/channels/{channel}'
        try:
            response = self.session.get(url)
            return response.json()
        except exceptions.RequestException as e:
            print(f"Error getting channel info: {e}")
            return None
