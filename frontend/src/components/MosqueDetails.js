import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import MapComponent from './MapComponent';

const MosqueDetails = () => {
    const { id } = useParams();
    const [mosque, setMosque] = useState(null);
    const [userLocation, setUserLocation] = useState(null);
    const [loading, setLoading] = useState(true);

    // Fetch mosque details by ID
    useEffect(() => {
        const fetchMosqueDetails = async () => {
            try {
                const response = await fetch(`http://127.0.0.1:8000/nav/detailmosque/${id}`);
                if (!response.ok) {
                    throw new Error('Failed to fetch mosque details');
                }
                const data = await response.json();
                console.log("Fetched Mosque Data:", data);
                setMosque(data);
            } catch (error) {
                console.error("Error fetching mosque details:", error);
            } finally {
                setLoading(false);
            }
        };
        fetchMosqueDetails();
    }, [id]);

    // Get user's current location
    useEffect(() => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const location = {
                        lat: position.coords.latitude,
                        lng: position.coords.longitude,
                    };
                    setUserLocation(location);
                    console.log("User Location:", location);
                },
                (error) => {
                    console.error("Error getting user location:", error);
                }
            );
        } else {
            alert("Geolocation is not supported by this browser.");
        }
    }, []);

    // Loading state
    if (loading) {
        return <div>Loading mosque details...</div>;
    }

    // Define mosque location object
    const mosqueLocation = mosque?.latitude && mosque?.longitude
        ? { lat: mosque.latitude, lng: mosque.longitude }
        : null;

    // Render component
    return (
        <div>
            <h2>{mosque?.mosque_name}</h2>
            <p>Address: {mosque?.mosque_address}</p>
            <h3>Prayer Timings:</h3>
            <ul>
                {Array.isArray(mosque?.prayers) && mosque.prayers.length > 0 ? (
                    mosque.prayers.map((prayer) => (
                        <li key={prayer.prayer_id}>
                            {prayer.prayer_name}: {prayer.prayer_time ? prayer.prayer_time.toString() : 'N/A'} (Rakat: {prayer.prayer_rakat})
                        </li>
                    ))
                ) : (
                    <li>No prayer timings available.</li>
                )}
            </ul>

            {/* Render MapComponent if both user and mosque locations are available */}
            {userLocation && mosqueLocation ? (
                <MapComponent
                    userLocation={userLocation}
                    mosqueLocation={mosqueLocation}
                />
            ) : (
                <p>No map data available</p>
            )}
        </div>
    );
};

export default MosqueDetails;
