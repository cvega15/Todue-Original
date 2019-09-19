import React, { createContext, Component } from 'react';

export const TasksContext = createContext();

class TasksContextProvider extends Component {
    
    state = {
        tasks: [
            {task_name: "smoke weed", due_date: "2019-09-09", due_time: "02:31", notifications: "06:50,10:30,09:15", id: 347},
            {task_name: "beat meat", due_date: "2019-09-12", due_time: "06:30", notifications: "06:50,10:30", id: 152}
        ],
    };

    addTask = (task_name, due_date, due_time, notifications) => {
        if(task_name === null){
            task_name = "untitled";
        }

        var new_tasks = this.state.tasks;
        var new_task = {task_name: task_name, due_date: due_date, due_time: due_time, notifications: notifications, id: Math.random() * 1000}
        new_tasks.push(new_task);

        this.setState({
            tasks: new_tasks
        });
    };

    editTask = (task_name, due_date, due_time, task_id) => {
        
        var new_task = {task_name: task_name, due_date: due_date, due_time: due_time, id: task_id}

        var i;
        for(i = 0; i < this.state.tasks.length; i++){
            if(this.state.tasks[i].id === task_id){
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
            return task.id !== task_id;
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