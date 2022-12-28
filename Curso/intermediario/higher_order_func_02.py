print('Brazil x Serbia')
while True:
    team_brazil_goals = input('Tell me Brazil score: ')

    if team_brazil_goals.isdigit():
        brazil_score = int(team_brazil_goals)
        team_serbia_goals = input('Tell me Serbia score: ')

        if team_serbia_goals.isdigit():
            serbia_score = int(team_serbia_goals)
        else:
            print('Enter a valid Value')
            continue


    print('Switzerland x Cameroon')
    team_switzerland_goals = input('Tell me Switerland score: ')

    if team_switzerland_goals.isdigit():
        switzerland_score = int(team_switzerland_goals)
        team_cameroon_goals = input('Tell me Cameroon score: ')

        if team_cameroon_goals.isdigit():
            cameroon_score = int(team_cameroon_goals)
        else:
            print('Enter a valid Value')
            continue
    else:
        print('Enter a valid Value')
        continue    

    break


def group_g_A(team_one='Brazil', team_two='Serbia'):
    def round_one_A(goals_brazil, goals_serbia):
        if goals_brazil > goals_serbia:
            return 'Brazil'
        elif goals_brazil < goals_serbia:
            return 'Serbia'
        else:
            return 'Empate'
    return round_one_A

def group_g_B(team_three='Switzerland', team_four='Cameroon'):
    def round_one_B(goals_switzerland, goals_cameroon):
        if goals_switzerland > goals_cameroon:
            return 'Switzerland'
        elif goals_switzerland < goals_cameroon:
            return 'Cameroon'
        else:
            return 'Empate'
    return round_one_B


def pts(team):
    def winner(points=0):
        points = 0
        points += 3
        return points
    return winner

team_winner_A = group_g_A()
spot_team_A = pts(team_winner_A(brazil_score, serbia_score))

team_winner_B = group_g_B()
spot_team_B = pts(team_winner_B(switzerland_score, cameroon_score))


print('Team             Pts')
print('------------------')
print(f'{team_winner_A(brazil_score, serbia_score)}:           {spot_team_A()}')
print(f'{team_winner_B(switzerland_score, cameroon_score)}:         {spot_team_B()}')












# def salutation(welcome):
#     def your_name(name):
#         return f'{welcome}, {name}'
#     return your_name

# morning = salutation('Good Morning')
# afternoon = salutation('Goof Afternoon')
# evening = salutation('Good Evening')

# for x in ['Jorge', 'Andressa', 'Daniela']:
#     print(morning(x))
#     print(afternoon(x))
#     print(evening(x))