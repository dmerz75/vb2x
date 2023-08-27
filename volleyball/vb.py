#!/usr/bin/env python

import os
import sys
import random
import argparse
import logging

def print_everything(courts, players, teams, excluded_players):

    print(f"number of players: {len(players)}")
    print(f"number of courts: {courts}")
    print(f"the teams are: {teams}")
    print(f"sitting out: {excluded_players}")

    # msg = "-start-\n"
    msg = ""

    for x in range(0, len(teams)-1, 2):
        team1 = teams[x]
        team2 = teams[x+1]
        msg += f"match: {team1[0]}--{team1[1]}  vs  {team2[0]}--{team2[1]}\n"

    msg += f"sitting this round:  {excluded_players}\n"
    # msg += "-end-\n"

    with(open("matchups.txt", "a+")) as fp:
        fp.write(msg)

    return msg

def list_contains(List1, List2):
    set1 = set(List1)
    set2 = set(List2)
    if set1.intersection(set2):
        return True
    else:
        return False


def shuffle_up(players, n_courts, excluded=[]):
    print("shuffling..")
    random.shuffle(players)

    print(players)
    print(excluded)

    num_players_needed = n_courts * 4

    while(list_contains(players[-(len(excluded)):], excluded)):
        logging.debug(f" ---NO--- {players}")
        logging.debug("re-shuffling")
        random.shuffle(players)

    included = players[:num_players_needed]
    excluded = list(set(players) ^ set(included))

    print(f"included: {included}")
    print(f"excluded: {excluded}")

    # if excluded:
    #     excluded = players[-len(excluded):]
    # print(players)
    # print(excluded)

    # for r in excluded:
    #     players.pop(r)

    final_players = players.copy()
    return final_players, excluded

def main(num_players, excluded):
    print("vb main..")
    print(f"making courts for {num_players}")
    print(f"non-exclusions: {excluded}")
    print(type(excluded))
    excluded = excluded.strip()
    excluded = excluded.replace(" ", ",")
    if excluded == "":
        excluded = []
    elif "," in excluded:
        excluded = [int(x) for x in excluded.split(",")]
    elif " " in excluded:
        excluded = [int(x) for x in excluded.split(" ")]
    else:
        excluded = []
    print(type(excluded), excluded)
    # if exclude
    # return

    players = [n+1 for n in range(num_players)]
    ordered_players = players.copy()
    courts = int(len(players) / 4)
    n_teams = courts * 2
    # n_players_included = n_teams * 2

    if courts * 4 == num_players:
        excluded = []

    shuffled_players, new_excluded = shuffle_up(players, courts, excluded)
    recently_excluded = excluded + new_excluded

    teams = [(shuffled_players[n*2], shuffled_players[n*2+1]) for n in range(n_teams)]

    print(f"ordered: {ordered_players}")
    print(f"shuffled: {shuffled_players}")
    print(f"newly excluded: {new_excluded}")
    print(f"shuffled: {shuffled_players}")
    print(f"recently_excluded: {recently_excluded}")
    message = print_everything(courts, shuffled_players, teams, new_excluded)

    print("results:")
    print(type(new_excluded), type(message))
    print(f"new_excluded: {new_excluded}")
    print(f"message: {message}")
    return new_excluded, message


if __name__ == "__main__":
    # excluded = []
    # num_players = 11

    # for i in range(3):
    #     excluded = main(num_players, excluded)
    #     print(f"end of round--excluded: {excluded}")

    parser = argparse.ArgumentParser(description='Process player parameters:')
    parser.add_argument('-n', "--number", type=int,
                        help='number of players')
    parser.add_argument('-e', "--excluded", type=str,
                        help='sum the integers (default: find the max)')
    args = parser.parse_args()

    # if args.excluded:
    #     excluded = [int(x) for x in args.excluded.split(',')]
    # else:
    #     excluded = []

    num_players = args.number
    excluded, message = main(num_players, args.excluded)
    # print("latest excluded:", excluded)
