from django.contrib.auth.models import User
from django.test import TestCase
import statistik.controller as subject

from statistik.models import Chart, Review, Song, UserProfile

class ReviewsTestCases(TestCase):
    def test_get_reviews_for_chart_returns_review_data_for_valid_chart_id(self):
        song = Song(title='Test Song', artist='Kayne West', bpm_min=59, bpm_max=573, game=0, game_version=2)
        song.save()
        chart = Chart(song=song, type=2, difficulty=12)
        chart.save()
        user = User(username='Prim', password='Somebody scream', email='whee@hi.com')
        user.save()
        user_profile = UserProfile(user=user, location='Here', play_side=0, best_techniques=[], max_reviewable=12)
        user_profile.save()
        review = Review(chart=chart, user=user, text='This song sucks', clear_rating='14', characteristics=[], recommended_options=[])
        review.save()

        review_data_list = subject.get_reviews_for_chart(chart.id)

        self.assertEqual(len(review_data_list), 1)

        review_data = review_data_list[0]

        self.assertEqual(review_data['user'], user.username)
        self.assertEqual(review_data['user_id'], user.id)
        self.assertEqual(review_data['playside'], '1P')
        self.assertEqual(review_data['text'], review.text)
        self.assertEqual(review_data['clear_rating'], '14.0')
        self.assertEqual(review_data['hc_rating'], '')
        self.assertEqual(review_data['exhc_rating'], '')
        self.assertEqual(review_data['score_rating'], '')
        self.assertEqual(len(review_data['characteristics']), 0)
        self.assertEqual(len(review_data['recommended_options']), 0)
