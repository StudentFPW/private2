import React from 'react';
import axios from 'axios';

export default function Daily(props) {
    const state = {
        cloud_cover: [],
        humidity: [],
        precipitation: [],
        temperature: [],
        pressure: [],
        wind: [],
        lang: "",
        date: (new Date().toISOString() + 4).slice(0, 10),
        lat: props.lat,
        lon: props.lon,
        token: props.token,
    };

    UpdateItems(state.lat, state.lon, state.token);

    return (
        <ul>
            <li>{state.lat}</li>
            <li>{state.lon}</li>
            <li>{state.token}</li>
        </ul>
    );
}

function UpdateItems(lat, lon, token, lang = "ru") {
    axios.get(`https://api.openweathermap.org/data/3.0/onecall?lat=${lat}&lon=${lon}&appid=${token}&lang=${lang}`)
        .then((response) => {
            return (
                console.log(response)
            )
        })
        .catch((err) => {
            return (
                console.log(err, "Daily")
            )
        })
};