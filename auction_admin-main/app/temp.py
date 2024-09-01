import json
from firebase_admin import credentials, initialize_app, db

cred_obj = credentials.Certificate("auction-fin-firebase-adminsdk-pg996-ae9e731fd8.json")
app = initialize_app(cred_obj, {
    'databaseURL': 'https://auction-fin-default-rtdb.firebaseio.com/'
})

if input().strip()=="yes123":
    root_ref = db.reference()
    for i in range(1,11):
        team_ref = root_ref.child(f'team{i}')

        with open('team1.json', 'r') as f:
            data = json.load(f)

        team_ref.set(data)

    pointstemp = [
        {
            "team1": 100,
            "team2": 100,
            "team3": 85,
            "team4": 95,
            "team5": 90,
            "team6": 80,
            "team7": 80,
            "team8": 85,
            "team9": 95,
            "team10": 90
        }
    ]
    with open('points.json', 'w') as f:
        json.dump(pointstemp, f, indent=2)

