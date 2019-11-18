import React from 'react';
import { TasksContext } from '../contexts/TasksContext';

class AddTask extends React.Component{
    
    static contextType = TasksContext;

    submit = (event) => {
        event.preventDefault();
        this.props.handleSubmit();
    };

    submitEdit = (event) => {
        event.preventDefault();
        this.props.handleSubmitEdit();
    }

    render(){
        if(this.props.task_data.add === true){
            return(
                <div className="page" id="page-1" >
                    <form id="new-form" onSubmit={this.submit}>
                        <div>
                            <h2>name</h2>
                            <input className="text-input" type="text" maxLength="40" id="task_name" onChange={this.props.handleChange} />
                            <br />
                            <h2>date</h2> 
                            <input className="text-input" type="date" id="due_date" defaultValue={this.props.task_data.due_date} onChange={this.props.handleChange} required />
                            <br />
                            <h2>time</h2>
                            <input className="text-input" type="time" id="due_time" defaultValue={this.props.task_data.due_time} onChange={this.props.handleChange} required />
                            <br />
                        </div>
                    </form> 
                </div>
            );
        }else{
            return(
                <div className="page" id="page-1">
                    <form id="new-form" onSubmit={this.submitEdit}>
                        <div>
                            <h2>name</h2>
                            <input className="text-input" type="text" maxLength="40" id="task_name" onChange={this.props.handleChange} defaultValue={this.props.task_data.task_name} />
                            <br />
                            <h2>date</h2> 
                            <input className="text-input" type="date" id="due_date" onChange={this.props.handleChange} defaultValue={this.props.task_data.due_date} required />
                            <br /> 
                            <h2>time</h2>
                            <input className="text-input" type="time" id="due_time" onChange={this.props.handleChange} defaultValue={this.props.task_data.due_time} required />
                            <br />
                        </div>
                    </form> 
                </div>
            );
        };
    };
};

export default AddTask;