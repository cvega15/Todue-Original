import React from 'react';
import Header from './components/Header';
import Footer from './components/footer';
import TasksArea from './components/TasksArea';
import './AppStyles.css';

class App extends React.Component {
    render() {
       
        return (
            <div>
                <Header />
                <TasksArea />
                <Footer />
            </div>
        ) 
    }
}

export default App;
