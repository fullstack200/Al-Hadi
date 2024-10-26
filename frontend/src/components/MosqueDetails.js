// src/components/MosqueDetails.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const MosqueDetails = () => {
    const { id } = useParams(); // Access the ID from the URL
    const [mosque, setMosque] = useState(null);

    useEffect(() => {
        const fetchMosqueDetails = async () => {
            const response = await fetch(`http://127.0.0.1:8000/nav/detailmosque/${id}`); // Use the ID in the API call
            const data = await response.json();
            setMosque(data);
        };

        fetchMosqueDetails();
    }, [id]);

    if (!mosque) return <div>Loading...</div>;

    return (
        <div>
            <h2>{mosque.mosque_name}</h2>
            <p>Address: {mosque.mosque_address}</p>
            <p>
                <a href={mosque.mosque_google_map_url} target="_blank" rel="noopener noreferrer">
                    View on Google Maps
                </a>
            </p>
            <h3>Prayer Timings:</h3>
            <ul>
                {Array.isArray(mosque.prayers) && mosque.prayers.length > 0 ? (
                    mosque.prayers.map((prayer) => (
                        <li key={prayer.prayer_id}>
                            {prayer.prayer_name}: {prayer.prayer_time ? prayer.prayer_time.toString() : 'N/A'} (Rakat: {prayer.prayer_rakat})
                        </li>
                    ))
                ) : (
                    <li>No prayer timings available.</li>
                )}
            </ul>
        </div>
    );
};

export default MosqueDetails;
