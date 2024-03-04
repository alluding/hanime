from typing import Any, Dict

class HanimeUser:
    def __init__(self, data: Dict[str, Any]):
        self.data = data

    def __getattr__(self, name: str) -> Any:
        return self.data.get(name, None)  

    def to_dict(self) -> Dict[str, Any]:
        return self.data.copy()
