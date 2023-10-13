import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';

import { Provider } from 'react-redux';
import { legacy_createStore as createStore, applyMiddleware, compose } from 'redux';

import ReduxApp from './App-redux';
import reducers from './reducers';
import { logging } from './middlewares/logging';

const store = createStore(
    reducers,
    compose(applyMiddleware(logging),
        window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()));

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <Provider store={store}>
        <ReduxApp />
    </Provider>
);

reportWebVitals();
