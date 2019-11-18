import React from 'react';
import { TasksContext } from '../contexts/TasksContext';
import AddNotifications from './AddNotifications';

class AddTask extends React.Component{
    
    static contextType = TasksContext;
    // Constructs everything
    constructor(props){
        super(props);

        var current_date = new Date().toISOString().slice(0, 10);

        if(this.props.task_data === null){
            this.state = {
                task_name: null,
                due_date: current_date,
                due_time: '00:00',
                notifications: [],
            };
        }else{
            var notificationz;
            if(this.props.task_data.notifications[0] === ""){
                notificationz = [];
            }else{
                notificationz = this.props.task_data.notifications;
            }
            this.state = {
                task_name: this.props.task_data.task_name,
                due_date: this.props.task_data.due_date,
                due_time: this.props.task_data.due_time,
                notifications: notificationz,
                task_id: this.props.task_data.task_id,
                time_made: this.props.task_data.time_made,
            };
        };
        
        this.handleNotifications = this.handleNotifications.bind(this);
    };

    handleChange = (event) => {
        this.setState({
            [event.target.id]: event.target.value
        });
    };

    handleNotifications(new_notifications){
        this.setState({
            notifications: new_notifications,
        });
    };

    handleSubmit = (event) => {
        this.context.addTask(this.state.task_name, this.state.due_date + ' ' + this.state.due_time, this.state.notifications.join());
        this.props.toggleModal();
    };

    handleSubmitEdit = (event) => {
        event.preventDefault();
        this.context.editTask(this.state.task_name, this.state.time_made, this.state.due_date + ' ' + this.state.due_time, this.state.notifications.join(), this.state.task_id);
        this.props.toggleModal();
    };

    render(){
        if(this.props.task_data === null){

            return(
                <div className="modal-content">
                    <div className="modal-pages">
                        <div className="page" id="page-1">
                            <form id="new-form" onSubmit={this.handleSubmit}>
                                <div>
                                    <h2 className="form-label">name</h2>
                                    <input className="text-input" type="text" maxLength="40" id="task_name" onChange={this.handleChange} />
                                    <br />
                                    <h2 className="form-label">date</h2> 
                                    <input className="text-input" type="date" id="due_date" defaultValue={this.state.due_date} onChange={this.handleChange} required />
                                    <br />
                                    <h2 className="form-label">time</h2>
                                    <input className="text-input" type="time" id="due_time" defaultValue={this.state.due_time} onChange={this.handleChange} required />
                                    <br />
                                </div>
                            </form> 
                            
                        </div>
                        
                        <AddNotifications handleNotifications={this.handleNotifications} notifications={this.state.notifications} />
                    </div>

                </div>
            );
        }else{
            return(
                <div className="modal-content">
                    <div className="modal-pages">
                        <div className="page" id="page-1">
                            <form id="new-form" onSubmit={this.handleSubmitEdit}>
                                <div>
                                    <h2 className="form-label">name</h2>
                                    <input className="text-input" type="text" maxLength="40" id="task_name" onChange={this.handleChange} defaultValue={this.state.task_name} />
                                    <br />
                                    <h2 className="form-label">date</h2> 
                                    <input className="text-input" type="date" id="due_date" onChange={this.handleChange} defaultValue={this.state.due_date} required />
                                    <br /> 
                                    <h2 className="form-label">time</h2>
                                    <input className="text-input" type="time" id="due_time" onChange={this.handleChange} defaultValue={this.state.due_time} required />
                                    <br />
                                </div>
                            </form> 
                        </div>
                        <AddNotifications handleNotifications={this.handleNotifications} notifications={this.state.notifications} />
                    </div>

                </div>
            );
        };
    };
};

export default AddTask;