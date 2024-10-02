import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  state = {
    mosque: null // Change from array to a single mosque object
  };

  componentDidMount() {
    this.getMosque();
  }

  getMosque() {
    axios
      .get('http://127.0.0.1:8000/nav/mosque01/')
      .then(res => {
        console.log("API Data:", res.data);
        this.setState({ mosque: res.data });
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
        <p>{mosque.mosque_address}</p>

        <h2>Prayers</h2>
        <ul>
          {mosque.prayers.map(prayer => (
            <li key={prayer.prayer_id}>
              <strong>{prayer.prayer_name}</strong> - Rakat: {prayer.prayer_rakat}, 
              Azaan Time: {prayer.azaan_time}, Prayer Time: {prayer.prayer_time}
              Prayer Valid Till: {prayer.prayer_valid_till}
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

export default App;
