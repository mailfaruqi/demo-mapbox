import Map, { Marker } from "react-map-gl";

import "../mapbox-gl.css";

const mapboxAccessToken = import.meta.env.VITE_MAPBOX_ACCESS_TOKEN;

export function MapExampleRoute() {
  return (
    <div>
      <MapboxMap
        coordinate={{
          latitude: -6.1753924,
          longitude: 106.8271528,
          zoom: 14,
        }}
      />

      {/* <MapboxMapMarkers
        map={{
          latitude: -6.1753924,
          longitude: 106.8271528,
          zoom: 14,
        }}
        places={[
          { latitude: -6.1753924, longitude: 106.8271528 },
          { latitude: -6.1763924, longitude: 106.9271528 },
          { latitude: -6.1773924, longitude: 106.8371528 },
        ]}
      /> */}
    </div>
  );
}

interface MapboxMapProps {
  coordinate: {
    latitude: number;
    longitude: number;
    zoom: number;
  };
}

export function MapboxMap({
  coordinate = {
    latitude: -6.1753924,
    longitude: 106.8271528,
    zoom: 14,
  },
}: MapboxMapProps) {
  return (
    <Map
      mapboxAccessToken={mapboxAccessToken}
      initialViewState={coordinate}
      style={{ width: 600, height: 400 }}
      mapStyle="mapbox://styles/mapbox/streets-v9"
    >
      <Marker
        longitude={coordinate.longitude}
        latitude={coordinate.latitude}
        anchor="bottom"
      >
        <img src="/images/pin.png" width={50} height={20} />
      </Marker>
    </Map>
  );
}
