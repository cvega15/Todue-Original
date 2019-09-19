import React from 'react';
import Task from './Task';
import { TasksContext } from '../contexts/TasksContext';

class App extends React.Component{

    static contextType = TasksContext;

    render(){
        const AllTasks = this.context.tasks.map((task, index) => <Task 
                key={index}
                task_name={task.task_name}
                due_date={task.due_date}
                due_time={task.due_time}
                notifications={task.notifications.split(",")}
                id={task.id}
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
