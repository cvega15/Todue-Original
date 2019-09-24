import React from 'react';
import { TasksContext } from '../contexts/TasksContext';
import { ModalContext } from '../contexts/ModalContext';

class App extends React.Component{

    static contextType = ModalContext;
    // Constructs everything
    constructor(props){

        super(props);
        this.handleEdit = this.handleEdit.bind(this);
    };

    handleEdit(){
        this.context.toggleModal(this.props);
    };

    render(){
        return(
            <TasksContext.Consumer>{(context => {
                const { deleteTask } = context;
                return(
                    <div className="task">
                        <h2 style={{ margin: "0", }}>{ this.props.task_name }</h2>
                        <h3>due date: { this.props.due_date }</h3>
                        <h3>due time: { this.props.due_time }</h3>
                        <button onClick={ this.handleEdit }>edit task</button> 
                        <button onClick={ ()=>deleteTask(this.props.task_id) }>delete task</button>
                    </div>
                )
            })}</TasksContext.Consumer>
        );
    };
};

export default App;
