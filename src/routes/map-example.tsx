import Map, { Marker } from "react-map-gl";

import "../mapbox-gl.css";

const mapboxAccessToken = import.meta.env.VITE_MAPBOX_ACCESS_TOKEN;

export function MapExampleRoute() {
  const places = [
    { latitude: -6.1753924, longitude: 106.8271528 },
    { latitude: -6.1762405, longitude: 106.82725 },
    { latitude: -6.1741286, longitude: 106.8284033 },
  ];

  return (
    <div>
      <MapboxMap
        coordinate={{
          latitude: -6.1753924,
          longitude: 106.8271528,
          zoom: 14,
        }}
        places={places}
      />
    </div>
  );
}

interface MapboxMapProps {
  coordinate: {
    latitude: number;
    longitude: number;
    zoom: number;
  };
  places: { latitude: number; longitude: number }[];
}

export function MapboxMap({
  coordinate = {
    latitude: -6.1753924,
    longitude: 106.8271528,
    zoom: 14,
  },
  places,
}: MapboxMapProps) {
  return (
    <Map
      mapboxAccessToken={mapboxAccessToken}
      initialViewState={coordinate}
      style={{ width: 600, height: 400 }}
      mapStyle="mapbox://styles/mapbox/streets-v9"
    >
      {places.map((place, index) => (
        <Marker
          key={index}
          longitude={place.longitude}
          latitude={place.latitude}
          anchor="bottom"
        >
          <img
            src="/images/pin.png"
            width={50}
            height={20}
            alt={`Marker ${index}`}
          />
        </Marker>
      ))}
    </Map>
  );
}
