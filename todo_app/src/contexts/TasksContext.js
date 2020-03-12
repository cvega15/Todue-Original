import React, { createContext, Component } from 'react';
import { UserContext } from '../contexts/UserContext';
import logo from '../images/ToDue192.png';

export const TasksContext = createContext();

class TasksContextProvider extends Component {

    static contextType = UserContext;

    constructor(props){
        super(props);

        var tasks = [];
        var all_notifications = [];

        if(localStorage.getItem('tasks') !== null){
            var tasks = JSON.parse(localStorage.getItem('tasks'));
        };
        if(localStorage.getItem('all_notifications') !== null){
            var all_notifications = JSON.parse(localStorage.getItem('all_notifications'));
        };

        this.state = {
            tasks: tasks,
            all_notifications: all_notifications,
            now: new Date()
        };

        this.notifications_index = 0;

        this.sendAllTasks = this.sendAllTasks.bind(this);
        this.getTasks = this.getTasks.bind(this);
        this.clearEverything = this.clearEverything.bind(this);
        this.sortTasks = this.sortTasks.bind(this);
        this.checkNotifications = this.checkNotifications.bind(this);
        this.buildNotifications = this.buildNotifications.bind(this);
        this.setNotificationsIndex = this.setNotificationsIndex.bind(this);
        this.notify = this.notify.bind(this);
        this.deleteNotifications = this.deleteNotifications.bind(this);
    };

    componentDidUpdate(){
        console.log('component did update');
        localStorage.setItem('tasks', JSON.stringify(this.state.tasks));
        localStorage.setItem('all_notifications', JSON.stringify(this.state.all_notifications));
        
    };

    componentDidMount(){ 
        if(this.context.logged_in){
            this.getTasks();
        }
        var interval_id = setInterval(() => this.checkNotifications(), 3000);
        this.interval_id = interval_id;
        
    };

    sendAllTasks(){
        if(this.context.logged_in){
            fetch('http://34.67.56.249/recieve-all-tasks', {
                method: 'POST',
                headers: {
                    'Authorization': localStorage.getItem('id_token'),
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.state.tasks)
            }).then(response => {
                this.getTasks();
            }).catch((error) => {
                this.context.goOffline(error);
            });
        };
    };

    sortTasks(){
        var sortedTasks = this.state.tasks.sort((a, b) => (a.due_time > b.due_time) ? 1 : -1);
        this.setState({ tasks: sortedTasks})
    };

