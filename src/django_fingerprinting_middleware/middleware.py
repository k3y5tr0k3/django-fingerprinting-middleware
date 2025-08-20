"""src/django_fingerprinting_middleware/middleware.py.

Django Browser Fingerprinting Middleware

This module provides a middleware class `BrowserFingerprintMiddleware` for
Django applications. The middleware generates a unique fingerprint for each
incoming HTTP request based on headers, the user agent string, IP address,
and other client-specific information.

The fingerprint is computed as a SHA-256 hash of collected fields including:

- IP address of the client
- User-Agent string
- Browser family and version
- Operating system family and version
- Device family
- Accepted languages from HTTP headers

The fingerprint can be used for:

- Identifying returning users without cookies
- Enhancing security by detecting unusual browser signatures
- Rate-limiting or abuse prevention
- Analytics and behavioral tracking

Usage:
    1. Add `BrowserFingerprintMiddleware` to `MIDDLEWARE` in Django settings:
        ```python
        MIDDLEWARE = [
            ...
            'django_fingerprinting_middleware.middleware.BrowserFingerprintMiddleware',
            ...
        ]
        ```

    2. Access the fingerprint in views or other middleware via:
        ```python
        fingerprint = request.browser_fingerprint
        ```

Dependencies:
    - user-agents: For parsing user agent strings.
    - hashlib: Standard library, used to hash the fingerprint.

This middleware is designed to be lightweight and compatible with Django 5+.
"""

import hashlib
from typing import Callable, Dict
from django.http import HttpRequest, HttpResponse
from user_agents import parse


class BrowserFingerprintMiddleware:
    """Middleware that adds a unique browser fingerprint to the request.

    The fingerprint is generated from request headers, user agent, and IP
    information and is available as `request.browser_fingerprint`.
    """

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        """Initialize the middleware.

        Args:
            get_response: The next middleware or view to call.
        """
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """Process the request and attach the browser fingerprint.

        Args:
            request: The incoming HTTP request.

        Returns:
            The response from the next middleware or view.
        """
        request.browser_fingerprint = self.get_fingerprint(request)
        response = self.get_response(request)
        return response

    def get_fingerprint(self, request: HttpRequest) -> str:
        """Generate a unique fingerprint for the given request.

        Args:
            request: The incoming HTTP request.

        Returns:
            A SHA-256 hash representing the browser fingerprint.
        """
        ua_string: str = request.META.get("HTTP_USER_AGENT", "")
        user_agent = parse(ua_string)

        # Collect basic fingerprint info
        data: Dict[str, str] = {
            "ip": request.META.get("REMOTE_ADDR", ""),
            "ua": ua_string,
            "browser": user_agent.browser.family,
            "version": user_agent.browser.version_string,
            "os": user_agent.os.family,
            "os_version": user_agent.os.version_string,
            "device": user_agent.device.family,
            "accept_lang": request.META.get("HTTP_ACCEPT_LANGUAGE", ""),
        }

        # Create a hash for easy storage / comparison
        fingerprint_raw: str = "|".join(f"{k}:{v}" for k, v in data.items())
        fingerprint_hash: str = hashlib.sha256(
            fingerprint_raw.encode("utf-8")
        ).hexdigest()
        return fingerprint_hash
