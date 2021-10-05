import random
def element_trump(elem_a, elem_b):
    # return 1 to mean that A beats B, -1 to mean that B beats A
    beat_pairs = [ ('W', 'F'), ('F', 'E'), ('E', 'W') ]
    for pair in beat_pairs:
        if elem_a == pair[0] and elem_b == pair[1]:
            return(1)
        if elem_a == pair[1] and elem_b == pair[0]:
            return(-1)
    return(0)

def hero_fight(hero_a, hero_b):
    # return 1 if A wins, -1 if B wins
    element_result = element_trump(hero_a['element'], hero_b['element'])
    if element_result == 0:
        if hero_a['power'] == 1 and hero_b['power'] == 6:
            return(1)
        elif hero_a['power'] == 6 and hero_b['power'] == 1:
            return(-1)
        elif hero_a['power'] > hero_b['power']:
            return(1)
        elif hero_a['power'] < hero_b['power']:
            return(-1)
        else:
            return(random.choice([1,-1]))
    else:
        return(element_result)

def team_fight(team_a, team_b, verbose=False):
    a_lineup = [a for a in team_a]
    b_lineup = [b for b in team_b]
    if verbose:
        print('Teams are ready to fight!')
        print('Team A:')
        print_team(a_lineup)
        print('Team B:')
        print_team(b_lineup)
        
    while(len(a_lineup) > 0 and len(b_lineup) > 0):
        a_fighter = random.choice(a_lineup)
        b_fighter = random.choice(b_lineup)
        if verbose:
            print('{} from team A fights {} from team B...'.format(a_fighter['name'], b_fighter['name']))
        result = hero_fight(a_fighter, b_fighter)
        if result == 1:
            b_lineup.remove(b_fighter)
            if verbose:
                print('{} from team A wins!'.format(a_fighter['name']))
        else:
            assert(result == -1)
            a_lineup.remove(a_fighter)
            if verbose:
                print('{} from team B wins!'.format(b_fighter['name']))
                
    if len(a_lineup):
        if verbose:
            print('Team A wins! Remaining alive:')
            print(a_lineup)
        return(1)
    else:
        assert(len(b_lineup))
        if verbose:
            print('Team B wins!  Remaining alive:')
            print(b_lineup)
        return(-1)

def team_matchup_evaluate(team_a, team_b, runs=1000, verbose=False):
    runs_done = 0
    a_wins = 0
    b_wins = 0
    while runs_done < runs:
        runs_done = runs_done + 1
        result = team_fight(team_a, team_b)
        if result == 1:
            a_wins = a_wins + 1
        else:
            assert(result == -1)
            b_wins = b_wins + 1
    if verbose:
        print('Team A wins {}/{} ({}%)'.format(a_wins, runs, 100 * a_wins / runs))
        print('Team B wins {}/{} ({}%)'.format(b_wins, runs, 100 * b_wins / runs))

    return((a_wins, b_wins))

def random_matchup_evaluate(team_a, runs=1000, verbose=False):
    runs_done = 0
    a_wins = 0
    b_wins = 0
    while runs_done < runs:
        runs_done = runs_done + 1
        team_b = get_random_team()
        result = team_fight(team_a, team_b)
        if result == 1:
            a_wins = a_wins + 1
        else:
            assert(result == -1)
            b_wins = b_wins + 1
    if verbose:
        print('Team A wins {}/{} ({}%)'.format(a_wins, runs, 100 * a_wins / runs))
        print('Team B wins {}/{} ({}%)'.format(b_wins, runs, 100 * b_wins / runs))

    return((a_wins, b_wins))

