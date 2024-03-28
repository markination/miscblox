import asyncio
import httpx
from Miscblox.Functions.logger import logger
import json
from array import array
from datetime import date

class AccountAvatar():
    def __init__(self, cookie):
        self.cookie = cookie
        self.logger = logger
        self.base_url = "avatar.roblox.com"
        self.client = httpx.AsyncClient(cookies={".ROBLOSECURITY": cookie})

    async def get_avatar_info(self):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")
            
            request = await self.client.get(f"{self.base_url}/v1/avatar")
            if request.status_code != 200:
                return self.logger.error("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            return jsonresponse
            
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
    
    async def get_avatar_rules(self):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")
            
            request = await self.client.get(f"{self.base_url}/v1/avatar-rules")
            if request.status_code != 200:
                return self.logger.error("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            return jsonresponse
            
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
    
    async def get_avatar_metadata(self):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")
            
            request = await self.client.get(f"{self.base_url}/v1/avatar/metadata")
            if request.status_code != 200:
                return self.logger.error("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            return jsonresponse
            
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
        
    async def get_user_avatar(self, userId: int):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")
            
            request = await self.client.get(f"{self.base_url}/v1/users/{userId}/avatar", json={"userID": userId})
            if request.status_code != 200:
                return self.logger.error("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            return jsonresponse
            
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
    
    async def get_user_current_wearing(self, userId: int):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")
            
            request = await self.client.get(f"{self.base_url}/v1/users/{userId}/currently-wearing", json={"userID": userId})
            if request.status_code != 200:
                return self.logger.error("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            return jsonresponse
            
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
    
    async def remove_asset_from_avatar(self, assetId: int):
        try:
            if self.cookie is None:
                self.logger.error("Please login with your Roblox account.")
                return None
            

            
            request = await self.client.post(f"{self.base_url}/v1/avatar/assets/{assetId}/remove", json={"assetId": assetId})

            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/avatar/assets/{assetId}/remove", json={"assetId": assetId}, headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
                    
                    return valid_request.json()
                        
                    
                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
        
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
        
    async def wear_asset_on_avatar(self, assetId: int):
        try:
            if self.cookie is None:
                self.logger.error("Please login with your Roblox account.")
                return None
            

            
            request = await self.client.post(f"{self.base_url}/v1/avatar/assets/{assetId}/wear", json={"assetId": assetId})

            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/avatar/assets/{assetId}/wear", json={"assetId": assetId}, headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
                    
                    return valid_request.json()
                        
                    
                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
        
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
    
    async def redraw_account_thumbnail(self):
        try:
            if self.cookie is None:
                self.logger.error("Please login with your Roblox account.")
                return None
        
            request = await self.client.post(f"{self.base_url}/v1/avatar/redraw-thumbnail")

            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/avatar/redraw-thumbnail", headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
                    
                    return valid_request.json()
                        
                    
                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
        
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
    
    async def change_account_color(self, colors: object):
        try:
            if self.cookie is None:
                self.logger.error("Please login with your Roblox account.")
                return None
        
            request = await self.client.post(f"{self.base_url}/v1/avatar/set-body-colors", json=colors)

            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/avatar/set-body-colors", headers=headers, json=colors)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
                    
                    return valid_request.json()
                        
                    
                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
        
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
        
    async def change_account_avatar_type(self, playerAvatarType: int):
        try:
            if self.cookie is None:
                self.logger.error("Please login with your Roblox account.")
                return None
        
            request = await self.client.post(f"{self.base_url}/v1/avatar/set-player-avatar-type", json={"playerAvatarType": playerAvatarType})

            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/avatar/set-player-avatar-type", json={"playerAvatarType": playerAvatarType}, headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
                    
                    return valid_request.json()
                        
                    
                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
        
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
    
    
    
    
    
    
    