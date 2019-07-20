import React from 'react';
import Task from './components/Task';
import Header from './components/Header';
import Footer from './components/footer';
import './AppStyles.css';

function App(){
    return(
        <div>
            <Header />
            <Task />
            <Task />
            <Footer />
        </div>
    )
};

export default App;
