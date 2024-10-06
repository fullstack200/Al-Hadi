import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  state = {
    mosque: null, // Expect a single mosque object
  };

  componentDidMount() {
    this.getMosque(); // Fetch mosque on component mount
  }

  getMosque() {
    axios
      .get('http://127.0.0.1:8000/nav/detailmosque/mosque02') // Adjust based on API
      .then(res => {
        console.log("API Data:", res.data); // Inspect API response
        this.setState({ mosque: res.data }); // Set mosque as an object
      })
      .catch(err => {
        console.log(err);
      });
  }

  render() {
    const { mosque } = this.state;

    // Check if the mosque data is available
    if (!mosque) {
      return <div>Loading...</div>;
    }

    return (
      <div>
        <h1>{mosque.mosque_name}</h1>
        <p>Address: {mosque.mosque_address}</p>
        <p>Google Map: <a href={mosque.mosque_google_map_url} target="_blank" rel="noopener noreferrer">View Map</a></p>

        <h2>Prayers</h2>
        <ul>
          {mosque.prayers.length > 0 ? (
            mosque.prayers.map(prayer => (
              <li key={prayer.prayer_id}>
                <strong>{prayer.prayer_name}</strong> - Rakat: {prayer.prayer_rakat}, 
                Azaan Time: {prayer.azaan_time}, Prayer Time: {prayer.prayer_time}
              </li>
            ))
          ) : (
            <li>No prayers available for this mosque.</li>
          )}
        </ul>
      </div>
    );
  }
}

export default App;
