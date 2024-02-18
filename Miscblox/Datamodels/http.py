from typing import Any, Dict, List, Optional
from httpx import Response
from pydantic import BaseModel

class HTTPResponse(BaseModel):
    status_code: int
    headers: Dict[str, str]
    content: bytes
    text: str
    json: Any
    history: List[Response]
    is_redirect: bool
    url: str

class HTTPRequest(BaseModel):
    method: str
    url: str
    headers: Dict[str, str]
    cookies: Dict[str, str]
    params: Dict[str, Any]
    data: Any
    json: Any
