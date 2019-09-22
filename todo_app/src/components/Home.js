import React from 'react';
import Header from './Header';
import TasksArea from './TasksArea';
import Modal from './Modal';

class Home extends React.Component {

    render(){
       
        return (
            <div className="home">
                <Modal />
                <Header title="users tasks" />
                <TasksArea /> 
            </div>
        );
    };
};

export default Home;