heroes = [
    {
        'name' : 'Arch-Alligator',
        'element' : 'W',
        'power' : 1,
        'popularity' : 1.3
    },
    {
        'name' : 'Blaze Boy',
        'element' : 'F',
        'power' : 6
    },
    {
        'name' : 'Captain Canoe',
        'element' : 'W',
        'power' : 2
    }, 
    {
        'name' : 'Dire Druid',
        'element' : 'E',
        'power' : 3,
        'popularity' : 0.8
    },
    {
        'name' : 'Earth Elemental',
        'element' : 'E',
        'power' : 2,
    },
    {
        'name' : 'Fire Fox',
        'element' : 'F',
        'power' : 3,
        'popularity' : 1.5,
    },
    {
        'name' : 'Greenery Giant',
        'element' : 'E',
        'power' : 6,
        'popularity' : 0.8
    },
    {
        'name' : 'Inferno Imp',
        'element' : 'F',
        'power' : 4,
        'popularity' : 1.3,
    },
    {
        'name' : 'Landslide Lord',
        'element' : 'E',
        'power' : 1
    },
    {
        'name' : 'Maelstrom Mage',
        'element' : 'W',
        'power' : 3,
        'popularity' : 1.8
    },
    {
        'name' : 'Nullifying Nightmare',
        'element' : 'V',
        'power' : 5,
        'popularity' : 0.8
    },
    {
        'name' : 'Oil Ooze',
        'element' : 'F',
        'power' : 2
    },
    {
        'name' : 'Phoenix Paladin',
        'element' : 'F',
        'power' : 5,
    },
    {
        'name' : 'Quartz Questant',
        'element' : 'E',
        'power' : 4,
        'popularity' : 0.8
    },
    {
        'name' : 'Rock-n-Roll Ranger',
        'element' : 'E',
        'power' : 5,
        'popularity' : 0.6
    },
    {
        'name' : 'Siren Sorceress',
        'element' : 'W',
        'power' : 4,
        'popularity' : 2.0
    },
    {
        'name' : 'Tidehollow Tyrant',
        'element' : 'W',
        'power' : 6,
        'popularity' : 1.4
    },

    {
        'name' : 'Volcano Villain',
        'element' : 'F',
        'power' : 1,
        'popularity' : 1.3
    },
    {
        'name' : 'Warrior of Winter',
        'element' : 'W',
        'power' : 5,
        'popularity' : 1.2
    },
]

for hero in heroes:
    if 'popularity' not in hero.keys():
        hero['popularity'] = 1
        
def get_random_team():
    team = []
    popularities = [ h['popularity'] for h in heroes ]
    while len(team) < 5:
        new_hero = random.choices(heroes, weights=popularities, k=1)[0]
        if new_hero not in team:
            team.append(new_hero)
    return(team)

def get_hero_by_stats(heroes, element, power):
    heroes = [ h for h in heroes if h['element'] == element ]
    heroes = [ h for h in heroes if h['power'] == power ]
    assert(len(heroes) == 1)
    return(heroes[0])

def print_hero(hero):
    print('{} ({}{})'.format(hero['name'], hero['element'], hero['power']))

def print_team(team):
    for hero in team:
        print_hero(hero)
    
def make_records(heroes):
    hero_records = {}
    for hero in heroes:
        hero_records[hero['name']] = { 'wins' : 0, 'losses' : 0 }

    runs = 0
    while runs < 846138: 
        runs = runs + 1
        team_blue = get_random_team()
        team_green = get_random_team()
        result = team_fight(team_blue, team_green, verbose=False)
        log_file = team_blue + team_green + [ 'Blue Team Wins' if result == 1 else 'Green Team Wins' ]
        log(log_file)
        alt_log_file = []
        for hero in heroes:
            alt_log_file.append(True if hero in team_blue else False)
            alt_log_file.append(True if hero in team_green else False)
        alt_log_file.append(True if result == 1 else False)
        alt_log_file.append(True if result == -1 else False)
        log(alt_log_file, alt_location=True)
            
        if result == 1:
            for hero in team_blue:
                hero_records[hero['name']]['wins'] = hero_records[hero['name']]['wins'] + 1
            for hero in team_green:
                hero_records[hero['name']]['losses'] = hero_records[hero['name']]['losses'] + 1
        else:
            assert(result == -1)
            for hero in team_green:
                hero_records[hero['name']]['wins'] = hero_records[hero['name']]['wins'] + 1
            for hero in team_blue:
                hero_records[hero['name']]['losses'] = hero_records[hero['name']]['losses'] + 1                                                         
        

    full_records = []
    for hero in heroes:
        record = hero_records[hero['name']]
        record['name'] = hero['name']
        record['element'] = hero['element']
        record['power'] = hero['power']
        record['win_rate'] = record['wins'] / (record['wins'] + record['losses'])
        full_records.append(record)
        
    full_records.sort(key=lambda r : r['win_rate'])
    
    for r in full_records:
        wins = r['wins']
        losses = r['losses']
        print('{} ({}{}) has been in {} fights, won {} and lost {} ({:.2f}% win rate)'.format(r['name'], r['element'], r['power'], wins + losses, wins, losses, 100 * wins / (wins + losses)))

def format_for_log(c):
    if type(c) == str:
        return(c)
    elif type(c) == dict:
        return(c['name'])
    elif c == True:
        return('1')
    elif c == False:
        return('0')
    else:
        assert(False)
        
