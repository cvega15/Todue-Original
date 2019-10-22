import React, { createContext, Component } from 'react';
import { UserContext } from '../contexts/UserContext';

export const TasksContext = createContext();

class TasksContextProvider extends Component {

    static contextType = UserContext;

    constructor(props){
        super(props);

        this.state = {
            tasks: [],
            ticket: [],
            online: true,
        };
        this.addToTicket = this.addToTicket.bind(this);
        this.sendTicket = this.sendTicket.bind(this);
        this.checkConnection = this.checkConnection.bind(this);
        this.sendAllTasks = this.sendAllTasks.bind(this);
        this.getTasks = this.getTasks.bind(this);
    };

    checkConnection(){
        console.log('program offline')

        var checker = setInterval(() => {
            if(navigator.onLine){
                this.sendTicket()
                this.setState({
                    online: true,
                })
                clearInterval(checker);
                return;
            };
        }, 2000);
    };
    
    sendTicket(){

        fetch('http://34.67.56.249:5000/recieve-ticket', {
            method: 'POST',
            headers: {
                'Authorization': this.context.id_token,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.state.ticket)
        }).then(() => {
            this.setState({
                ticket: [],
            })
            return true;
        }).catch((error) => {
            return false;
        });
    };

    sendAllTasks(){
        if(this.context.logged_in){
            fetch('http://34.67.56.249:5000/recieve-all-tasks', {
                method: 'POST',
                headers: {
                    'Authorization': this.context.id_token,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.state.tasks)
            }).then(response => {
                this.getTasks();
            }).catch((error) => {
                if(this.state.online){
                    this.checkConnection();
                };
                this.setState({
                    online: false,
                });
            });
        };
    };

    addToTicket(data, mode){

        if(mode === "add"){
            this.state.ticket.push({data, mode})
        }else if(mode === "edit"){
            this.state.ticket.push({data, mode})
        }else{
            this.state.ticket.push({data, mode})
        }
        console.log(this.state.ticket);
    };

    addTask = (task_name, due_time, notifications, task_id) => {
        
        if(task_name === null){
            task_name = "untitled";
        };

        var le_task_id = task_id;
        if(task_id === undefined){
            le_task_id = Math.floor((Math.random() * 1000));
        }

        var current_time = new Date()
        var new_tasks = this.state.tasks;
        var new_task = {task_name: task_name, due_time: due_time, notifications: notifications, task_id: le_task_id, time_made: current_time, last_updated: current_time.getTime()}
        new_tasks.push(new_task);

        this.setState({
            tasks: new_tasks
        });
        
        if(this.context.logged_in){
            fetch('http://34.67.56.249:5000/post-task', {
                method: 'POST',
                headers: {
                    'Authorization': this.context.id_token,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(new_task)
            }).catch((error) => {
                if(this.state.online){
                    this.checkConnection();
                };
                this.addToTicket(new_task, "add");
                this.setState({
                    online: false,
                });
            });
        };
    };

    editTask = (task_name, time_made, due_time, notifications, task_id) => {
        
        var new_task = {task_name: task_name, time_made: time_made, due_time: due_time, notifications: notifications, task_id: task_id, last_updated: (new Date()).getTime()}
        var i;

        for(i = 0; i < this.state.tasks.length; i++){
            if(this.state.tasks[i].task_id === task_id){
                var new_tasks = this.state.tasks;
                this.state.tasks.splice(i, 1, new_task)
                this.setState({
                    tasks: new_tasks
                });

                if(this.context.logged_in){
                    fetch('http://34.67.56.249:5000/edit-task', {
                        method: 'POST',
                        headers: {
                            'Authorization': this.context.id_token,
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(new_task)
                    }).catch((error) => {
                        if(this.state.online){
                            this.checkConnection();
                        };
                        this.addToTicket(new_task, "edit");
                        this.setState({
                            online: false,
                        });
                    });
                    return;
                };
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

        if(this.context.logged_in){
            fetch('http://34.67.56.249:5000/delete-task', {
                method: 'DELETE',
                headers: {
                    'Authorization': this.context.id_token,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(task_id)
            }).catch((error) => {
                if(this.state.online){
                    this.checkConnection();
                };
                this.addToTicket(task_id, "delete");
                this.setState({
                    online: false,
                }); 
            });
        };
    };

    getTasks(){
        if(this.context.logged_in){
            fetch('http://34.67.56.249:5000/get-tasks', {
                method: 'GET',
                headers: {
                    'Authorization': this.context.id_token,
                }
            }).then(response => {
                return response.json();
            }).then(tasks => {
                this.setState({
                    tasks: tasks
                });
            }).catch((error) => {
                this.setState({
                    online: false,
                });
            });
        }
    }

    componentDidMount(){
        this.getTasks();
    };

    render() {
        return ( 
            <TasksContext.Provider value={{...this.state, addTask: this.addTask, deleteTask: this.deleteTask, editTask: this.editTask, sendAllTasks: this.sendAllTasks, getTasks: this.getTasks}}>
                {this.props.children}
            </TasksContext.Provider>
        );
    };
};

export default TasksContextProvider;