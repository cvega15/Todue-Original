import React from 'react';
import Header from './Header';
import TasksArea from './TasksArea';
import Modal from './Modal';
import Navbar from './Navbar';

class Home extends React.Component {

    render(){
       
        return (
            <div className="home">
                <Modal />
                <Header title="users tasks" button_text="add task"/>
                <TasksArea /> 
                <Navbar />
            </div>
        );
    };
};

export default Home;