def log(contents, overwrite=False, alt_location=False):
    location = "hero_league_player_log_alt.csv" if alt_location else "hero_league_player_log.csv"
    contents = [ format_for_log(c) for c in contents ]
    message = ",".join(contents) + '\n'
    file = open(location, 'w' if overwrite else 'a')  # a = append mode
    file.write(message)

def setup_logs():
    log(['Blue 1', 'Blue 2', 'Blue 3', 'Blue 4', 'Blue 5', 'Green 1', 'Green 2', 'Green 3', 'Green 4', 'Green 5', 'Result'], overwrite=True)
    alt_log_header = []
    for hero in heroes:
        alt_log_header.append('{}_on_Blue'.format(hero['name']))
        alt_log_header.append('{}_on_Green'.format(hero['name']))
    alt_log_header.append('Blue_Win')
    alt_log_header.append('Green_Win')
    log(alt_log_header, overwrite=True, alt_location=True)

def select_team_from_params(heroes, include_nightmare, fire_heroes, water_heroes, earth_heroes, fire_1, water_1, earth_1):
    team = []
    if include_nightmare:
        nm = [h for h in heroes if h['element'] == 'V']
        team.append(nm[0])
    fire_number = 1 if fire_1 else 6
    while fire_heroes > 0:
        fh = [h for h in heroes if h['element'] == 'F' and h['power'] == fire_number]
        team.append(fh[0])
        fire_number = 6 if fire_number == 1 else (fire_number - 1)
        fire_heroes = fire_heroes - 1
        
    water_number = 1 if water_1 else 6
    while water_heroes > 0:
        fh = [h for h in heroes if h['element'] == 'W' and h['power'] == water_number]
        team.append(fh[0])
        water_number = 6 if water_number == 1 else (water_number - 1)
        water_heroes = water_heroes - 1
    
    earth_number = 1 if earth_1 else 6
    while earth_heroes > 0:
        fh = [h for h in heroes if h['element'] == 'E' and h['power'] == earth_number]
        team.append(fh[0])
        earth_number = 6 if earth_number == 1 else (earth_number - 1)
        earth_heroes = earth_heroes - 1

    assert(len(team) == 5)
    return(team)

def list_potential_teams(heroes):
    teams = []
    for include_nightmare in [True, False]:
        slots_left_after_n = 5 - (1 if include_nightmare else 0)
        for fire_heroes in range(0, slots_left_after_n + 1):
            slots_left_after_f = slots_left_after_n - fire_heroes
            for water_heroes in range(0, slots_left_after_f + 1):
                earth_heroes = slots_left_after_f - water_heroes
                fire_1_possibilities = [False] if fire_heroes == 0 else [False,True]
                water_1_possibilities = [False] if water_heroes == 0 else [False,True]
                earth_1_possibilities = [False] if earth_heroes == 0 else [False,True]
                for fire_1 in fire_1_possibilities:
                    for water_1 in water_1_possibilities:
                        for earth_1 in earth_1_possibilities:
                            teams.append(select_team_from_params(heroes, include_nightmare, fire_heroes, water_heroes, earth_heroes, fire_1, water_1, earth_1))
    return(teams) 

def optimize_vs_npcs(heroes):
    teams = list_potential_teams(heroe*s)
    print('Found {} potentially optimal teams.'.format(len(teams)))

    enemy_team = [
        get_hero_by_stats(heroes, 'F', 5),
        get_hero_by_stats(heroes, 'W', 6),
        get_hero_by_stats(heroes,'E', 3),
        get_hero_by_stats(heroes, 'E', 4),
        get_hero_by_stats(heroes, 'E', 6),
    ]
    outcomes = []
    for team in teams:
        res = team_matchup_evaluate(team, enemy_team, runs=10000)
        outcomes.append({'team' : team, 'wins' : res[0]})

    outcomes.sort(key= lambda x : x['wins'], reverse=True)
    print('Top Teams:\n')
    for o in outcomes[0:6]:
        print_team(o['team'])
        print('{}/10000 wins ({:.2f}%)\n'.format(o['wins'], 100 * o['wins'] / 10000))

random.seed('hero_league')
#setup_logs()
#make_records(heroes)

enemy_team = [
    get_hero_by_stats(heroes, 'F', 5),
    get_hero_by_stats(heroes, 'W', 6),
    get_hero_by_stats(heroes,'E', 3),
    get_hero_by_stats(heroes, 'E', 4),
    get_hero_by_stats(heroes, 'E', 6),
]

