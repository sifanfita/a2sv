class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        won_matches = {}
        lost_matches = {}

   
        for winner, loser in matches:
            won_matches[winner] = won_matches.get(winner, 0) + 1
            lost_matches[loser] = lost_matches.get(loser, 0) + 1

    
        not_lost = [player for player in won_matches if lost_matches.get(player, 0) == 0]

   
        lost_once = [player for player in lost_matches if lost_matches[player] == 1]

   
        not_lost.sort()
        lost_once.sort()

        return [not_lost, lost_once]
        