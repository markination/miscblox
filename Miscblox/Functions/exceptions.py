from Miscblox.Functions.logger import logger



class RobloxAPIError(Exception):
    """Base class for Roblox API errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
        return logger.error(message + " (ROBLOX API ERROR)")
    
class RobloxAccountUnauthorized(Exception):
    """Base class for no Authorized Account."""
    def __init__(self):
        super().__init__()
        
        return logger.error("Please authorize the client with your roblox account.")
    
