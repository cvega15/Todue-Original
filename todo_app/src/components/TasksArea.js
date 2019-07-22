import React from 'react';
import Task from './Task';
import tasks_data from '../../src/TasksData';

class App extends React.Component{

    constructor(){

        // Gets functions from parent class then sets the state
        super();
        this.state = {
            tasks: tasks_data // An array[] of task objects
        };

        // Binds functions to the this keyword
        this.remove_task = this.remove_task.bind(this);
        this.edit_task = this.edit_task.bind(this);
        this.add_task = this.add_task.bind(this);
    };

    // Adds a task to the array of tasks
    add_task(){
        console.log("task added button waz clicked lolz");
    };

    // Removes a task from the array of tasks
    remove_task(index){

        // Creates a copy of the tasks array which has the index removed
        var new_tasks = this.state.tasks;
        new_tasks.splice(index, 1);

        // Sets the state to the new copy of the array
        this.setState({
            tasks: new_tasks 
        });
    };

    // Edits the task that was passed in as index and changes the name and due date to the parameter's new_name and new_date
    edit_task(index, new_name, new_date){

        // Creates a copy of the tasks array then edits the index's contents with the passed in info
        var new_tasks = this.state.tasks;
        new_tasks[index].due_date = new_date;
        new_tasks[index].task_name = new_name;
        console.log(new_tasks[index].due_date);
        console.log(new_tasks[index].task_name);
        
        this.setState({
            tasks: new_tasks
        })
        console.log(this.state.tasks[index].due_date);
    
    };

    // Reserved react function used for rendering the page
    render(){
   
        const AllTasks = this.state.tasks.map((task, index) => <Task 
                key={task.id}
                index={index} 
                task_name={task.task_name} 
                due_date={task.due_date} 
                delete_task_from_area={this.remove_task}
                edit_task_from_area={this.edit_task}
            />
        );

        return(
            <div className="tasks_area">
                <button onClick={this.add_task}>add task</button>
                {AllTasks}
            </div>
        );
    };
};

export default App;
