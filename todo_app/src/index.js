import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './AppStyles.css';
//import registerServiceWorker from './registerserviceWorker';

// reducers produce the state of your application
// the store is like the brain which keeps track of everything
// the reducer functions take an action and the current state and returns a copy of the current state plus new data
// actions are just javascript objects that are sent into the reducer
// higher order component takes a component and returns a new component

ReactDOM.render(<App />, document.getElementById('root'));



// Learn more about service workers: https://bit.ly/CRA-PWA
//serviceWorker.unregister();
