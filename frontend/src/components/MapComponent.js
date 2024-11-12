import React, { useState, useEffect } from 'react';
import { GoogleMap, LoadScript, Marker, DirectionsService, DirectionsRenderer } from '@react-google-maps/api';

const MapComponent = ({ userLocation, mosqueLocation }) => {
    // State for directions result
    const [directionsResponse, setDirectionsResponse] = useState(null);

    useEffect(() => {
        if (userLocation && mosqueLocation) {
            console.log("User Location:", userLocation);
            console.log("Mosque Location:", mosqueLocation);
        }
    }, [userLocation, mosqueLocation]);

    const directionsCallback = (response) => {
        if (response !== null && response.status === 'OK') {
            setDirectionsResponse(response);
        } else {
            console.error("Error fetching directions:", response?.status);
        }
    };

    // Render a loading message if locations are not yet available
    if (!userLocation || !mosqueLocation) {
        return <div>Loading map...</div>;
    }

    return (
        <LoadScript googleMapsApiKey={'AIzaSyDDk6ejdl7sm8zOvM49cZexfcc3RbANcz4'}>
            <GoogleMap
                center={userLocation}
                zoom={13}
                mapContainerStyle={{ height: '400px', width: '100%' }}
            >
                {/* User and Mosque markers */}
                <Marker position={userLocation} label="You" />
                <Marker position={mosqueLocation} label="Mosque" />

                {/* DirectionsService to calculate route */}
                <DirectionsService
                    options={{
                        origin: userLocation,
                        destination: mosqueLocation,
                        travelMode: 'DRIVING'
                    }}
                    callback={directionsCallback}
                />

                {/* Render the route */}
                {directionsResponse && (
                    <DirectionsRenderer
                        options={{
                            directions: directionsResponse
                        }}
                    />
                )}
            </GoogleMap>
        </LoadScript>
    );
};

export default MapComponent;
