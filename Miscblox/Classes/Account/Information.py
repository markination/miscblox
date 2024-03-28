import asyncio
import httpx
from Miscblox.Functions.logger import logger
import json
from Miscblox.Functions.exceptions import RobloxAPIError, RobloxAccountUnauthorized


class AccountInformation():
    def __init__(self, cookie):
        self.cookie = cookie
        self.logger = logger
        self.base_url = "https://accountinformation.roblox.com"
        self.client = httpx.AsyncClient(cookies={".ROBLOSECURITY": cookie})
        if self.cookie is None:
            raise RobloxAccountUnauthorized
    

    async def get_birthdate(self):
        try:
            if self.cookie is None:
                raise RobloxAccountUnauthorized
            
            request = await self.client.get(f"{self.base_url}/v1/birthdate")
            if request.status_code != 200:
                self.logger.error("Something went wrong when connecting to Roblox's API.")
                return None
            
            jsonresponse = request.json()
            if jsonresponse is None:
                return None
            return jsonresponse
        except Exception as e:
            self.logger.error(f"Something went wrong when connecting to Roblox: {e}")
            return None
    
    async def update_birthdate(self, birthMonth: int, birthDay: int, birthYear: int,*, password: str):
        try:
            if self.cookie is None:
                raise RobloxAccountUnauthorized
            

            
            request = await self.client.post(f"{self.base_url}/v1/birthdate", json={"birthMonth": birthMonth, "birthDay": birthDay, "birthYear": birthYear, "password": password})

            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/birthdate", json={"birthMonth": birthMonth, "birthDay": birthDay, "birthYear": birthYear, "password": password}, headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
                    
                    return valid_request.json()
                        
                    
                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
        
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
            
    async def get_description(self):
        try:
            if self.cookie is None:
                raise RobloxAccountUnauthorized
                        
            request = await self.client.get(f"{self.base_url}/v1/description")
            if request.status_code != 200:
                return self.logger.error("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            if jsonresponse is None:
                return None
            return jsonresponse
            
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
    
    async def update_description(self,*, description: str):
        try:
            if self.cookie is None:
                raise RobloxAccountUnauthorized

            request = await self.client.post(f"{self.base_url}/v1/description", json={"description": description})
            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/description", json={"description": description}, headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
                    
                    return valid_request.json()
                        
                    
                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")  
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
    
    async def get_gender(self):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")
            
            request = await self.client.get(f"{self.base_url}/v1/gender")
            if request.status_code != 200:
                return self.logger.error("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            if jsonresponse is None:
                return None
            return jsonresponse
            
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
    
    async def update_gender(self,*, gender: str):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")
 
            request = await self.client.post(f"{self.base_url}/v1/gender", json={"gender": gender})
            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/gender", json={"gender": gender}, headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
                    
                    return valid_request.json()
                        
                    
                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")  
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
        
    async def get_consecutive_xbox_logins(self):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")
            
            request = await self.client.get("https://accountinformation.roblox.com/v1/xbox-live/consecutive-login-days")
            if request.status_code != 200:
                return self.logger.error("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            if jsonresponse is None:
                return None
            return jsonresponse
            
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
        
    async def get_metadata(self):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")
            
            request = await self.client.get("https://accountinformation.roblox.com/v1/metadata")
            if request.status_code != 200:
                return self.logger.error("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            if jsonresponse is None:
                return None
            return jsonresponse
            
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
        
    async def get_phone(self):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")
            
            request = await self.client.get("https://accountinformation.roblox.com/v1/phone")
            if request.status_code != 200:
                return self.logger.error("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            if jsonresponse is None:
                return None
            return jsonresponse
            
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
   
        
    async def update_phone(self, countryCode: str, prefix: str, phone: str, password: str, verificationChannel: str):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")
 
            request = await self.client.post(f"{self.base_url}/v1/phone", json={"countryCode": countryCode, "prefix": prefix, "phone": phone, "password": password, "verificationChannel": verificationChannel})
            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/phone", json={"countryCode": countryCode, "prefix": prefix, "phone": phone, "password": password, "verificationChannel": verificationChannel}, headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
                    
                    return valid_request.json()
                        
                    
                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")  
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
        
    async def delete_phone(self, countryCode: str, prefix: str, phone: str, password: str, verificationChannel: str):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")
 
            request = await self.client.delete(f"{self.base_url}/v1/phone", json={"countryCode": countryCode, "prefix": prefix, "phone": phone, "password": password, "verificationChannel": verificationChannel})
            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/phone/delete", json={"countryCode": countryCode, "prefix": prefix, "phone": phone, "password": password, "verificationChannel": verificationChannel}, headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
                    
                    return valid_request.json()
                        
                    
                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")  
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
        
    async def verify_phone(self,*, code: str):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")
 
            request = await self.client.post(f"{self.base_url}/v1/phone/verify")
            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/phone/verify", headers=headers, json={"code": code})
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
                    
                    return valid_request.json()
                        
                    
                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")  
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
        
    
    async def resend_phone_code(self):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")
 
            request = await self.client.post(f"{self.base_url}/v1/phone/resend")
            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/phone/resend", headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
                    
                    return valid_request.json()
                        
                    
                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")  
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
        
    async def delete_starcode_affiliate(self):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")
 
            request = await self.client.delete(f"{self.base_url}/v1/star-code-affiliates")
            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.delete(f"{self.base_url}/v1/star-code-affiliates", headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")
                    
                    return valid_request.json()
                        
                    
                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")  
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
        
    async def get_starcode_affiliate(self):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")
            
            request = await self.client.get(f"{self.base_url}/v1/star-code-affiliates")
            if request.status_code != 200:
                return self.logger.error("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            if jsonresponse is None:
                return None
            return jsonresponse
            
        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
   
