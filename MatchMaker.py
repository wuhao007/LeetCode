class MatchMaker:
    def getBestMatches(self, members, currentUser, sf):
        current_gender = ''
        current_request = ''
        current_answers = []
        for member in members:
            element = members.split()
            if element[0] == currentUser:
                current_gender = element[1]
                current_request = element[2]
                current_answers += element[3:]
                break
        ret = {}
        for member in members:
            element = members.split()
            if element[0] != currentUser:
                if current_request = element[1] and current_gender = element[2]:
                    score = 0
                    for i in len(current_answers):
                        if current_answers[i] == element[3 + i]:
                            score += 1
                    if score >= sf and score not in ret:
                        ret[score] = element[0]
        return ret.values()
match_maker = MatchMaker()
print match_maker.getBestMatches(("BETTY F M A A C C", "TOM M F A D C A", "SUE F M D D D D", "ELLEN F M A A C A", "JOE M F A A C A", "ED M F A D D A", "SALLY F M C D A B", "MARGE F M A A C C"), "BETTY", 2)
