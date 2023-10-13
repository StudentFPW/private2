import React from 'react';
import { useLocation, useParams } from 'react-router-dom/cjs/react-router-dom.min';

export default function Page(props) {

    const params = useParams();

    const location = useLocation();
    const search = location.search;
    const query = new URLSearchParams(search);

    return (
        <React.Fragment>
            <ul>
                <li>{location.search}</li>
                <li>Page = {params.id} with filter {query.get('sorting')}</li>
            </ul>
        </React.Fragment>
    )
}
