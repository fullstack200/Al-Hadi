// src/components/MosqueList.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './MosqueList.css';

const MosqueList = () => {
    const [mosques, setMosques] = useState([]);
    const [searchTerm, setSearchTerm] = useState('Masjid E '); // Set initial search term

    useEffect(() => {
        const fetchMosques = async () => {
            const response = await fetch('http://127.0.0.1:8000/nav/listmosque'); // Use your API endpoint
            const data = await response.json();
            setMosques(data);
        };

        fetchMosques();
    }, []);

    // Filter mosques based on the search term
    const filteredMosques = mosques.filter(mosque =>
        mosque.mosque_name.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <div>
            <h2>List of Mosques</h2>
            <input
                type="text"
                placeholder="Search by mosque name..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)} // Update searchTerm on input change
                
            />
            <ul>
                {filteredMosques.map((mosque) => (
                    <li key={mosque.mosque_id}>
                        <Link className="mosque-link" to={`/mosque/${mosque.mosque_id}`}>
                            {mosque.mosque_name}
                        </Link>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default MosqueList;
