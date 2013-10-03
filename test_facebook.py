import os
import unittest

import facebook


class FacebookAdsAPITest(unittest.TestCase):
    """Tests for Facebook Ads API client."""

    def setUp(self):
        try:
            self.access_token = os.environ['FACEBOOK_ACCESS_TOKEN']
            self.app_id = os.environ['FACEBOOK_APP_ID']
            self.app_secret = os.environ['FACEBOOK_APP_SECRET']
            self.api = facebook.AdsAPI(
                self.access_token, self.app_id, self.app_secret)
        except KeyError:
            raise Exception("FACEBOOK_ACCESS_TOKEN, FACEBOOK_APP_ID, and "
                            "FACEBOOK_APP_SECRET must be set as environmental "
                            "variables.")

    def tearDown(self):
        pass

    def test_debug_token(self):
        response = self.api.debug_token(self.access_token)
        self.assertEqual(str(response['data']['app_id']), self.app_id)

if __name__ == '__main__':
    unittest.main()
