import React from 'react';

import App1 from './App1';
import App2 from './App2';
import App3 from './App3';
import App4 from './App4';
import App5 from './App5';
import MyClassComponent1 from './MyClassComponent1';

class App extends React.Component {
  render() {
    return (
      <React.Fragment>
        <App1 />
        <App2 />
        <App3 />
        <App4 />
        <App5 />
        <MyClassComponent1 />
      </React.Fragment>
    )
  }
}

export default App;