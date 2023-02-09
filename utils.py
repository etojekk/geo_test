from rosreestr2coord import Area
import geopandas as gpd
from shapely.geometry import Polygon
import folium


MAP_OUTFILE_PATH = './templates/geo.html'

def make_map(area_id: str = None):
    area_is_valid = True
    area = Area(area_id, with_proxy=True)
    coords = area.get_coord()
    while len(coords) == 1:
        coords = coords[0]
    if len(coords) == 2 and isinstance(coords[0]) == float:
        coords = [coords]
    if not coords:
        print('area is invalid')
        area_is_valid = False
        return area_is_valid
    center = (area.get_center_xy()[0][0][0])[::-1]
    polygon_geom = Polygon(coords)
    polygon = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom])
    area_map = folium.Map(location=center, zoom_start=18, tiles='OpenStreetMap')
    folium.GeoJson(polygon).add_to(area_map)
    folium.LatLngPopup().add_to(area_map)

    area_map.save(outfile=MAP_OUTFILE_PATH)

    return area_is_valid