    addTask = (task_name, due_time, notifications, task_id) => {
        
        if(task_name === null){
            task_name = "untitled";
        };

        var new_task_id = task_id;
        if(task_id === undefined){
            new_task_id = Math.floor((Math.random() * 1000));
        }

        var current_time = new Date()
        var new_tasks = this.state.tasks;
        var new_task = {task_name: task_name, due_time: due_time, notifications: notifications, task_id: new_task_id, time_made: current_time, last_updated: current_time.getTime()}
        new_tasks.push(new_task);
        
        this.setState({
            tasks: new_tasks
        }, () => {
            this.sortTasks();
            this.buildNotifications();
        });
        
        if(this.context.logged_in){
            fetch('http://34.67.56.249/post-task', {
                method: 'POST',
                headers: {
                    'Authorization': localStorage.getItem('id_token'),
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(new_task)
            }).then(response => {
                if(response.status == 401){
                    this.context.toggleLogin()
                    this.clearEverything()
                    localStorage.clear();
                }
            }).catch((error) => {
                console.log('adding task failed')
                this.context.goOffline(error);
                this.context.addTaskToTicket(new_task, "add");
            });
        };
    };

    editTask = (task_name, time_made, due_time, notifications, task_id) => {

        if(task_name === ''){
            task_name = "untitled";
        };
        
        var new_task = {task_name: task_name, time_made: time_made, due_time: due_time, notifications: notifications, task_id: task_id, last_updated: (new Date()).getTime()}
        var i;

        for(i = 0; i < this.state.tasks.length; i++){
            if(this.state.tasks[i].task_id === task_id){
                var new_tasks = this.state.tasks;
                this.state.tasks.splice(i, 1, new_task)
                this.setState({
                    tasks: new_tasks
                }, () => {
                    this.sortTasks();
                    this.buildNotifications();
                });

                if(this.context.logged_in){
                    fetch('http://34.67.56.249/edit-task', {
                        method: 'POST',
                        headers: {
                            'Authorization': localStorage.getItem('id_token'),
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(new_task)
                    }).then(response => {
                        if(response.status == 401){
                            this.context.toggleLogin()
                            this.clearEverything()
                            localStorage.clear();
                        }
                    }).catch((error) => {
                        console.log('editing task failed')
                        this.context.goOffline(error);
                        this.context.addTaskToTicket(new_task, "edit");
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
        }, () => {
            this.sortTasks();
            this.buildNotifications();
        });

        if(this.context.logged_in){
            fetch('http://34.67.56.249/delete-task', {
                method: 'DELETE',
                headers: {
                    'Authorization': localStorage.getItem('id_token'),
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(task_id)
            }).then(response => {
                if(response.status == 401){
                    this.context.toggleLogin()
                    this.clearEverything()
                    localStorage.clear();
                }
            }).catch((error) => {
                console.log('deleting task failed')
                this.context.goOffline(error);
                this.context.addTaskToTicket(task_id, "delete");
            });
        };
    };

    getTasks(){
        console.log("getting tasks")
        if(this.context.logged_in){
            fetch('http://34.67.56.249/get-tasks', {
                method: 'GET',
                headers: {
                    'Authorization': localStorage.getItem('id_token'),
                }
            }).then(response => {
                if(response.ok === false){
                    throw "error"
                }else if(response.status == 401){
                    this.context.toggleLogin()
                    this.clearEverything()
                    localStorage.clear();
                    return
                }
                return response.json();
            }).then(tasks => {
                console.log('thenning 2')
                this.setState({
                    tasks: tasks
                }, () => {
                    this.sortTasks();
                    this.buildNotifications();
                });
                this.context.syncTrue()

            }).catch((error) => {

                // Take everything from local storage and put it in the state's tasks

                console.log('getting tasks failed')
                console.log(error)
                this.context.goOffline(error);
            });
        }
    }

    clearEverything(){
        this.setState({
            tasks: [],
        });
    };

    buildNotifications(){
        var current_date = new Date();
        var new_notifications = []

        var array_len = this.state.tasks.length;
        var i = 0;
        for(i; i < array_len; i++){

            var current_task = this.state.tasks[i];
            var task_id = current_task.task_id;
            
            if(new Date(current_task.due_time.replace(' ', ':')) > current_date){
                new_notifications.push({
                    date: ((current_task.due_time).substr(0, (current_task.due_time).indexOf(' '))),
                    time: ((current_task.due_time).substr((current_task.due_time).indexOf(' ') + 1)),
                    id: task_id
                });

                var task_notifications = current_task.notifications.split(",");
                if(task_notifications[0] === ""){
                    task_notifications = []
                };
                var notifications_length = task_notifications.length;
                var o = 0;
                for(o; o < notifications_length; o++){
                    new_notifications.push({
                        time: task_notifications[o],
                        id: task_id
                    });
                };
            };
        };
        this.setState({all_notifications: new_notifications.sort((a, b) => (a.time > b.time) ? 1 : -1)}, () => {this.setNotificationsIndex();});
    };
    
    setNotificationsIndex(){
        var current_time = new Date();
        current_time = (("0" + (current_time.getHours())).slice(-2) + ':' + ("0" + (current_time.getMinutes())).slice(-2))

        var index = 0;
        var length = this.state.all_notifications.length;
        for(index; index < length; index++){
            if(this.state.all_notifications[index].time > current_time){
                this.notifications_index = index;
                return
            };
        };
        this.notifications_index = 0;
    };

    deleteNotifications(id){
        var new_notifications = this.state.all_notifications.filter(notification => notification.id !== id);
        this.setState({all_notifications: new_notifications});
    };

    notify(id, type){
        if(type === 'daily'){
            console.log('daily notification')
            new Notification('To Due', {
                body: 'Daily reminder: ' + this.state.tasks.find(notification => notification.task_id === id).task_name,
                icon: logo
            });
        }else if(type === 'final'){

            new Notification('To Due', {
                body: 'Now due! ' + this.state.tasks.find(notification => notification.task_id === id).task_name,
                icon: logo
            });
        };
    };

    checkNotifications(){
        if(this.state.all_notifications.length >= 1){
            var notification_object = this.state.all_notifications[this.notifications_index];
            var current_time = new Date();

            if((("0" + (current_time.getHours())).slice(-2) + ':' + ("0" + (current_time.getMinutes())).slice(-2)) === notification_object.time){
                if(typeof notification_object.date === 'undefined'){
                    this.notify(notification_object.id, 'daily')

                    if(this.notifications_index === this.state.all_notifications.length-1){
                        this.notifications_index = 0;
                    }else{
                        this.notifications_index++;
                        this.checkNotifications();
                    };

                }else{
                    var today = new Date();

                    if((today.getFullYear() + '-' + ("0" + (today.getMonth() + 1)).slice(-2) + '-' + ("0" + (today.getDate())).slice(-2)) === notification_object.date){
                        
                        this.notify(notification_object.id, 'final')
                        this.deleteNotifications(notification_object.id);
                        this.setNotificationsIndex();
                        this.checkNotifications();
                    }else{

                        if(this.notifications_index === this.state.all_notifications.length-1){
                            this.notifications_index = 0;
                        }else{
                            this.notifications_index++;
                            this.checkNotifications();
                        };  
                    };
                };
            };
        };
    };

    componentWillUnmount(){
        clearInterval(this.interval_id);  
    };

    render() {
        return(
            <TasksContext.Provider value={{...this.state, clearEverything: this.clearEverything, addTask: this.addTask, deleteTask: this.deleteTask, editTask: this.editTask, sendAllTasks: this.sendAllTasks, getTasks: this.getTasks}}>
                {this.props.children}
            </TasksContext.Provider>
        );
    };
};

export default TasksContextProvider;