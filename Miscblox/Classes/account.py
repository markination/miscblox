import httpx
from ..Functions.logger import logger
from .Account.Information import AccountInformation
from .Account.Settings import AccountSettings
from .Account.adverts import AdvertConfiguration

import asyncio


class RobloxAccount:
    def __init__(self):
        self.cookie = None
        self.client = None
        self.logger = logger
        self.information = None
        self.settings = None
    
    async def logout(self):
        if self.cookie is None:
            self.logger.warning("You are not logged in.")
            return
        self.cookie = None
        self.client = None
        self.logger.info("Logged out successfully.")
    
    async def login(self, cookie: str):
        if self.cookie is not None:
            self.logger.warning("There is already a session active.")
            return
        
        self.logger.info("Logging in...")
        self.client = httpx.AsyncClient(cookies={".ROBLOSECURITY": cookie})
        self.cookie = cookie
        response = await self.get_minimal_authenticated_info()
        if response:
            self.logger.info(f"Successfully logged in as {response['name']} ({response['id']})")
            self.information = AccountInformation(cookie=self.cookie)
            self.settings = AccountSettings(cookie=self.cookie)
    
    async def get_minimal_authenticated_info(self):
        if self.cookie is None:
            self.logger.warning("You need to log in first.")
            return None
        
        url = "https://users.roblox.com/v1/users/authenticated"
        try:
            
            response = await self.client.get(url)
            if response.status_code == 200:
                return response.json()
            
            else:
                self.logger.error(f"Failed to get authenticated user info: {response.status_code}")
                return None
        except httpx.HTTPStatusError as exc:
            self.logger.error(f"HTTP error: {exc}")
            return None
        except httpx.RequestError as exc:
            self.logger.error(f"Request error: {exc}")
            return None
        
            
    async def get_all_authenticated_info(self):
        if self.cookie is None:
            self.logger.warning("You need to log in first.")
            return None
        
        user_url = "https://users.roblox.com/v1/users/authenticated"
        try:
            authenticated_response = await self.client.get(user_url)
            if authenticated_response.status_code != 200:
                self.logger.error("Could not fetch the authenticated user.")
                return None
            
            authenticated_data = authenticated_response.json()
            user_id = authenticated_data.get('id')
            if user_id is None:
                self.logger.error("User ID not found in the authenticated response.")
                return None

            url = f"https://users.roblox.com/v1/users/{user_id}"
            try:
                response = await self.client.get(url)
                if response.status_code == 200:
                    return response.json()
                else:
                    self.logger.error(f"Could not fetch authenticated user's information: {response.status_code}")
                    return None
            except Exception as e:
                self.logger.error(f"Something went wrong when fetching the authenticated account's information: {e}")
                return None
        
        except Exception as e:
            self.logger.error(f"Something went wrong when fetching the authenticated user: {e}")
            return None
        
    async def get_user_by_id(self, roblox_id):
        if self.cookie is None:
            self.logger.warning("You need to log in first.")
            return None
        
        if isinstance(roblox_id, int) is False:
            return self.logger.error("Please provide an Integer.")
        
        url = f"https://users.roblox.com/v1/users/{roblox_id}"
        try:
            try:
                authenticated_response = await self.client.get(url=url)
            except Exception as e:
                self.logger.error(f"Something went wrong when fetching the authenticated user: {e}")
                return None              
            if authenticated_response.status_code != 200:
                self.logger.error("Could not find that user.")
                return None
            
            return authenticated_response.json()
        
        except Exception as e:
            self.logger.error(f"Something went wrong when fetching the authenticated user: {e}")
            return None

