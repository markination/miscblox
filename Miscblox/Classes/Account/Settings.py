import asyncio
import httpx
from Miscblox.Functions.logger import logger
import json
from datetime import date

class AccountSettings():
    def __init__(self, cookie):
        self.cookie = cookie
        self.logger = logger
        self.base_url = "https://accountsettings.roblox.com"
        self.client = httpx.AsyncClient(cookies={".ROBLOSECURITY": cookie})
        if self.cookie is None:
            self.logger.error("Please login with your Roblox account.")

    async def get_account_country(self):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")

            request = await self.client.get(f"{self.base_url}/v1/account/settings/account-country")
            if request.status_code != 200:
                return self.logger.error("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            return jsonresponse

        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")

    async def update_account_country(self, country_id: int):
        try:
            if self.cookie is None:
                self.logger.error("Please login with your Roblox account.")
                return None



            request = await self.client.post(f"{self.base_url}/v1/account/settings/account-country",json={"targetCountryId": country_id})
            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/account/settings/account-country",json={"targetCountryId": country_id}, headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")

                    return valid_request.json()


                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")

        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")

    async def get_account_metadata(self):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")

            request = await self.client.get(f"{self.base_url}/v1/account/settings/metadata")
            if request.status_code != 200:
                return self.logger.error("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            return jsonresponse

        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")

    async def get_account_email(self):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")

            request = await self.client.get(f"{self.base_url}/v1/email")
            if request.status_code != 200:
                return self.logger.error("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            return jsonresponse

        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")

    async def update_account_email(self, password: str, emailAddress: str, skipVerificationEmail: bool, isAdsAccount: bool):
        try:
            if self.cookie is None:
                self.logger.error("Please login with your Roblox account.")
                return None



            request = await self.client.post(f"{self.base_url}/v1/email",json={"password": password, "emailAddress": emailAddress, "skipVerfiiationEmail": skipVerificationEmail, "isAfsAccount": isAdsAccount})
            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/email",json={"password": password, "emailAddress": emailAddress, "skipVerfiiationEmail": skipVerificationEmail, "isAfsAccount": isAdsAccount}, headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")

                    return valid_request.json()


                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")

        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")


    async def verify_account_email(self, freeItem: bool, isAdsAccount: bool):
        try:
            if self.cookie is None:
                self.logger.error("Please login with your Roblox account.")
                return None



            request = await self.client.post(f"{self.base_url}/v1/email/verify",json={"freeItem": freeItem, "isAdsAccount": isAdsAccount})
            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/email/verify",json={"freeItem": freeItem, "isAdsAccount": isAdsAccount}, headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")

                    return valid_request.json()


                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")

        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")

    async def get_blocked_accounts(self):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")

            request = await self.client.get(f"{self.base_url}/v1/users/get-detailed-blocked-users")
            if request.status_code != 200:
                return self.logger.error("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            return jsonresponse

        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")

    async def block_account(self, userId: int):
        try:
            if self.cookie is None:
                self.logger.error("Please login with your Roblox account.")
                return None



            request = await self.client.post(f"{self.base_url}/v1/users/{userId}/block")
            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/users/{userId}/block", headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")

                    return valid_request.json()


                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")

        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")

    async def unblock_account(self, userId: int):
        try:
            if self.cookie is None:
                self.logger.error("Please login with your Roblox account.")
                return None



            request = await self.client.post(f"{self.base_url}/v1/users/{userId}/unblock")
            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/users/{userId}/unblock", headers=headers)
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")

                    return valid_request.json()


                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")

        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")

    async def get_trade_privacy(self):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")

            request = await self.client.get(f"{self.base_url}/v1/trade-privacy")
            if request.status_code != 200:
                return self.logger.error("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            return jsonresponse

        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")

    async def get_trade_quality(self):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")

            request = await self.client.get(f"{self.base_url}/v1/trade-value")
            if request.status_code != 200:
                return self.logger.error("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            return jsonresponse

        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")

    async def update_trade_privacy(self, tradePrivacy: int):
        try:
            if self.cookie is None:
                self.logger.error("Please login with your Roblox account.")
                return None



            request = await self.client.post(f"{self.base_url}/v1/trade-privacy", json={"tradePrivacy": tradePrivacy})
            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/trade-privacy", headers=headers, json={"tradePrivacy": tradePrivacy})
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")

                    return valid_request.json()


                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")

        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")

    async def update_trade_quality(self, tradeValue: int):
        try:
            if self.cookie is None:
                self.logger.error("Please login with your Roblox account.")
                return None



            request = await self.client.post(f"{self.base_url}/v1/trade-privacy", json={"tradeValue": tradeValue})
            if request.status_code != 200:
                if request.status_code == 403:
                    find = request.headers.get("X-CSRF-TOKEN")
                    headers ={"X-CSRF-TOKEN": find}
                    valid_request = await self.client.post(f"{self.base_url}/v1/trade-privacy", headers=headers, json={"tradeValue": tradeValue})
                    if valid_request.status_code != 200:
                        return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")

                    return valid_request.json()


                return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {request.status_code} | {request.text}")

        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
