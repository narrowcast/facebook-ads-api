import hashlib
import hmac
import json
import logging
import urllib
import urllib2

FACEBOOK_API = 'https://graph.facebook.com'

logger = logging.getLogger(__name__)


class AdsAPI(object):
    """A client for the Facebook Ads API."""
    def __init__(self, access_token, app_id, app_secret):
        self.access_token = access_token
        self.app_id = app_id
        self.app_secret = app_secret
        h = hmac.new(access_token, app_secret, hashlib.sha256)
        self.appsecret_proof = h.hexdigest()

    def debug_token(self, token):
        """Returns debug information about the given token."""
        path = 'debug_token'
        args = {
            'input_token': token,
            'access_token': '%s|%s' % (self.app_id, self.app_secret)
        }
        return self.make_request(path, args)

    def make_request(self, path, args):
        """Makes a request against the Facebook Ads API endpoint."""
        url = '%s/%s?%s' % (FACEBOOK_API, path, urllib.urlencode(args))
        logger.info('Making a GET request at %s' % url)
        f = urllib2.urlopen(url)
        return json.load(f)

    def get_adaccount(self, account_id, fields, batch=False):
        """Returns the fields of a Facebook ad account."""
        path = 'act_%s' % account_id
        args = {'fields': fields}
        return self.make_request(path, args)
