import os
from typing import Dict
from graphql_query import Operation, Query
import json
import requests

from space_x.create_database import session, Launch, Rocket


def get_json_data(query: Operation, url: str) -> Dict:
    results = {}
    response = requests.post(url, json={'query': query.render()}).text
    results.update(json.loads(response)['data'])
    return results


def add_data_to_db(data: Dict) -> None:
    with session() as conn:
        for key, values in data.items():
            for value in values:
                if key == 'launches':
                    conn.add(Launch(**value))
                elif key == 'rockets':
                    conn.add(Rocket(**value))
            print(f'[Загрузка] {key} завершена')
            conn.commit()


if __name__ == '__main__':
    URL = 'https://spacex-production.up.railway.app'
    ROCKETS = Query(
        name='rockets',
        fields=['id', 'name', 'description', 'wikipedia']
    )
    LAUNCHES = Query(
        name='launches',
        fields=['id', 'details', 'mission_name']
    )

    operation = Operation(type='query', queries=[ROCKETS, LAUNCHES])

    data = get_json_data(operation, URL)
    add_data_to_db(data)
