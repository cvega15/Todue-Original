import React from 'react';
import { connect } from 'react-redux';

class App extends React.Component{

    // Constructs everything
    constructor(props){

        super(props);
        this.state = {

            task_name: this.props.task_name,
            due_date: this.props.due_date 
        };

        //this.edit_mode = this.edit_mode.bind(this); <--- this is example code for how to bind a function to the this keyword
    };

    handleClick = () => {
        this.props.deletePost(this.props.index);
    };

    render(){
        return(
            <div className="task">
                <h2 style={{ margin: "0", }}>{this.props.task_name}</h2>
                <h3>due: {this.props.due_date}</h3>
                <button>edit task</button> 
                <button onClick={this.handleClick}>delete task</button>
            </div>
        );
    };
};

const mapDispatchToProps = (dispatch) => {
    return{
        deletePost: (id) => { dispatch({type: 'DELETE_POST', id: id }) }
    }
}

export default connect(mapDispatchToProps)(App);
