import React from 'react';
import App from './Task';

class AddTask extends React.Component{

    constructor(){
        //var todays_date = new Date().toISOString().substr(0, 10);
        super()
        this.state = {
            task_name: null,
            due_date: null,
            due_time: null,
        }
    }

    handleChange = (e) => {
        this.setState({
            [e.target.id]: e.target.value
        })
    }

    handleSubmit = (e) => {
        e.preventDefault();
        console.log(this.state)
    }

    render(){
        return(
            <div className="AddTask">
                <h1>please enter new task information</h1>
                <form onSubmit={this.handleSubmit}>
                    <label>name</label>     
                    <input type="text" id="task_name" onChange={this.handleChange} />
                    <br />
                    <label>date</label> 
                    <input type="date" id="due_date" value={this.state.todays_date} onChange={this.handleChange} />
                    <br /> 
                    <label>time</label>
                    <input type="time"id="due_time" value="00:00" onChange={this.handleChange}/>
                    <br />
                    <button>save</button>
                </form> 
            </div>
        );
    };
};

export default AddTask;
