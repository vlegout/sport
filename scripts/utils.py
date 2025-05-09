import math

from typing import List, Tuple

from data import TracePoint


def get_lat_lon(points: List[TracePoint]) -> Tuple[float, float]:
    x = y = z = 0.0

    if len(points) == 0:
        return 0.0, 0.0

    for point in points:
        lon = math.radians(float(point.lon))
        lat = math.radians(float(point.lat))

        x += math.cos(lon) * math.cos(lat)
        y += math.cos(lon) * math.sin(lat)
        z += math.sin(lon)

    total = len(points)

    x = x / total
    y = y / total
    z = z / total

    lon = math.atan2(y, x)
    lat = math.atan2(z, math.sqrt(x * x + y * y))

    lat, lon = map(math.degrees, (lon, lat))

    return lat, lon


def get_delta_lat_lon(lat: float, max_distance: float) -> Tuple[float, float]:
    earth_radius = 6371000
    delta_lat = max_distance / earth_radius * (180 / math.pi)
    delta_lon = (
        max_distance / (earth_radius * math.cos(math.radians(lat))) * (180 / math.pi)
    )

    return (delta_lat, delta_lon)
