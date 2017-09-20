from django.contrib.auth.models import User
from django.test import TestCase
import statistik.controller as subject

from statistik.models import Chart, Review, Song, UserProfile

class ReviewsTestCases(TestCase):
    def setUp(self):
        self.song = Song(title='Test Song', artist='Kayne West', bpm_min=59, bpm_max=573, game=0, game_version=2)
        self.song.save()
        self.chart = Chart(song=self.song, type=2, difficulty=12)
        self.chart.save()
        self.user = User(username='Prim', password='Somebody scream', email='whee@hi.com')
        self.user.save()
        self.user_profile = UserProfile(user=self.user, location='Here', play_side=0, best_techniques=[], max_reviewable=12)
        self.user_profile.save()

    def tearDown(self):
        Review.objects.all().delete()
        UserProfile.objects.all().delete()
        User.objects.all().delete()
        Chart.objects.all().delete()
        Song.objects.all().delete()

    def test_get_reviews_for_chart_returns_review_data_for_valid_chart_id(self):
        review = Review(chart=self.chart, user=self.user, text='This song sucks', clear_rating='14', characteristics=[], recommended_options=[])
        review.save()

        review_data_list = subject.get_reviews_for_chart(self.chart.id)

        self.assertEqual(len(review_data_list), 1)

        review_data = review_data_list[0]

        self.assertEqual(review_data['user'], self.user.username)
        self.assertEqual(review_data['user_id'], self.user.id)
        self.assertEqual(review_data['playside'], '1P')
        self.assertEqual(review_data['text'], review.text)
        self.assertEqual(review_data['clear_rating'], '14.0')
        self.assertEqual(review_data['hc_rating'], '')
        self.assertEqual(review_data['exhc_rating'], '')
        self.assertEqual(review_data['score_rating'], '')
        self.assertEqual(len(review_data['characteristics']), 0)
        self.assertEqual(len(review_data['recommended_options']), 0)

    def test_get_reviews_for_chart_returns_empty_list_if_no_reviews(self):
        review_data_list = subject.get_reviews_for_chart(self.chart.id)

        self.assertEqual(len(review_data_list), 0)

    def test_get_reviews_for_chart_returns_characteristics_in_proper_format(self):
        self.user_profile.best_techniques = [0, 6]
        self.user_profile.save()
        review = Review(chart=self.chart, user=self.user, text='This song sucks', clear_rating='14', characteristics=[0, 5, 6], recommended_options=[])
        review.save()

        review_data_list = subject.get_reviews_for_chart(self.chart.id)

        self.assertEqual(len(review_data_list), 1)

        actual_characteristics = review_data_list[0]['characteristics']

        expected_characteristics = [
            { 'technique': 'Scratching', 'is_insane': True },
            { 'technique': 'Chord Scales', 'is_insane': False },
            { 'technique': 'Denim', 'is_insane': True }
        ]

        self.assertEqual(len(actual_characteristics), 3)
        self.assertEqual(expected_characteristics, actual_characteristics)