"""Look up a city name for each office and save it.

Nominatim allows about one request per second. The result is written to
output/geocode_cache.csv every 25 offices, so a rerun continues where it stopped.
"""

import time
from pathlib import Path

import pandas as pd
from geopy.exc import GeocoderServiceError, GeocoderTimedOut, GeocoderUnavailable
from geopy.geocoders import Nominatim

DATA_PATH = Path("data/Dataset1_Arizona_Dental_Offices.csv")
CACHE_PATH = Path("output/geocode_cache.csv")
CITY_FIELDS = ("city", "town", "village", "hamlet", "municipality")

CACHE_PATH.parent.mkdir(exist_ok=True)

offices = pd.read_csv(DATA_PATH)
offices["Office_Id"] = offices.index

if CACHE_PATH.exists():
    cache = pd.read_csv(CACHE_PATH)
else:
    cache = pd.DataFrame(columns=["Office_Id", "Latitude", "Longitude", "City_Raw"])

done_ids = set(cache["Office_Id"].astype(int))
remaining = offices.loc[~offices["Office_Id"].isin(done_ids)]
print(f"cached {len(done_ids)} remaining {len(remaining)}", flush=True)

geolocator = Nominatim(user_agent="oncap-arizona-dental-case-study")
new_rows = []


def city_name(location):
    if location is None:
        return None
    address = location.raw.get("address", {})
    for field in CITY_FIELDS:
        if address.get(field):
            return address[field]
    return None


def lookup(lat, lon):
    last_error = None
    for attempt in range(4):
        try:
            location = geolocator.reverse(
                (lat, lon),
                language="en",
                addressdetails=True,
                timeout=20,
            )
            return city_name(location)
        except (GeocoderTimedOut, GeocoderServiceError, GeocoderUnavailable) as error:
            last_error = error
            time.sleep(5 * (attempt + 1))
    print(f"gave up after retries: {last_error}", flush=True)
    return None


for n, row in enumerate(remaining.itertuples(index=False), start=1):
    city = lookup(row.Latitude, row.Longitude)
    new_rows.append(
        {
            "Office_Id": int(row.Office_Id),
            "Latitude": row.Latitude,
            "Longitude": row.Longitude,
            "City_Raw": city,
        }
    )
    if n % 25 == 0:
        pd.concat([cache, pd.DataFrame(new_rows)], ignore_index=True).to_csv(CACHE_PATH, index=False)
        print(f"saved {len(done_ids) + n}", flush=True)
    time.sleep(1.1)

if new_rows:
    pd.concat([cache, pd.DataFrame(new_rows)], ignore_index=True).to_csv(CACHE_PATH, index=False)

print(f"finished {len(done_ids) + len(new_rows)}", flush=True)
