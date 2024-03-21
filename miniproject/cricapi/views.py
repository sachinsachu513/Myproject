from django.shortcuts import render

# Create your views here.
import requests
import json
from tabulate import tabulate
import datetime
daten=datetime.datetime.now().date()
timen=datetime.datetime.now().time()
def fetch_cricket_scores(request):
    # dic={"date":date,"time":time}

    url = 'https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent'
    headers = {
        'X-RapidAPI-Host': 'cricbuzz-cricket.p.rapidapi.com',
        "X-RapidAPI-Key": "7b9c7866a1msh85417a71983e0b1p1467e8jsn99de1d9a89dd",
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    matches_data = []

    for match in data['typeMatches'][0]['seriesMatches'][0]['seriesAdWrapper']['matches']:
        table = [
            [f" {match['matchInfo']['matchDesc']} , {match['matchInfo']['team1']['teamName']} vs {match['matchInfo']['team2']['teamName']}"],
            ["Series Name", match['matchInfo']['seriesName']],
            ["Match Format", match['matchInfo']['matchFormat']],
            ["Result", match['matchInfo']['status']],
            [f"{match['matchInfo']['team1']['teamName']} Score", f"{match['matchScore']['team1Score']['inngs1']['runs']}/{match['matchScore']['team1Score']['inngs1']['wickets']} in {match['matchScore']['team1Score']['inngs1']['overs']} overs"],
            [f"{match['matchInfo']['team2']['teamName']} Score", f"{match['matchScore']['team2Score']['inngs1']['runs']}/{match['matchScore']['team2Score']['inngs1']['wickets']} in {match['matchScore']['team2Score']['inngs1']['overs']} overs"],
        ]
        matches_data.append(tabulate(table, tablefmt="html"))


    return render(request, "cricket/completed.html", context={"cricket_scores": matches_data,"date":daten,"time":timen})


def fetch_upcoming_matches(request):
    dates = datetime.datetime.now().date()
    times = datetime.datetime.now().time()

    url = "https://cricbuzz-cricket.p.rapidapi.com/schedule/v1/international"

    headers = {
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
        "X-RapidAPI-Key": "dc717f31b7msh42c852b865998afp19db81jsnd5569dc9e85d"  # Replace with your RapidAPI key
    }

    response = requests.get(url, headers=headers)
    upcoming_matches = []

    if response.status_code == 200:
        try:
            data = response.json()
            match_schedules = data.get('matchScheduleMap', [])

            for schedule in match_schedules:
                if 'scheduleAdWrapper' in schedule:
                    date = schedule['scheduleAdWrapper']['date']
                    matches = schedule['scheduleAdWrapper']['matchScheduleList']

                    for match_info in matches:
                        for match in match_info['matchInfo']:
                            description = match['matchDesc']
                            team1 = match['team1']['teamName']
                            team2 = match['team2']['teamName']
                            match_data = {
                                'Date': date,
                                'Description': description,
                                'Teams': f"{team1} vs {team2}"
                            }
                            upcoming_matches.append(match_data)
                else:
                    print("No match schedule found for this entry.")

        except json.JSONDecodeError as e:
            print("Error parsing JSON:", e)
        except KeyError as e:
            print("Key error:", e)
    else:
        print("Failed to fetch cricket scores. Status code:", response.status_code)


    return render(request, "cricket/upcoming.html", context={"upcoming_matches": upcoming_matches,"dates":dates,"times":times})
