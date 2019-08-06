import React from 'react';
import TasksArea from './components/TasksArea';
import AddTask from './components/AddTask';
import Navbar from './components/Navbar';
import './AppStyles.css';

class App extends React.Component {

    constructor(){
        super();
        this.state = {
            tasks: [
                { name: 'feed fish', date: '10/23/2019', id: 1},
                { name: 'take out trash', date: '12/06/2019', id: 2},
                { name: 'get lit', date: '13/07/2019', id: 3},
            ]
        };
    };

    render(){
       
        return (
            <div className="everything">
                <Navbar />  
                <AddTask />
                <TasksArea tasks={this.state.tasks}/>
            </div>
        );
    };
};

export default App;
