import unittest

import facebook


class FacebookAdsAPITest(unittest.TestCase):
    """Tests for Facebook Ads API client."""

    def setUp(self):
        try:
            self.app_id = os.environ['FACEBOOK_APP_ID']
            self.app_secret = os.environ['FACEBOOK_APP_SECRET']
        except KeyError:
            raise Exception("FACEBOOK_APP_ID and FACEBOOK_APP_SECRET "
                            "must be set as environmental variables.")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
