import React from 'react';
import { Route } from 'react-router-dom';
import { Link, Switch } from 'react-router-dom/cjs/react-router-dom.min';

import '../styles/App.css';

import Home from './Home';
import Api from './Api';
import Test from './Test';
import Page from './Page';

function App() {
  return (
    <React.Fragment>

      <nav>
        <Link to="/home">Home</Link><br />
        <Link to="/api">Api</Link><br />
        <Link to="/test">Test</Link>
      </nav>

      <Switch>

        <Route path='/home'>
          <Home />
        </Route>

        <Route path='/api'>
          <Api />
        </Route>

        <Route path='/test'>
          <Test />
        </Route>

        <Route path='/page/:id'>
          <Page />
        </Route>

        <Route path=''>
          <h1>Hello world !</h1>
        </Route>

      </Switch>

    </React.Fragment>
  );
}

export default App;
