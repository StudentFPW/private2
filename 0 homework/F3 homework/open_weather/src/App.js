import React from 'react';

import Geocoding from '../src/components/Geocoding';

import '../src/styles/App.css';

class App extends React.Component {
  render() {
    return (
      <React.Fragment>
        <Geocoding />
      </React.Fragment>
    );
  }
}

export default App;