from typing import (
    List,
    Optional,
    Dict,
    Any
)

from .models import (
    ParsedData,
    SearchPayload,
    BaseHeaders
)

from tls_client import Session
import json


class Search:
    BASE_URL = 'https://search.htv-services.com/'

    def __init__(self, client_identifier: Optional[str] = 'chrome_118'):
        self.session = Session(
            client_identifier=client_identifier, random_tls_extension_order=True)
        self.session.headers = BaseHeaders().__dict__

    def search(self, payload: SearchPayload) -> Dict[str, Any]:
        response = self.session.post(self.BASE_URL, json=payload.dict())
        return response.json()

    @staticmethod
    def filter_response(base_response: Dict[str, Any], filter_options: List[str]) -> Dict[str, Any]:
        return {key: base_response[key] for key in filter_options if key in base_response}

    @staticmethod
    def _parse(response: Dict[str, Any]) -> List[ParsedData]:
        try:
            hits = json.loads(response.get('hits', '[]'))
            return [ParsedData(hit) for hit in hits]
        except (KeyError, json.JSONDecodeError):
            return []
