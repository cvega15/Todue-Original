import React from 'react';
import { ModalContext } from '../contexts/ModalContext';
import { TasksContext } from '../contexts/TasksContext';
import ModalPages from './ModalPages';

class Modal extends React.Component{

    static contextType = ModalContext;

    constructor(props){

        super(props);
        this.state = {
            showing_notifications: false,
            scroll: 0,
        };
        this.toggleNotifications = this.toggleNotifications.bind(this);
        this.changeScroll = this.changeScroll.bind(this);
    };

    toggleNotifications(){
        if(this.state.showing_notifications === false){
            this.setState({ showing_notifications: true });
        }else{
            this.setState({ showing_notifications: false });
        };
    }

    changeScroll(page){
        this.setState({scroll: page})  
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
                                    <button className="modal-button" onClick={ toggleModal } >close</button>
                                    {title}
                                    <button className="modal-button" form="new-form">save</button>
                                </div>

                                <div style={{display: "flex", justifyContent: "space-between", marginLeft: "4%", marginRight: "4%"}}>
                                    <button className='page-change' onMouseUp={() => {document.getElementById('#modal-pages').scrollBy(-100,0)}}>&lt;</button>
                                    <div style={{display: "flex", paddingTop: "2.8vh"}}>
                                        <div className="page-indicator" id="#pagei-1" style={ (this.state.scroll === 0) ? {backgroundColor: "white"} : {}}></div>
                                        <div className="page-indicator" id="#pagei-2" style={ (this.state.scroll === 1) ? {backgroundColor: "white"} : {}}></div>
                                    </div>
                                    <button className='page-change' onMouseUp={() => {document.getElementById('#modal-pages').scrollBy(100,0)}}>&gt;</button>
                                </div>

                                <ModalPages changeScroll={ this.changeScroll } toggleModal={ toggleModal } task_data={ task_data }/>
                                
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
