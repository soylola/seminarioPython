# Práctica 2, ejercicio 10

def print_final_table(rounds):
    chef_names = rounds[0]["scores"].keys()
    statistics = {}
    round_number = 1

    for name in chef_names:
        statistics[name] = {"current_round":0, "final_points":0, "rounds_won":0, "best_round":0}


    print("- "*60)
    

    for round in rounds: # PER ROUND
        max_points = 0
        
        for chef in chef_names:
            round_points = 0
            round_points += sum(round["scores"][chef].values()) # round_points: judge1 + judge2 + judge3
            statistics[chef]["final_points"] += round_points
            statistics[chef]["current_round"] = round_points

            if (round_points > max_points):
                max_points = round_points
                round_winner = chef


            if  statistics[chef]["current_round"]  > statistics[chef]["best_round"]:
                statistics[chef]["best_round"] = statistics[chef]["current_round"]


        statistics[round_winner]["rounds_won"] += 1

        print(f"Round {round_number} - {rounds[round_number-1]["theme"]}")
        print(f"Winner: {round_winner} ({max_points} pts)")
        
        print("Cocinero       Puntaje       Rondas Ganadas       Mejor Ronda       Promedio")
        print("- "*39)

        for chef in chef_names:
            print(f"{chef:<{15}} {statistics[chef]["current_round"]:<{15}} {statistics[chef]["rounds_won"]:<{20}} {statistics[chef]["best_round"]:<{15}} {((statistics[chef]["final_points"])/round_number):.1f}")

        round_number = round_number + 1
        print("- "*39)
        


rounds = [
    {
        'theme': 'Entrada',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 7,
            'judge_3': 9},
            'Mateo': {'judge_1': 7, 'judge_2': 8,
            'judge_3': 7},
            'Camila': {'judge_1': 9, 'judge_2': 9,
            'judge_3': 8},
            'Santiago': {'judge_1': 6, 'judge_2': 7,
            'judge_3': 6},
            'Lucía': {'judge_1': 8, 'judge_2': 8,
            'judge_3': 8},
        }
    },
    {
        'theme': 'Plato principal',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 9,
            'judge_3': 8},
            'Mateo': {'judge_1': 8, 'judge_2': 7,
            'judge_3': 9},
            'Camila': {'judge_1': 7, 'judge_2': 6,
            'judge_3': 7},
            'Santiago': {'judge_1': 9, 'judge_2': 8,
            'judge_3': 8},
            'Lucía': {'judge_1': 7, 'judge_2': 8,
            'judge_3': 7},
        }
    },
    {
        'theme': 'Postre',
        'scores': {
            'Valentina': {'judge_1': 7, 'judge_2': 8,
            'judge_3': 7},
            'Mateo': {'judge_1': 9, 'judge_2': 9,
            'judge_3': 8},
            'Camila': {'judge_1': 8, 'judge_2': 7,
            'judge_3': 9},
            'Santiago': {'judge_1': 7, 'judge_2': 7,
            'judge_3': 6},
            'Lucía': {'judge_1': 9, 'judge_2': 9,
            'judge_3': 9},
        }
    },
    {
        'theme': 'Cocina internacional',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 9,
            'judge_3': 9},
            'Mateo': {'judge_1': 7, 'judge_2': 6,
            'judge_3': 7},
            'Camila': {'judge_1': 9, 'judge_2': 8,
            'judge_3': 8},
            'Santiago': {'judge_1': 8, 'judge_2': 9,
            'judge_3': 7},
            'Lucía': {'judge_1': 7, 'judge_2': 7,
            'judge_3': 8},
        }
    },
    {
        'theme': 'Final libre',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 8,
            'judge_3': 9},
            'Mateo': {'judge_1': 8, 'judge_2': 9,
            'judge_3': 8},
            'Camila': {'judge_1': 7, 'judge_2': 7,
            'judge_3': 7},
            'Santiago': {'judge_1': 9, 'judge_2': 9,
            'judge_3': 9},
            'Lucía': {'judge_1': 8, 'judge_2': 8,
            'judge_3': 7},
        }
    }
]