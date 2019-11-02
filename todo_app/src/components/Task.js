import React from 'react';
import { TasksContext } from '../contexts/TasksContext';
import { ModalContext } from '../contexts/ModalContext';
import { UserContext } from '../contexts/UserContext';
import { useSwipeable } from 'react-swipeable';
import turn_to_12 from '../Tools';

class App extends React.Component{

    static contextType = ModalContext;
    // Constructs everything
    constructor(props){

        super(props);
        
        this.second = 1000
        this.minute = this.second * 60
        this.hour = this.minute * 60
        this.day = this.hour * 24

        var sec;
        var min;
        var hrs;
        var dys;

        this.state = {
            now: new Date(),
        }

        this.handleEdit = this.handleEdit.bind(this);

    };

    componentDidMount(){
        var interval_id = setInterval(()=>this.updateTime(), 1000);
        this.interval_id = interval_id
    };

    componentWillUnmount(){
        clearInterval(this.interval_id);  
    };

    updateTime(){
        this.setState({now: new Date()})
    };

    handleEdit(){
        this.context.toggleModal(this.props);
    };

    render(){

        var new_time = (new Date(this.props.due_date + ':' + this.props.due_time).getTime())
        var difference = new_time - this.props.now;
        
        if(difference > 0){
            var total_difference = new_time - ((this.props.time_made).getTime())
            this.sec = Math.floor((difference%(this.minute))/1000);
            this.min = Math.floor((difference%(this.hour))/this.minute);
            this.hrs = Math.floor((difference%(this.day))/this.hour);
            this.dys = Math.floor((difference/(this.day)));
        }else{
            this.sec = 0;
            this.min = 0;
            this.hrs = 0;
            this.dys = 0;
        }

        var percentage = (Math.floor(difference/1000)/Math.floor(total_difference/1000))*100

        var styling = {
            width: percentage + '%',
        };
        return(
            <UserContext.Consumer>{(UserContext => (
                <TasksContext.Consumer>{(TasksContext => {
                    const { clock_mode } = UserContext
                    const { deleteTask } = TasksContext;
                    var le_time = this.props.due_time;
                    if(!clock_mode){
                        var le_time = turn_to_12(this.props.due_time);
                    }
                    return(
                        <div className="task">
                            <div className="task-content">
                                <div className="left-task">
                                    <h2 style={{fontSize: "2.2vh", marginBottom: "0", width: "100%", wordWrap: "break-word"}}>{ this.props.task_name }</h2>
                                    <div>
                                        <h3>{ this.props.due_date }</h3>
                                        <h3>{ le_time }</h3>
                                    </div>
                                    {/*
                                    <button onClick={ this.handleEdit }>edit task</button>
                                    <button onClick={ () => deleteTask(this.props.task_id) }>delete task</button>                                    
                                    */}
                                </div>
                                <div className="right-task">
                                    <div>
                                        <h3>dys: { this.dys }</h3>
                                        <h3>hrs: { this.hrs }</h3>
                                        <h3>min: { this.min }</h3>
                                        <h3>sec: { this.sec }</h3>
                                    </div>
                                </div>
                            </div>
                            <div className="bar" style={ styling }></div>
                        </div>
                        
                    )
                })}</TasksContext.Consumer>
            ))}</UserContext.Consumer>
        );
    };
};

export default App;
