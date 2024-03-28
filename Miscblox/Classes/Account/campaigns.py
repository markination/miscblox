import asyncio
import httpx
from Miscblox.Functions.logger import logger
import json
from array import array
from datetime import date
from Miscblox.Functions.exceptions import RobloxAPIError, RobloxAccountUnauthorized


class CampaignConfiguration():
    def __init__(self, cookie):
        self.cookie = cookie
        self.logger = logger
        self.base_url = "adconfiguration.roblox.com"
        self.client = httpx.AsyncClient(cookies={".ROBLOSECURITY": cookie})
        if self.cookie is None:
            self.logger.error("Please login with your Roblox account.")
    
    async def get_sponsored_campaigns(self, campaignTargetType: int, campaignTargetId: int, includeReportingStats: bool = None, isArchived: bool = None):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")
            
            request = await self.client.get(f"{self.base_url}/v2/sponsored-campaigns", json={"campaignTargetType": campaignTargetType, "campaignTargetId": campaignTargetId, "includeReportingStats": includeReportingStats, "isArchived": isArchived})
            if request.status_code != 200:
                raise RobloxAPIError("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            return jsonresponse

        except Exception as e:
            return self.logger.error(f"Something went wrong when connecting to Roblox's API. | {e}")
    
    async def get_eligible_campaign_assets(self):
        try:
            if self.cookie is None:
                raise RobloxAccountUnauthorized

            request = await self.client.get(f"{self.base_url}/v2/sponsored-campaigns/eligible-asset-type-ids")
            if request.status_code != 200:
                raise RobloxAPIError("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            return jsonresponse

        except Exception as e:
            raise RobloxAPIError("Something went wrong when connecting to Roblox's API.")


    async def items_is_eligible_for_sponsorship(self, campaignTargetType: int, campainTargetIds: list):
        try:
            if self.cookie is None:
                return self.logger.error("Please login with your roblox account.")

            request = await self.client.get(f"{self.base_url}/v2/sponsored-campaigns/multi-get-can-user-sponsor", json={"campaginTargetType": campaignTargetType, "campaignTargetIds": campainTargetIds})
            if request.status_code != 200:
                raise RobloxAPIError("Something went wrong when connecting to Roblox's API.")
            jsonresponse = request.json()
            return jsonresponse


        except Exception as e:
            raise RobloxAPIError("Something went wrong when connecting to Roblox's API.")



