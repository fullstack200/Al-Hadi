// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import MosqueListPage from './pages/MosqueListPage';
import MosqueDetailsPage from './pages/MosqueDetailsPage';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<MosqueListPage />} />
                <Route path="/mosque/:id" element={<MosqueDetailsPage />} />
            </Routes>
        </Router>
    );
}

export default App;
