from dataclasses import dataclass
import os


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:

    latitude = str(os.getenv("OW_LAT"))
    longitude = str(os.getenv("OW_LON"))

    return Coordinates(float(latitude), float(longitude)

)


if __name__ == "__main__":
    print(get_gps_coordinates())
