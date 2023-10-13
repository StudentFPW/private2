import React from'react';
import '../styles/App.css';

import Header from './Header';
import MainCountries from './MainCountries';

class App extends React.Component {
    render() {
        return (
            <React.Fragment>
                <Header/>
                <MainCountries/>
            </React.Fragment>
        );
    };
};

export default App;