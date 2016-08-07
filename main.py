import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.garden.mapview import MapView, MapSource

class MapViewApp(App):
    def build(self):
        map = MapView()
        source = MapSource(url="http://localhost:8080/whistler_tiles/{z}/x{x}_y{y}.png",
        max_zoom=6)
        map.map_source = source
        return map

if __name__ == "__main__":
    MapViewApp().run()
