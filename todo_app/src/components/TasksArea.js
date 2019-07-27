import React from 'react';
import Task from './Task';
import ModalAdd from './ModalAdd';
import tasks_data from '../../src/TasksData';

class App extends React.Component{

    // Initializes the class and all it's variables and methods
    constructor(){

        // Gets functions from parent class then sets the state
        super();
        this.state = {
            tasks: tasks_data, // An array[] of task objects
        };

        // Binds functions so it can be used elsewhere in the class
        this.add_task = this.add_task.bind(this);
        this.edit_task = this.edit_task.bind(this);
        this.remove_task = this.remove_task.bind(this);
    };

    // Creates a new task with the data passed in
    add_task(task_name, due_date){
      
        // Creates a copy of the tasks array then adds a new task with the passed in info
        var new_tasks = this.state.tasks;
        var new_task = {id: Math.random() * 100, task_name: task_name, due_date: due_date}
        new_tasks.push(new_task);
       
        // Sets the state to the tasks copy
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

        // Sets the state to the tasks copy
        this.setState({
            tasks: new_tasks
        });
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

    // Reserved react function used for rendering the page
    render(){
        
        const AllTasks = this.state.tasks.map((task, index) => <Task 
                key={task.id}
                index={index} 
                task_name={task.task_name} 
                due_date={task.due_date} 
                delete_task_from_area={this.remove_task}
                show_modal_area={this.show_modal}
                edit_task_from_area={this.edit_task} 
            />
        );

        if(this.props.showing_modal){
            return(
                <div className="tasks_area">
                    <ModalAdd 
                        show_modal={this.props.show_modal}
                        modal_mode={this.state.modal_mode}
                        edadd_change={this.show_modal}
                        add_task_to_area={this.add_task} 
                    />
                
                    {AllTasks}
                </div>
            );
        }else{
            return(
                <div className="tasks_area">
                    <br />
                    <div className="tasks_area_scroll">
                        {AllTasks}
                    </div>
                </div>
            );
        };
    };
};

export default App;
