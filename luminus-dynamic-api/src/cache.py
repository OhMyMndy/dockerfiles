from requests_cache import CachedSession, timedelta

session = CachedSession(
    "./cache/requests",
    expire_after=timedelta(hours=1),
    stale_if_error=True,
    # ~/.cache/app
    backend="filesystem",
)
