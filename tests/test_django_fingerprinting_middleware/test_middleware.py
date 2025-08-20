"""tests/test_middleware.py.

Unit tests for BrowserFingerprintMiddleware.

These tests cover:
- Correct fingerprint generation
- Consistency of the fingerprint
- Handling of missing headers
"""

import pytest
from django.test import RequestFactory
from django.http import HttpRequest, HttpResponse

from src.django_fingerprinting_middleware.middleware import BrowserFingerprintMiddleware


@pytest.fixture
def rf() -> RequestFactory:
    """Return a Django RequestFactory instance for creating test requests."""
    return RequestFactory()


def dummy_get_response(request: HttpRequest) -> HttpResponse:
    """A dummy get_response function for middleware testing.

    Args:
        request: The Django HTTP request object.

    Returns:
        HttpResponse: A simple HTTP response.
    """
    return HttpResponse("OK")


def test_fingerprint_added_to_request(rf: RequestFactory) -> None:
    """Test that the middleware adds a `browser_fingerprint` attribute.

    Args:
        rf: Django RequestFactory fixture.
    """
    request: HttpRequest = rf.get("/")
    middleware = BrowserFingerprintMiddleware(dummy_get_response)

    response: HttpResponse = middleware(request)

    assert hasattr(request, "browser_fingerprint")
    assert isinstance(request.browser_fingerprint, str)
    assert len(request.browser_fingerprint) == 64  # SHA-256 hash length
    assert response.status_code == 200


def test_fingerprint_is_consistent_for_same_request(rf: RequestFactory) -> None:
    """Test that the fingerprint is consistent for the same request.

    Args:
        rf: Django RequestFactory fixture.
    """
    request1: HttpRequest = rf.get("/", HTTP_USER_AGENT="TestAgent/1.0")
    request2: HttpRequest = rf.get("/", HTTP_USER_AGENT="TestAgent/1.0")

    middleware = BrowserFingerprintMiddleware(dummy_get_response)

    fingerprint1: str = middleware.get_fingerprint(request1)
    fingerprint2: str = middleware.get_fingerprint(request2)

    assert fingerprint1 == fingerprint2


def test_fingerprint_changes_for_different_user_agents(rf: RequestFactory) -> None:
    """Test that different user agents produce different fingerprints.

    Args:
        rf: Django RequestFactory fixture.
    """
    request1: HttpRequest = rf.get("/", HTTP_USER_AGENT="AgentA/1.0")
    request2: HttpRequest = rf.get("/", HTTP_USER_AGENT="AgentB/1.0")

    middleware = BrowserFingerprintMiddleware(dummy_get_response)

    fingerprint1: str = middleware.get_fingerprint(request1)
    fingerprint2: str = middleware.get_fingerprint(request2)

    assert fingerprint1 != fingerprint2


def test_fingerprint_handles_missing_headers(rf: RequestFactory) -> None:
    """Test that the middleware works even if some headers are missing.

    Args:
        rf: Django RequestFactory fixture.
    """
    request: HttpRequest = rf.get("/")

    request.META.pop("HTTP_USER_AGENT", None)
    request.META.pop("HTTP_ACCEPT_LANGUAGE", None)
    request.META.pop("REMOTE_ADDR", None)

    middleware = BrowserFingerprintMiddleware(dummy_get_response)
    fingerprint: str = middleware.get_fingerprint(request)

    assert isinstance(fingerprint, str)
    assert len(fingerprint) == 64
