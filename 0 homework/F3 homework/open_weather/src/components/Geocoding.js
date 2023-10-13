import React from 'react';
import axios from 'axios';

import Daily from './Daily';

class Geocoding extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            lat: 0,
            lon: 0,
            token: "ac1376893cc2a3d9a1ebe7c8d00e82c0",
            city: "Riga",
            pagination: 1,
        };
    }

    componentDidMount() {
        this.updateItems();
    }

    updateItems() {
        axios.get(`http://api.openweathermap.org/geo/1.0/direct?q=${this.state.city}&limit=${this.state.pagination}&appid=${this.state.token}`)
            .then((response) => {
                this.setState({
                    lat: response.data[0].lat,
                    lon: response.data[0].lon,
                })
            })
            .catch((err) => { console.log(err, "Geocoding") })
    };

    render() {
        return (
            <React.Fragment>
                <Daily
                    lat={this.state.lat}
                    lon={this.state.lon}
                    token={this.state.token}
                    city={this.state.city}
                />
            </React.Fragment>
        )
    };
}

export default Geocoding;