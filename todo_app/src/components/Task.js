import React from 'react';

class App extends React.Component{

    // Constructs everything
    constructor(props){

        super(props);
        this.state = {

            editing: false,
            task_name: this.props.task_name,
            due_date: this.props.due_date 
        };

        this.edit_mode = this.edit_mode.bind(this); // binds the function to the class
        this.delete_task = this.delete_task.bind(this); // binds the function to the class
        this.save_changes = this.save_changes.bind(this); // binds the function to the class
    };

    edit_mode(){
        
        if(this.state.editing){
            this.setState({
                editing: false
            });
        }else{
            this.setState({
                editing: true
            });
        };
    };

    save_changes(){
        
        this.props.edit_task_from_area(this.props.index, this.refs.new_task_name.value, this.refs.new_due_date.value);
        this.setState({
            editing: false
        });
    };

    // Deletes the task
    delete_task(){

        this.props.delete_task_from_area(this.props.index);
    };

    render(){

        if(this.state.editing){
            return(
                <div className="task">
                    
                    <h2>task name</h2>
                    <input type="text" ref="new_task_name" defaultValue={this.props.task_name} required /> 
                    <h2>due date</h2> 
                    <input type="date" ref="new_due_date" defaultValue={this.props.due_date} required /> 
                    <br />

                    <button onClick={this.save_changes}>save</button> 
                    <button onClick={this.edit_mode}>cancel</button>
                </div>
            );
        }else{
            return(
                 <div className="task">
                    <h2>{this.props.task_name}</h2>
                    <h3>due: {this.props.due_date}</h3>
                    <button onClick={this.edit_mode}>edit task</button> 
                    <button onClick={this.delete_task}>delete task</button>
                </div>
            );
        };
    };
};

export default App;
