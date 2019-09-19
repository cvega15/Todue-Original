import React from 'react';
import AddTask from './AddTask';
import { ModalContext } from '../contexts/ModalContext';
import { TasksContext } from '../contexts/TasksContext';

class Modal extends React.Component{

    static contextType = ModalContext;

    constructor(props){

        super(props);
        this.state = {
            showing_notifications: false
        };
        this.toggleNotifications = this.toggleNotifications.bind(this);
    };

    toggleNotifications(){
        if(this.state.showing_notifications === false){
            this.setState({ showing_notifications: true });
        }else{
            this.setState({ showing_notifications: false });
        };
    }

    render(){
        const { isShowing, task_data } = this.context;
        const { toggleModal } = this.context;
        
        let title;
        if(task_data === null){
            title = <h1>Add Task</h1>;
        }else{
            title = <h1>Edit Task</h1>;
        }


        if(isShowing === true){
            return(
                <TasksContext.Consumer>{(context) => {
                    return(
                        <div className="modal">
                            <div className="modal-box">
                                <div className="modal-header">
                                    {title}
                                    <button onClick={ toggleModal } >close</button>
                                </div>

                                <AddTask toggleModal={ toggleModal } task_data={ task_data }/>

                            </div>
                            <div className="modal-background" onClick={ toggleModal }></div>
                        </div>
                    )
                }}</TasksContext.Consumer>
            );
        }else{
            return null;
        }
    };
};

export default Modal;