test_team_pve = [ 
    get_hero_by_stats(heroes, 'F', 5),
    get_hero_by_stats(heroes, 'F', 6),
    get_hero_by_stats(heroes,'E', 1),
    get_hero_by_stats(heroes, 'E', 5),
    get_hero_by_stats(heroes, 'E', 6),
]

test_team_a = [ #lsusr
    get_hero_by_stats(heroes, 'F', 4),
    get_hero_by_stats(heroes, 'W', 1),
    get_hero_by_stats(heroes,'W', 5),
    get_hero_by_stats(heroes, 'E', 5),
    get_hero_by_stats(heroes, 'V', 5),
]
test_team_b = [ #Measure
    get_hero_by_stats(heroes, 'F', 1),
    get_hero_by_stats(heroes, 'W', 4),
    get_hero_by_stats(heroes,'W', 6),
    get_hero_by_stats(heroes, 'E', 1),
    get_hero_by_stats(heroes, 'V', 5),
]
test_team_c = [ #abstractapplic
    get_hero_by_stats(heroes, 'F', 5),
    get_hero_by_stats(heroes, 'F', 6),
    get_hero_by_stats(heroes,'W', 6),
    get_hero_by_stats(heroes, 'E', 6),
    get_hero_by_stats(heroes, 'V', 5),
]
test_team_d = [ #Yonge
    get_hero_by_stats(heroes, 'W', 6),
    get_hero_by_stats(heroes, 'E', 1),
    get_hero_by_stats(heroes,'E', 5),
    get_hero_by_stats(heroes, 'E', 6),
    get_hero_by_stats(heroes, 'V', 5),
]
test_team_e = [ #GuySrinivasan
    get_hero_by_stats(heroes, 'F', 6),
    get_hero_by_stats(heroes, 'W', 5),
    get_hero_by_stats(heroes,'W', 6),
    get_hero_by_stats(heroes, 'E', 6),
    get_hero_by_stats(heroes, 'V', 5),
]
test_team_f = [ # Maxwell Peterson
    get_hero_by_stats(heroes, 'F', 6),
    get_hero_by_stats(heroes,'W', 6),
    get_hero_by_stats(heroes, 'E', 1),
    get_hero_by_stats(heroes, 'E', 6),
    get_hero_by_stats(heroes, 'V', 5),
]
test_team_g = [ # gjm
    get_hero_by_stats(heroes, 'F', 5),
    get_hero_by_stats(heroes, 'F', 6),
    get_hero_by_stats(heroes, 'E', 6),
    get_hero_by_stats(heroes, 'W', 6),
    get_hero_by_stats(heroes, 'V', 5),
]
test_team_h = [ # Alumium
    get_hero_by_stats(heroes, 'F', 6),
    get_hero_by_stats(heroes, 'W', 6),
    get_hero_by_stats(heroes, 'E', 1),
    get_hero_by_stats(heroes, 'E', 5),
    get_hero_by_stats(heroes, 'E', 6),
]
test_team_i = [ # Jemist
    get_hero_by_stats(heroes, 'F', 6),
    get_hero_by_stats(heroes, 'W', 6),
    get_hero_by_stats(heroes, 'E', 5),
    get_hero_by_stats(heroes, 'E', 6),
    get_hero_by_stats(heroes, 'V', 5),
]
test_team_j = [ # simon
    get_hero_by_stats(heroes, 'F', 2),
    get_hero_by_stats(heroes, 'F', 6),
    get_hero_by_stats(heroes, 'W', 1),
    get_hero_by_stats(heroes, 'W', 6),
    get_hero_by_stats(heroes, 'E', 6),
]

#res = team_matchup_evaluate(test_team_pve, enemy_team, runs=100000,verbose=True)
#res = random_matchup_evaluate(enemy_team, runs=100000,verbose=True)
#res = team_matchup_evaluate(test_team_i, test_team_k, runs=100000, verbose=True)

teams = [
    test_team_a,
    test_team_b,
    test_team_c,
    test_team_d,
    test_team_e,
    test_team_f,
    test_team_g,
    test_team_h,
    test_team_i,
    test_team_j
]
for x in range(0, len(teams)):
    for y in range(0, len(teams)):
        if( x >= y ):
            continue
        print('Testing Team {} vs Team {}:\n'.format(x, y ))
        random.seed('hero_league')
        res = team_matchup_evaluate(teams[x], teams[y], runs=100000,verbose=True)
