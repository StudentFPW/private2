import React from 'react';
import axios from 'axios';
import '../styles/Countries.css';

function Countries() {
    const [countries, setCountries] = React.useState([]);

    React.useEffect(() => {
        axios.get("https://restcountries.com/v3.1/all")
        .then((response) => setCountries(response.data))
        .catch((error) => console.log(error));
        }, []);

    return (
        <table>
            <thead>
                {countries.length === 0? <tr><td>Loading...</td></tr> : <tr><th>Name</th><th>Capital</th></tr> }
            </thead>

            <tbody>
                {countries.map(country => <tr><td>{country.name.common}</td><td>{country.capital}</td></tr>)}
            </tbody>
        </table>
    );
};
export default Countries;