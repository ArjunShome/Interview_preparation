from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
import time
from typing import Dict
from log import logger

# Rate limiter on Client IP
# Can be modified to add rate limiting on client_ip and route
class RateLimiter(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.rate_limit_records: Dict[str, float] = {}
        self.exempt_paths = ["/docs", "/openapi.json", "/redoc", "/favicon.ico"]
        self.rate_limit = 1.0  # requests per second
        self.interval = 1.0 / self.rate_limit
        
    
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        current_time = time.monotonic()
        client_ip = request.client.host
        path = request.url.path

        prev = self.rate_limit_records.get(client_ip)
        if path not in self.exempt_paths:
            if prev is not None:
                elapsed = current_time - prev
                if elapsed < self.interval:
                    retry_after = max(0.0, self.interval - elapsed)
                    logger.warning(f"Rate limit exceeded for IP: {client_ip}")
                    return JSONResponse(
                        status_code=429,
                        content={"message": "Too Many Requests. Please try again later."},
                        headers={
                            "X-Rate-Limit-exceeded": "true",
                            "X-Retry-After": f"{retry_after} seconds"
                        },
                    )
        self.rate_limit_records[client_ip] = current_time
        response = await call_next(request)
        response.headers["X-Rate-Limit-exceeded"] = "false"
        return response