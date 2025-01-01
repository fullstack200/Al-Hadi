import React, { useEffect, useState, useRef } from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

// Declare google globally to avoid ESLint warning
/* global google */

// Define the map container style
const mapContainerStyle = {
    height: "400px",
    width: "100%",
};

const MapComponent = ({ userLocation, mosqueLocation }) => {
    const [map, setMap] = useState(null);
    const mapRef = useRef(null);

    // Center the map to either the user's location or the mosque location
    const center = userLocation || mosqueLocation || { lat: 0, lng: 0 };
    const zoom = 15;

    // When the map is loaded, we can add the markers
    const handleMapLoad = (map) => {
        setMap(map);
        addMarkers(map);
    };

    const addMarkers = (map) => {
        // Clear any existing markers
        if (map) {
            // Add marker for user location
            if (userLocation) {
                new google.maps.Marker({
                    position: userLocation,
                    map: map,
                    title: "Your Location",
                });
            }

            // Add marker for mosque location
            if (mosqueLocation) {
                new google.maps.Marker({
                    position: mosqueLocation,
                    map: map,
                    title: "Mosque Location",
                });
            }
        }
    };

    return (
        <LoadScript googleMapsApiKey="API_KEY">
            <GoogleMap
                id="map"
                mapContainerStyle={mapContainerStyle}
                zoom={zoom}
                center={center}
                onLoad={handleMapLoad}
            >
                {/* Map will be rendered here */}
            </GoogleMap>
        </LoadScript>
    );
};

export default MapComponent;
