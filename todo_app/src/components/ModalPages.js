import React from 'react';
import AddTask from './AddTask.js';
import AddNotifications from './AddNotifications';
import { TasksContext } from '../contexts/TasksContext';

class ModalPages extends React.Component {

    static contextType = TasksContext;

    constructor(props){
        super(props);
        this.props.changeScroll(0);
        var current_date = new Date().toISOString().slice(0, 10);

        if(this.props.task_data === null){
            this.state = {
                task_name: null,
                due_date: current_date,
                due_time: '00:00',
                notifications: [],
                add: true,
            };
        }else{
            var task_notificaions;
            if(this.props.task_data.notifications[0] === ""){
                task_notificaions = [];
            }else{
                task_notificaions = this.props.task_data.notifications;
            }
            this.state = {
                task_name: this.props.task_data.task_name,
                due_date: this.props.task_data.due_date,
                due_time: this.props.task_data.due_time,
                notifications: task_notificaions,
                task_id: this.props.task_data.task_id,
                time_made: this.props.task_data.time_made,
                add: false,
            };
        };

        this.handleNotifications = this.handleNotifications.bind(this);
    };

    handleNotifications(new_notifications){
        this.setState({
            notifications: new_notifications,
        });
    };

    handleChange = (event) => {
        this.setState({
            [event.target.id]: event.target.value
        });
    };

    handleSubmit = () => {
        this.context.addTask(this.state.task_name, this.state.due_date + ' ' + this.state.due_time, this.state.notifications.join());
        this.props.toggleModal();
    };

    handleSubmitEdit = (event) => {
        this.context.editTask(this.state.task_name, this.state.time_made, this.state.due_date + ' ' + this.state.due_time, this.state.notifications.join(), this.state.task_id);
        this.props.toggleModal();
    };


    render(){
        return(

            <div className="modal-pages" id="#modal-pages" onScroll={() => {
                var element = document.getElementById("#modal-pages");
                var scroll = element.scrollLeft;

                if(scroll === 0){
                    this.props.changeScroll(0);
                }else if(scroll >= Math.floor(element.scrollWidth/2)){
                    this.props.changeScroll(1);
                }

            }}>
                <AddTask handleChange={ this.handleChange } handleSubmit={this.handleSubmit} handleSubmitEdit={this.handleSubmitEdit} task_data={ this.state } />
                <AddNotifications handleSubmitEdit={this.handleSubmitEdit} handleNotifications={this.handleNotifications} notifications={this.state.notifications} />
            </div>
        );
    };
};

export default ModalPages;