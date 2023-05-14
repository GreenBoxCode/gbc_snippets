import math


def get_distance_and_bearing(lat1, lon1, lat2, lon2):
    try:
        # Convert decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Calculate the distance between the two points in Km
        d = 6371.01 * math.acos(
            math.sin(lat1) * math.sin(lat2)
            + math.cos(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)
        )

        # Calculate the bearing (clockwise from north)
        bearing = math.atan2(
            math.sin(lon2 - lon1) * math.cos(lat2),
            math.cos(lat1) * math.sin(lat2)
            - math.sin(lat1) * math.cos(lat2) * math.cos(lon2 - lon1),
        )

        # Convert the bearing to degrees
        bearing = math.degrees(bearing)
        if bearing < 0:
            bearing += 360
        # Return the distance and bearing
        return d, bearing
    except Exception as e:
        print(f"An error has occured:/n{e}")


# Example Vancouver to Honolulu
# North Lat is positive
# West Lon is negative
lat1 = 49.1919444444
lon1 = -123.1751
lat2 = 21.3099
lon2 = -157.8581

gcr = get_distance_and_bearing(lat1, lon1, lat2, lon2)
print(gcr)
