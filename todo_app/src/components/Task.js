import React from 'react';

class App extends React.Component{

    constructor(props){
        super(props);
        this.state = {
            is_editing: false 
        };
        this.edit_task = this.edit_task.bind(this); //binds the function to the class
        this.delete_task = this.delete_task.bind(this); // binds the function to the class
        this.save_task = this.save_task.bind(this) // binds the function to the class
    };

    edit_task(){
        this.setState({
            is_editing: true
        });
    };

    save_task(){
        var new_name = this.refs.task_name_edit.value;
        var new_date = this.refs.due_date_edit.value; 
        this.props.edit_task_from_area(this.props.index, new_name, new_date);
        this.setState({
            is_editing: false,
        });
    };

    delete_task(){
        this.props.delete_task_from_area(this.props.index);
    };

    render_normal(){
        return(
            <div className="task">
                <h2>{this.props.task_name}</h2>
                <h3>due: {this.props.due_date}</h3>
                <button onClick={this.edit_task}>edit task</button> 
                <button onClick={this.delete_task}>delete task</button>
            </div>
        );
    };

    render_edit(){
        return(
            <div className="task">
                <textarea ref="task_name_edit" defaultValue={this.props.task_name}></textarea>
                <textarea ref="due_date_edit" defaultValue={this.props.due_date}></textarea>
                <button onClick={this.save_task}>save task</button> 
            </div>
        );
    };

    render(){
        if(this.state.is_editing){
            return this.render_edit();
        }else{
            return this.render_normal();
        };
    };
};

export default App;
