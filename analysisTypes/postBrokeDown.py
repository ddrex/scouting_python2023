import statistics
#import mysql.connector
def postBrokeDown(analysis, rsRobotMatchData):

    rsCEA = {}
    rsCEA['analysisTypeID'] = 18
    numberOfMatchesPlayed = 0

    # only using to test ranks, eliminate later
    postBrokeDownList = []
    
    # Loop through each match the robot played in.
    for matchResults in rsRobotMatchData:
        rsCEA['team'] = matchResults[analysis.columns.index('team')]
        rsCEA['eventID'] = matchResults[analysis.columns.index('eventID')]
        # We are hijacking the starting position to write DNS or UR. This should go to Auto as it will not
        #   likely be displayed on team picker pages.
        preNoShow = matchResults[analysis.columns.index('preNoShow')]
        scoutingStatus = matchResults[analysis.columns.index('scoutingStatus')]
        if preNoShow == 1:
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = 'DNS'
        elif scoutingStatus == 2:
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = 'UR'
        else:
            
            postBrokeDown = matchResults[analysis.columns.index('postBrokeDown')]
            
            
            if postBrokeDown is None:
                postBrokeDown = 0
            

            postBrokeDownDisplay = postBrokeDown
            postBrokeDownValue = postBrokeDown
            
            if postBrokeDown == 1:
                postBrokeDownColor = 4
            elif postBrokeDown == 0:
                postBrokeDownColor = 2
            
           
            

            # Increment the number of matches played and write M#D, M#V and M#F
            numberOfMatchesPlayed += 1
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'D'] = postBrokeDownDisplay
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'V'] = postBrokeDownValue
            rsCEA['M' + str(matchResults[analysis.columns.index('teamMatchNum')]) + 'F'] = postBrokeDownColor

            postBrokeDownList.append(postBrokeDownValue)

    if numberOfMatchesPlayed > 0:
        rsCEA['S1V'] = round(statistics.mean(postBrokeDownList), 1)
    return rsCEA