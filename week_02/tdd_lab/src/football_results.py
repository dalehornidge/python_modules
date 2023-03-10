def get_result(final_score):
    print(final_score)
    if final_score["home_team"] > final_score["away_team"]:
        return "Home Win!"
    if final_score["home_team"] == final_score["away_team"]:
        return "Both teams draw!"
    else:
        return "Away Win!"
    
        

def get_league_results(final_scores):
    for game in final_score_full_league:
        if 