import asyncio
import httpx
from Miscblox.Functions.logger import logger
import json
from array import array
from datetime import date

class AdvertConfiguration():
    def __init__(self, cookie):
        self.cookie = cookie
        self.logger = logger
        self.base_url = "https://ads.roblox.com"
        self.client = httpx.AsyncClient(cookies={".ROBLOSECURITY": cookie})
        if self.cookie is None:
            self.logger.error("Please login with your Roblox account.")
    
    async def create_Asset_Ad(self, assetId: int, name: str = None):
        try:
            if self.cookie is None:
                self.logger.error("Please login with your Roblox account.")
                return None
            

            
            request = await self.client.post(f"{self.base_url}/v1/user-ads/assets/create", json={"assetId": assetId, "name": name, "Files": None})

            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/user-ads/assets/create", json={"assetId": assetId, "name": name, "Files": None}, headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
                    
                    return valid_request.json()
                        
                    
                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
        
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
    
    async def create_Pass_Ad(self, passId: int, name: str = None):
        try:
            if self.cookie is None:
                self.logger.error("Please login with your Roblox account.")
                return None
            

            
            request = await self.client.post(f"{self.base_url}/v1/user-ads/game-passes/create", json={"passId": passId, "name": name, "Files": None})

            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/user-ads/game-passes/create", json={"assetId": passId, "name": name, "Files": None}, headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
                    
                    return valid_request.json()
                        
                    
                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
        
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
    
    async def create_Group_Ad(self, groupId: int, name: str = None):
        try:
            if self.cookie is None:
                self.logger.error("Please login with your Roblox account.")
                return None
            

            
            request = await self.client.post(f"{self.base_url}/v1/user-ads/groups/create", json={"groupId": groupId, "name": name, "Files": None})

            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/user-ads/groups/create", json={"groupId": groupId, "name": name, "Files": None}, headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
                    
                    return valid_request.json()
                        
                    
                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
        
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
            
            
            
            