import json
import os
import csv



def summonertoparticipant(playername,sololane):
    if sololane==True:
        n_assists=1
    else:
        n_assists=2

    with open(os.path.join(os.path.dirname(__file__), "data", "CSV", "wardtimers.csv"), 'w', newline='\n')as f:
        thewriter = csv.writer(f)
        thewriter.writerow(["game", "placed", "died"])

    with open(os.path.join(os.path.dirname(__file__), "data", "CSV", "killtimers.csv"), 'w', newline='\n')as f:
        thewriter = csv.writer(f)
        thewriter.writerow(["game","kill"])

    for cs in range(1, 21):
        wardtimes = []
        killtimes = []

        paths = {
            "normal": os.path.join(os.path.dirname(__file__), "data", "normaldata", f"game{cs}.json"),
            "timeline": os.path.join(os.path.dirname(__file__), "data", "timelinedata",f"game{cs}.json"),
        }

        with open(paths['normal']) as f:
            x = json.load(f)

        with open(paths['timeline']) as f:
            y = json.load(f)
        # Match the player name to the participantId the player was in the game

        for pl in range(1, 10):
            try:
                if x['participantIdentities'][pl]['player']['summonerName'] == playername:
                    playerid = x['participantIdentities'][pl]['participantId']
                    # WARDTIMER
                    for m in range(100):
                        for i in range(100):
                            try:
                                if y['frames'][m]['events'][i]['type'] == 'WARD_PLACED':
                                    if y['frames'][m]['events'][i]['creatorId'] == playerid:
                                        timestamp = y['frames'][m]['events'][i]['timestamp']
                                        wardtimes.append(timestamp)
                            except:
                                pass
                    print(wardtimes)
                    # KILLTIMER
                    for m in range(100):
                        for i in range(100):

                            try:
                                if y['frames'][m]['events'][i]['type'] == 'CHAMPION_KILL':
                                    print("1",y['frames'][m]['events'][i]['victimId'])
                                    if y['frames'][m]['events'][i]['victimId'] == playerid:
                                        print("2",y['frames'][m]['events'][i]['assistingParticipantIds'])
                                        print('beforN_ass')
                                        if len(y['frames'][m]['events'][i]['assistingParticipantIds']) == n_assists:
                                            timestamp = y['frames'][m]['events'][i]['timestamp']
                                            killtimes.append(timestamp)
                                            print("Final")
                            except:
                                pass
            except:
                pass

        for x in killtimes:
            y = x / 1000 / 60
            with open(os.path.join(os.path.dirname(__file__), "data", "CSV", "killtimers.csv"), 'a', newline='\n')as f:
                thewriter = csv.writer(f)
                thewriter.writerow([cs,y])


        wardplaced = []
        warddied = []
        for x in wardtimes:
            y = x / 1000 / 60
            z = (x + 100000) / 1000 / 60
            wardplaced.append(y)
            warddied.append(z)
            with open(os.path.join(os.path.dirname(__file__), "data", "CSV", "wardtimers.csv"), 'a', newline='\n')as f:
                thewriter = csv.writer(f)
                thewriter.writerow([cs, y, z])