import json
from typing import NamedTuple
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    with open("data.json", "r") as file:
        data = json.load(file)

    latitude = data['coordinates']['latitude']
    longitude = data['coordinates']['longitude']

    return Coordinates(latitude, longitude)


if __name__ == "__main__":
    print(get_gps_coordinates())
