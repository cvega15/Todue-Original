import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './AppStyles.css';
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import rootReducer from './reducers/rootReducer';
//import registerServiceWorker from './registerserviceWorker';

const store = createStore(rootReducer);

ReactDOM.render(<Provider store={store}><App /></Provider>, document.getElementById('root'));

// Learn more about service workers: https://bit.ly/CRA-PWA
//serviceWorker.unregister();
