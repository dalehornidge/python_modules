import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):

    def setUp(self):
      self.final_score_home_win = {
         "home_team": 1,
         "away_team": 0
      }
      
      self.final_score_away_win = {
         "home_team": 1,
         "away_team": 3
      }
      
      self.final_score_draw = {
         "home_team": 1,
         "away_team": 1
      }

      self.final_score_full_league = { 
         "Game_1": {
         "home_team": 1,
         "away_team": 0
      }, 
      "Game_2": {
         "home_team": 1,
         "away_team": 3
      },
      "Game_3":
        {
         "home_team": 1,
         "away_team": 1
      }  
      }

      
      
    def test_check_results_home_win(self):
        self.assertEqual("Home Win!", get_result(self.final_score_home_win))

    def test_check_results_draw(self):
       self.assertEqual("Both teams draw!", get_result(self.final_score_draw))

    def test_check_results_away_win(self):
       self.assertEqual("Away Win!", get_result(self.final_score_away_win))

    

    # Test we get the right result string for a final score dictionary representing -

        # Home win
        # Away win
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 




