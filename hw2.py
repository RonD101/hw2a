def printCompetitor(competitor):
    '''
    Given the data of a competitor, the function prints it in a specific format.
    Arguments:
        competitor: {'competition name': competition_name, 'competition type': competition_type,
                        'competitor id': competitor_id, 'competitor country': competitor_country, 
                        'result': result}
    '''
    competition_name = competitor['competition name']
    competition_type = competitor['competition type']
    competitor_id = competitor['competitor id']
    competitor_country = competitor['competitor country']
    result = competitor['result']

    assert (isinstance(result, int))  # Updated. Safety check for the type of result

    print(
        f'Competitor {competitor_id} from {competitor_country} participated in {competition_name} ({competition_type}) and scored {result}')


def printCompetitionResults(competition_name, winning_gold_country, winning_silver_country, winning_bronze_country):
    '''
    Given a competition name and its champs countries, the function prints the winning countries 
        in that competition in a specific format.
    Arguments:
        competition_name: the competition name
        winning_gold_country, winning_silver_country, winning_bronze_country: the champs countries
    '''
    undef_country = 'undef_country'
    countries = [country for country in [winning_gold_country, winning_silver_country, winning_bronze_country] if
                 country != undef_country]
    print(f'The winning competitors in {competition_name} are from: {countries}')


def key_sort_competitor(competitor):
    '''
    A helper function that creates a special key for sorting competitors.
    Arguments:
        competitor: a dictionary contains the data of a competitor in the following format: 
                    {'competition name': competition_name, 'competition type': competition_type,
                        'competitor id': competitor_id, 'competitor country': competitor_country, 
                        'result': result}
    '''
    competition_name = competitor['competition name']
    result = competitor['result']
    return (competition_name, result)


def sortKey(dict1):
    return dict1['competition name']


def sortKeyResult(dict1):
    return dict1['result']


def readParseData(file_name):
    '''
    Given a file name, the function returns a list of competitors.
    Arguments: 
        file_name: the input file name. Assume that the input file is in the directory of this script.
    Return value:
        A list of competitors, such that every record is a dictionary, in the following format:
            {'competition name': competition_name, 'competition type': competition_type,
                'competitor id': competitor_id, 'competitor country': competitor_country, 
                'result': result}
    '''
    competitors_in_competitions = []
    # TODO Part A, Task 3.4
    with open(file_name, 'r') as file:
        str_lines = file.readlines()
        country_name = {}
        for str_line in str_lines:
            line_list = str_line.split()
            if line_list[0] == 'competitor':
                country_name[int(line_list[-2])] = line_list[-1]
            else:
                temp_dic = {
                    'competition name': line_list[1],
                    'competition type': line_list[3],
                    'competitor id': int(line_list[2]),
                    'result': int(line_list[4])
                }
                competitors_in_competitions.append(temp_dic.copy())
        for dic_index in competitors_in_competitions:
            dic_index['competitor country'] = country_name[dic_index['competitor id']]
        competitors_in_competitions.sort(key=sortKeyResult)
        competitors_in_competitions.sort(key=sortKey)
    return competitors_in_competitions


def calcCompetitionsResults(competitors_in_competitions):
    '''
    Given the data of the competitors, the function returns the champs countries for each competition.
    Arguments:
        competitors_in_competitions: A list that contains the data of the competitors
                                    (see readParseData return value for more info)
    Retuen value:
        A list of competitions and their champs (list of lists). 
        Every record in the list contains the competition name and the champs, in the following format:
        [competition_name, winning_gold_country, winning_silver_country, winning_bronze_country]
    '''
    competitions_champs = []
    # TODO Part A, Task 3.5
    sports_name = []
    for temp_dict in competitors_in_competitions:
        str_sport = temp_dict['competition name']
        if not str_sport in sports_name:
            sports_name.append(str_sport)
            templist = [str_sport]
            sport_dict = [elem for elem in competitors_in_competitions if elem['competition name'] == str_sport]
            ids = []
            for index in sport_dict:
                ids.append(index['competitor id'])
            for index in sport_dict:
                if ids.count(index['competitor id']) > 1:
                    sport_dict.remove(index)
            if len(sport_dict) == 0:
                continue
            if sport_dict[0]['competition type'] == 'untimed':
                templist.append(sport_dict[-1]['competitor country'])
                if len(sport_dict) > 1:
                    templist.append(sport_dict[-2]['competitor country'])
                    if len(sport_dict) > 2:
                        templist.append(sport_dict[-3]['competitor country'])
                    else:
                        templist.append('undef_country')
                else:
                    templist.append('undef_country')
                    templist.append('undef_country')
            else:
                templist.append(sport_dict[0]['competitor country'])
                if len(sport_dict) > 1:
                    templist.append(sport_dict[1]['competitor country'])
                    if len(sport_dict) > 2:
                        templist.append(sport_dict[2]['competitor country'])
                    else:
                        templist.append('undef_country')
                else:
                    templist.append('undef_country')
                    templist.append('undef_country')
            competitions_champs.append(templist.copy())
    return competitions_champs


def partA(file_name='input.txt', allow_prints=True):
    # read and parse the input file
    competitors_in_competitions = readParseData(file_name)
    if allow_prints:
        # competitors_in_competitions are sorted by competition_name (string) and then by result (int)
        for competitor in sorted(competitors_in_competitions, key=key_sort_competitor):
            printCompetitor(competitor)

    # calculate competition results
    competitions_results = calcCompetitionsResults(competitors_in_competitions)
    if allow_prints:
        for competition_result_single in sorted(competitions_results):
            printCompetitionResults(*competition_result_single)

    return competitions_results


def partB(file_name='input.txt'):
    competitions_results = partA(file_name, allow_prints=False)
    # TODO Part B


if __name__ == "__main__":
    '''
    The main part of the script.
    __main__ is the name of the scope in which top-level code executes.
    
    To run only a single part, comment the line below which correspondes to the part you don't want to run.
    '''
    file_name = 'input.txt'

    partA(file_name)
    partB(file_name)
