import OpggScraper
from RiotAPI import API
import SummonerNameToParticipantId
import time
import Plotting


class creds:
    APIKEY = ''    # Riots API key. Get it at https://developer.riotgames.com/
    username = ''       # Your league username (CASE SENSITIVE)
    sololane = True       # Are you a sololaner or botlane?

def main():
    username=creds.username
    OpggScraper.opggloop(username)
    API(creds)
    SummonerNameToParticipantId.summonertoparticipant(username,creds.sololane)
    Plotting.plot()

if __name__ == '__main__':
    main()