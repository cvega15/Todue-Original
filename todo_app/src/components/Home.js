import React from 'react';
import Header from './Header';
import TasksArea from './TasksArea';

class Home extends React.Component {

    render(){
       
        return (
            <div className="home">
                <Header />
                <TasksArea />
            </div>
        );
    };
};

export default Home;
