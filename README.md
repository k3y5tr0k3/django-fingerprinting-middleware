# django-fingerprinting-middleware
A lightweight Django middleware for generating unique browser fingerprints. Useful for analytics, fraud detection, rate limiting, and session tracking.

## Overview
A lightweight Django middleware for generating unique browser fingerprints. Useful for analytics, fraud detection, rate limiting, and session tracking.
This middleware leverages headers, IP, and user agent information to create a hash-based fingerprint.

## Features
- Simple, server-side browser fingerprinting
- Lightweight

## Installation
```bash
pip install django-fingerprinting-middleware
```

## Usage
Add the middleware to your Django settings.py:
```python
MIDDLEWARE = [
    # ... other middleware
    "browser_fingerprint.middleware.BrowserFingerprintMiddleware",
]
```

Use the fingerprint in your views:
```python
from django.http import JsonResponse

def my_view(request):
    return JsonResponse({
        "fingerprint": request.browser_fingerprint
    })
```

## Roadmap

**v1.0:** Basic Fingerprinting
- Server-side fingerprint from headers and IP
- SHA-256 hash generation
- Middleware integration and example view

**v1.1:** Enhanced Fingerprinting
- Support for cookies to persist fingerprints across sessions
- Optionally combine with device/browser info from user-agents library

**v1.2:**: Frontend Integration
- Optional JS-based fingerprinting (screen size, timezone, fonts)
- Merge server-side and client-side signals for robust uniqueness

**v1.3:** Analytics & Security
- Store fingerprints in the database for tracking
- Support rate-limiting and fraud detection hooks
- Dashboard for visualizing unique visitors

## Contributing
TBD

## License
MIT License. See [LICENSE](LICENSE)
