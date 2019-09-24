import React, { createContext, Component } from 'react';

export const TasksContext = createContext();

class TasksContextProvider extends Component {
    
    state = {
        tasks: [],
    };

    addTask = (task_name, due_date, due_time, notifications) => {

        if(task_name === null){
            task_name = "untitled";
        };

        var new_tasks = this.state.tasks;
        var new_task = {task_name: task_name, due_date: due_date, due_time: due_time, notifications: notifications, task_id: Math.random() * 1000}
        new_tasks.push(new_task);

        this.setState({
            tasks: new_tasks
        });
    };

    editTask = (task_name, due_date, due_time, notifications, task_id) => {
        var new_task = {task_name: task_name, due_date: due_date, due_time: due_time, notifications: notifications, task_id: task_id}
        var i;

        for(i = 0; i < this.state.tasks.length; i++){
            if(this.state.tasks[i].task_id === task_id){
                var new_tasks = this.state.tasks;
                this.state.tasks.splice(i, 1, new_task)
                this.setState({
                    tasks: new_tasks
                });
                return
            };
        };
    };
    
    deleteTask = (task_id) => {
        var new_tasks = this.state.tasks.filter(function(task) {
            return task.task_id !== task_id;
        });
        this.setState({
            tasks: new_tasks 
        });
    };

    render() {
        return ( 
            <TasksContext.Provider value={{...this.state, addTask: this.addTask, deleteTask: this.deleteTask, editTask: this.editTask}}>
                {this.props.children}
            </TasksContext.Provider>
        );
    };
};

export default TasksContextProvider;