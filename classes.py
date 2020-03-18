import numpy as np
import matplotlib.pyplot as plt
import pickle as pkl

class candidate(object):
    def __init__(self, name, party, constituency, votes, total_votes, alliance):
        self.name = name
        self.party = party
        self.constituency = constituency
        self.votes = votes
        self.total_votes = total_votes
        self.alliance = alliance
        
    def percentageOfVotes(self):
        return 100*self.votes/self.total_votes
        
    def __str__(self):
        output = "Candidate\nName: " + self.name + "\n"
        output += "Party: " + self.party + "\n"
        output += "Constituency: " + self.constituency + "\n"
        output += "Votes: " + str(self.votes) + " (" + str(round(self.percentageOfVotes(), 2)) + "%)\n"
        return output
        
class constituency(object):
    def __init__(self, name, total_voters, total_electors, state):
        self.name = name
        self.total_voters = total_voters
        self.total_electors = total_electors
        self.state = state
        self.candidates = []

    def addCandidate(self, name, party, constituency, votes, total_votes, alliance):
        c = candidate(name, party, constituency, votes, total_votes, alliance)
        self.candidates.append(c)
        self.candidates.sort(key = lambda i: i.votes, reverse = True)

    def winner(self):
        return self.candidates[0]

    def winningMargin(self, percentage):
        if len(self.candidates) > 1:
            difference = self.candidates[0].votes - self.candidates[1].votes
        else:
            difference = self.candidates[0].votes
        if percentage:
            return difference/self.total_voters
        else:
            return difference
        
    def percentageTurnout(self):
        return 100*self.total_voters/self.total_electors
        
    def __str__(self):
        output = "Constituency: " + self.name + "\n"
        output += "Voters: " + str(self.total_voters) + " (" + str(round(self.percentageTurnout(), 2)) + "% turnout)\n"
        output += "State: " + self.state + "\n"
        output += "Candidates: " + str(len(self.candidates))
        return output

class elections(object):
    def __init__(self, name, year, winner_alliance):
        self.name = name
        self.year = year
        self.constituencies = []
        self.winner_alliance = winner_alliance

    def addConstituency(self, name, total_voters, total_electors, state):
        c = constituency(name, total_voters, total_electors, state)
        self.constituencies.append(c)

    def addCandidate(self, name, party, constituency, votes, total_votes, alliance, total_electors, state):
        for i in range(len(self.constituencies)):
            if self.constituencies[i].name == constituency:
                self.constituencies[i].addCandidate(name, party, constituency, votes, total_votes, alliance)
                return

    def winner(self):
        return self.winner_alliance

    def percentageTurnout(self):
        turnout = 0
        total = 0
        for i in self.constituencies:
            turnout += i.total_voters
            total += i.total_electors
        return 100*turnout/total
    
    def __str__(self):
        output = self.name + " " + str(self.year)
        output += "Winner: " + self.winner + "\n"
        output += "Turnout: " + str(round(self.percentageTurnout(), 2))
        return output
