import hashlib
import hmac
import json
import logging
import urllib

FACEBOOK_API = 'https://graph.facebook.com'

logger = logging.getLogger(__name__)


class AdsAPI(object):
    """A client for the Facebook Ads API."""
    def __init__(self, access_token, app_id, app_secret):
        self.access_token = access_token
        h = hmac.new(access_token, app_id, app_secret)
        self.appsecret_proof = h.hexdigest()
