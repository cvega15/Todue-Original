import React from 'react';
import { TasksContext } from '../contexts/TasksContext';
import { ModalContext } from '../contexts/ModalContext';

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
            <TasksContext.Consumer>{(context => {
                const { deleteTask } = context;
                return(
                    <div className="task">
                        <div className="task-content">
                            <div className="left-task">
                                <h2 style={{ margin: "0", }}>{ this.props.task_name }</h2>
                                <h3>{ this.props.due_date }</h3>
                                <h3>{ this.props.due_time }</h3>
                                <button onClick={ this.handleEdit }>edit task</button>
                                <button onClick={ () => deleteTask(this.props.task_id) }>delete task</button>
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
        );
    };
};

export default App;
