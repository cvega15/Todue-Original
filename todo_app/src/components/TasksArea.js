import React from 'react';
import Task from './Task';
import { TasksContext } from '../contexts/TasksContext';

class App extends React.Component{

    static contextType = TasksContext;

    constructor(props){
        super(props);
        this.state = {
            now: new Date()
        };
    };

    componentDidMount(){
        var interval_id = setInterval(()=>this.updateTime(), 1000);
        this.interval_id = interval_id
    };

    componentWillUnmount(){
        clearInterval(this.interval_id);  
    };

    updateTime(){
        this.setState({now: new Date()})
    };
    
    render(){


    
        const AllTasks = this.context.tasks.map((task) => <Task
                now={this.state.now}
                task_name={task.task_name}
                due_date={(task.due_time).substr(0, (task.due_time).indexOf(' '))}
                due_time={(task.due_time).substr((task.due_time).indexOf(' ') + 1)}
                time_made={new Date(task.time_made)}
                notifications={task.notifications.split(",")}
                task_id={task.task_id}
                key={task.task_id}
            />
        );

        return(
            <div className="tasks-area">
                { AllTasks }
            </div>
        );
    };
};

export default App;
