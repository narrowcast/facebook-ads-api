import os
import unittest

import facebook

USER_ID = os.environ['USER_ID']
ACCOUNT_ID = os.environ['ACCOUNT_ID']
CAMPAIGN_ID = os.environ['CAMPAIGN_ID']
GROUP_ID = os.environ['GROUP_ID']
CREATIVE_ID = os.environ['CREATIVE_ID']
OFFSITE_PIXEL_ID = os.environ['OFFSITE_PIXEL_ID']
PAGE_ID = os.environ['PAGE_ID']
STORY_ID = os.environ['STORY_ID']


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
        self.assertNotIn('error', response)
        self.assertEqual(str(response['data']['app_id']), self.app_id)

    def test_error_handling(self):
        try:
            response = self.api.debug_token('')
        except facebook.AdsAPIError as e:
            pass

    def test_get_adusers(self):
        response = self.api.get_adusers(ACCOUNT_ID)
        self.assertNotIn('error', response)

    def test_get_adaccount(self):
        response = self.api.get_adaccount(ACCOUNT_ID, ['id'])
        self.assertNotIn('error', response)

    def test_get_adaccounts(self):
        response = self.api.get_adaccounts(USER_ID, ['id'])
        self.assertNotIn('error', response)

    def test_get_adcampaign(self):
        response = self.api.get_adcampaign(CAMPAIGN_ID, ['id'])
        self.assertNotIn('error', response)

    def test_get_adcampaigns(self):
        response = self.api.get_adcampaigns(ACCOUNT_ID, ['id'])
        self.assertNotIn('error', response)

    def test_get_adgroup(self):
        response = self.api.get_adgroup(GROUP_ID, ['id'])
        self.assertNotIn('error', response)

    def test_get_adgroups_by_adaccount(self):
        response = self.api.get_adgroups_by_adaccount(ACCOUNT_ID, ['id'])
        self.assertNotIn('error', response)

    def test_get_adgroups_by_adcampaign(self):
        response = self.api.get_adgroups_by_adcampaign(CAMPAIGN_ID, ['id'])
        self.assertNotIn('error', response)

    def test_get_adcreative(self):
        response = self.api.get_adcreative(CREATIVE_ID, ['id'])
        self.assertNotIn('error', response)

    def test_get_adcreatives(self):
        response = self.api.get_adcreatives(ACCOUNT_ID, ['id'])
        self.assertNotIn('error', response)

    def test_get_adimages(self):
        response = self.api.get_adimages(ACCOUNT_ID)
        self.assertNotIn('error', response)

    def test_get_adimages_by_hashes(self):
        response = self.api.get_adimages(ACCOUNT_ID, [
            '1026f5ca40f31a8808732e2c59817c3d',
            '0d65031128a5126fba23f4085f9b5256'])
        self.assertNotIn('error', response)

    def test_get_stats_by_adaccount(self):
        response = self.api.get_stats_by_adaccount(ACCOUNT_ID)
        self.assertNotIn('error', response)

    def test_get_stats_by_adcampaign(self):
        response = self.api.get_stats_by_adcampaign(ACCOUNT_ID)
        self.assertNotIn('error', response)

    def test_get_stats_by_adgroup(self):
        response = self.api.get_stats_by_adgroup(ACCOUNT_ID)
        self.assertNotIn('error', response)

    def test_get_stats_by_adgroup_with_ids(self):
        response = self.api.get_stats_by_adgroup(ACCOUNT_ID, [GROUP_ID])
        self.assertNotIn('error', response)

    def test_get_adreport_stats(self):
        response = self.api.get_adreport_stats(
            ACCOUNT_ID, 'last_28_days', 'all_days', ['account_id'])
        self.assertNotIn('error', response)

    def test_get_conversion_stats_by_adaccount(self):
        response = self.api.get_conversion_stats_by_adaccount(ACCOUNT_ID)
        self.assertNotIn('error', response)

    def test_get_conversion_stats_by_adcampaign(self):
        response = self.api.get_conversion_stats_by_adcampaign(ACCOUNT_ID)
        self.assertNotIn('error', response)

    def test_get_conversion_stats_by_adgroup(self):
        response = self.api.get_conversion_stats_by_adgroup(ACCOUNT_ID)
        self.assertNotIn('error', response)

    def test_get_conversion_stats(self):
        response = self.api.get_conversion_stats(GROUP_ID)
        self.assertNotIn('error', response)

    def test_get_offsite_pixel(self):
        response = self.api.get_offsite_pixel(OFFSITE_PIXEL_ID)
        self.assertNotIn('error', response)

    def test_get_offsite_pixels(self):
        response = self.api.get_offsite_pixels(ACCOUNT_ID)
        self.assertNotIn('error', response)

    def test_get_keyword_stats(self):
        response = self.api.get_keyword_stats(GROUP_ID)
        self.assertNotIn('error', response)

    def test_get_ratecard(self):
        response = self.api.get_ratecard(ACCOUNT_ID)
        self.assertNotIn('error', response)

    def test_get_reach_estimate(self):
        targeting_spec = {'countries': ['KR']}
        response = self.api.get_reach_estimate(
            ACCOUNT_ID, 'KRW', targeting_spec)
        self.assertNotIn('error', response)

    def test_get_adcampaign_list(self):
        responses = self.api.get_adcampaign_list(ACCOUNT_ID)
        for response in responses:
            self.assertNotIn('error', response)

    def test_get_adcampaign_detail(self):
        responses = self.api.get_adcampaign_detail(
            ACCOUNT_ID, CAMPAIGN_ID, 'last_28_days')
        for response in responses:
            self.assertNotIn('error', response)

    def test_get_user_pages(self):
        response = self.api.get_user_pages(USER_ID)
        self.assertNotIn('error', response)

    def test_get_page_access_token(self):
        response = self.api.get_page_access_token(PAGE_ID)
        self.assertNotIn('error', response)

    def test_get_autocomplete_data(self):
        response = self.api.get_autocomplete_data("", 'adcountry', limit=1000)
        self.assertNotIn('error', response)

    def test_create_link_page_post(self):
        response = self.api.create_link_page_post(
            PAGE_ID, 'http://www.youtube.com/watch?v=JJXuBSx_1yE',
            'Link page post creation test',
        )
        self.assertNotIn('error', response)

    def test_create_link_page_post_with_custom_image(self):
        try:
            thumbnail = open('kodim23.png', 'rb')
            response = self.api.create_link_page_post(
                PAGE_ID, 'http://www.virect.com/', thumbnail=thumbnail
            )
            self.assertNotIn('error', response)
        except facebook.AdsAPIError as e:
            print e.message

    def test_create_video_page_post(self):
        try:
            source = open('afm.mp4', 'rb')
            response = self.api.create_video_page_post(PAGE_ID, source=source)
            self.assertNotIn('error', response)
        except facebook.AdsAPIError as e:
            print e.message

    def test_create_video_page_post_with_thumbnail(self):
        try:
            source = open('afm.mp4', 'rb')
            thumbnail = open('kodim23.png', 'rb')
            response = self.api.create_video_page_post(
                PAGE_ID, source=source, thumb=thumbnail)
            self.assertNotIn('error', response)
        except facebook.AdsAPIError as e:
            print e.message

    def test_create_adcampaign(self):
        response = self.api.create_adcampaign(
            ACCOUNT_ID, 'Test Campaign', 1, 100)
        self.assertNotIn('error', response)

    def test_create_adcreative_type_27(self):
        response = self.api.create_adcreative_type_27(
            ACCOUNT_ID, PAGE_ID, story_id=STORY_ID,
            name='Test Type 27 Ad Creative')
        self.assertNotIn('error', response)

    def test_create_adgroup(self):
        targeting = {'geo_locations': {'countries': ['KR']}}
        conversion_specs = [{"action.type": ["offsite_conversion"],
                             "offsite_pixel": [OFFSITE_PIXEL_ID]}]
        response = self.api.create_adgroup(
            ACCOUNT_ID, 'Test Ad Group', 'ABSOLUTE_OCPM', {'ACTIONS': 1000},
            CAMPAIGN_ID, CREATIVE_ID, targeting, conversion_specs
        )
        self.assertNotIn('error', response)

    def test_create_offsite_pixel(self):
        response = self.api.create_offsite_pixel(
            ACCOUNT_ID, 'Test Pixel', 'CHECKOUT')
        self.assertNotIn('error', response)

if __name__ == '__main__':
    unittest.main()
