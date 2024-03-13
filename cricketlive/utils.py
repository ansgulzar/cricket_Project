import requests


def debut_function():
    api_url = f"https://hs-consumer-api.espncricinfo.com/v1/pages/player/home?playerId=253802"
    headers = {'User-Agent': 'YourApp/1.0'}
    response1 = requests.get(api_url, headers=headers)
    data8 = response1.json()['content']['matches']['types']

    # test debut match
    teamA1 = "pak"
    teamA2 = "aus"
    groundA = "Ghazafi stadium"
    dateA = 55 - 2 - 23

    # test recent match
    teamB1 = "pak"
    teamB2 = "aus"
    groundB = "Ghazafi stadium"
    dateB = 55 - 2 - 23

    # ODI debut match
    teamC1 = "pak"
    teamC2 = "aus"
    groundC = "Ghazafi stadium"
    dateC = 55 - 2 - 23

    # ODI recent match
    teamD1 = "pak"
    teamD2 = "aus"
    groundD = "Ghazafi stadium"
    dateD = 55 - 2 - 23

    # T20 debut match
    teamE1 = "pak"
    teamE2 = "aus"
    groundE = "Ghazafi stadium"
    dateE = 55 - 2 - 23

    # T20 recent match
    teamF1 = "pak"
    teamF2 = "aus"
    groundF = "Ghazafi stadium"
    dateF = 55 - 2 - 23

    for a, baby in enumerate(data8):
        if a == 0:
            for b, babe in enumerate(baby['matches']):
                if b == 0:
                    for c, bab in enumerate(babe['events']):
                        if c == 0:
                            groundA = bab['match']['ground']['smallName']
                            dateA = bab['match']['startDate'][:-14]
                            for d, ba in enumerate(bab['match']['teams']):
                                if d == 0:
                                    teamA1 = ba['team']['slug']
                                else:
                                    teamA2 = ba['team']['slug']
                        if c == 1:
                            groundB = bab['match']['ground']['smallName']
                            dateB = bab['match']['startDate'][:-14]
                            for d, ba in enumerate(bab['match']['teams']):
                                if d == 0:
                                    teamB1 = ba['team']['slug']
                                else:
                                    teamB2 = ba['team']['slug']
                # now I am writing code in second iteration for odi matches above code is test matches data
                if b == 1:
                    for c, bab in enumerate(babe['events']):
                        if c == 0:
                            groundC = bab['match']['ground']['smallName']
                            dateC = bab['match']['startDate'][:-14]
                            for d, ba in enumerate(bab['match']['teams']):
                                if d == 0:
                                    teamC1 = ba['team']['slug']
                                else:
                                    teamC2 = ba['team']['slug']
                        if c == 1:
                            groundD = bab['match']['ground']['smallName']
                            dateD = bab['match']['startDate'][:-14]
                            for d, ba in enumerate(bab['match']['teams']):
                                if d == 0:
                                    teamD1 = ba['team']['slug']
                                else:
                                    teamD2 = ba['team']['slug']
                if b == 2:
                    for c, bab in enumerate(babe['events']):
                        if c == 0:
                            groundE = bab['match']['ground']['smallName']
                            dateE = bab['match']['startDate'][:-14]
                            for d, ba in enumerate(bab['match']['teams']):
                                if d == 0:
                                    teamE1 = ba['team']['slug']
                                else:
                                    teamE2 = ba['team']['slug']
                        if c == 1:
                            groundF = bab['match']['ground']['smallName']
                            dateF = bab['match']['startDate'][:-14]
                            for d, ba in enumerate(bab['match']['teams']):
                                if d == 0:
                                    teamF1 = ba['team']['slug']
                                else:
                                    teamF2 = ba['team']['slug']
    return teamA1, teamA2, teamB1, teamB2, teamC1, teamC2, teamD1, teamD2, teamE1, teamE2, teamF1, teamF2, groundA, groundB, groundC, groundD, groundE, groundF, dateA, dateB, dateC, dateD, dateE, dateF


# print("Debut Test Matches")
# print(teamA1, "VS", teamA2, groundA, dateA)
#
# print("Recent Test Matches")
# print(teamB1, "VS", teamB2, groundB, dateB)
#
# print("Debut ODI Matches")
# print(teamC1, "VS", teamC2, groundC, dateC)
#
# print("Recent ODI Matches")
# print(teamD1, "VS", teamD2, groundD, dateD)
#
# print("Debut T20 Matches")
# print(teamE1, "VS", teamE2, groundE, dateE)
#
# print("Recent T20 Matches")
# print(teamF1, "VS", teamF2, groundF, dateF)

# for babe in baby['matches']:
#     for bab in babe['events']:
#         for ba in bab['match']['teams']:
#             print(ba['team']['slug'])
