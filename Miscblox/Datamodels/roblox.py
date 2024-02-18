from pydantic import BaseModel
from typing import Optional, List

class RobloxUser(BaseModel):
    id: int
    username: Optional[str]
    display_name: Optional[str]
    description: Optional[str]
    avatar_url: Optional[str]

class RobloxGroup(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    owner_id: int

class RobloxGame(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    creator_id: int

class RobloxBadge(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    image_url: Optional[str] = None

class RobloxAsset(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    asset_type: str
    creator_id: int

class RobloxCatalogItem(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    item_type: str
    creator_id: int

class RobloxComment(BaseModel):
    id: int
    user_id: int
    content: str
    created_at: str

class RobloxMessage(BaseModel):
    id: int
    sender_id: int
    recipient_id: int
    content: str
    created_at: str

class RobloxTrade(BaseModel):
    id: int
    initiator_id: int
    recipient_id: int
    items_offered: List[RobloxAsset]
    items_requested: List[RobloxAsset]
    created_at: str

class RobloxInventoryItem(BaseModel):
    id: int
    asset_id: int
    owner_id: int
    quantity: int
