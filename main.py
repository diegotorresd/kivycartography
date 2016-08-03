from kivy.garden.mapview import MapView
from kivy.app import App

class MapViewApp(App):
    def build(self):
        mapView = MapView(zoom=12, lat=50.6394, lon=3.057)
        return mapView

if __name__ == '___main___':
    MapViewApp().run()
