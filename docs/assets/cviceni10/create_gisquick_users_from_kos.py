#!/usr/bin/env python3

# Notes
# - delete users
# docker compose exec app gisquick dumpusers | jq '.[].username' > users
# modify users - keep gis1
# cat users | xargs -I {} docker compose exec -T app gisquick deleteuser {}
# TODO: delete data
# python3 ~/git/k155cvut/gis-1/docs/assets/cviceni10/create_gisquick_users_from_kos.py Predmet_B252_1551GIS.csv data/publish/users.json
# docker compose exec app gisquick loadusers /publish/users.json

import argparse
import csv
import json
import bcrypt
from unidecode import unidecode
from datetime import datetime

teachers = [
    ('Landa', 'Martin', 'landamar'),
    ('Mužík', 'František', 'muzikfra')
]

salt = bcrypt.gensalt()

def gen_user(firstname, lastname, username):
    password = unidecode(firstname.split(' ')[0].lower())
    print(username.lower(), password)
    return {
        "username": username.lower(),
        "email": f"{username.lower()}@cvut.cz",
        "password": bcrypt.hashpw(password.encode(), salt).decode(),
        "first_name": firstname,
        "last_name": lastname,
        "is_active": True,
        "is_superuser": False,
        "created_at": f"{datetime.now().isoformat()}Z",
        "confirmed_at": None,
        "last_login_at": None,
    }

def main(csv_input, json_output):
    users = []
    with open(csv_input) as csvfile:
        userreader = csv.reader(csvfile, delimiter=';')
        next(userreader) # skip initial row
        for row in userreader:
            if len(row) < 3:
                continue
            users.append(gen_user(row[0], row[1], row[3]))

    for ln, fn, un in teachers:
        users.append(gen_user(fn, ln, un))
                         
    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=4)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Create Gisquick users from KOS-generated CSV file')
    parser.add_argument('csv_input')
    parser.add_argument('json_output')

    args = parser.parse_args()
    main(args.csv_input, args.json_output)
    
