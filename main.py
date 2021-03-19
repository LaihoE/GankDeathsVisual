import OpggScraper
from RiotAPI import API
import SummonerNameToParticipantId
import time
import Plotting


class creds:
    APIKEY = 'RGAPI-9ece776f-d779-4af8-82f8-7d6a30cdd8e4'    # Riots API key. Get it at https://developer.riotgames.com/
    username = 'scrubler'       # Your league username (CASE SENSITIVE)
    sololane = True       # Are you a sololaner or botlane?

def main():
    username=creds.username
    OpggScraper.opggloop(username)
    API(creds)
    SummonerNameToParticipantId.summonertoparticipant(username,creds.sololane)
    Plotting.plot()

if __name__ == '__main__':
    main()