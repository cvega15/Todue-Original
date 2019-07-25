import React from 'react';

class App extends React.Component{

    constructor(props){

        super(props);

        this.state = {
            identifier: this.props.identifier,
        };

        this.on_submit = this.on_submit.bind(this);
        this.handle_change = this.handle_change.bind(this);
    };

    on_submit(event){

        event.preventDefault();
        this.props.edadd_change();
        this.props.add_task_to_area(this.state.task_name, this.state.due_date);
    };

    handle_change(event){

        this.setState({
            [event.target.name]: event.target.value
        });
    };

    render(){
        return(
            <div className="modal_background">
                <div className="modal_content">
                    <h1>please enter new task information</h1>
                    <form>
                        <label>name</label>     
                        <input type="text" 
                               name="task_name" 
                               onChange={this.handle_change} 
                               required />
                        <label>date</label> 
                        <input type="text" 
                               name="due_date" 
                               onChange={this.handle_change} 
                               required />
                        <button onClick={(event) => this.on_submit(event)}>save</button>
                        <button onClick={this.props.edadd_change}>cancel</button>
                    </form> 
                </div>
            </div>
        );
    };
};

export default App;
