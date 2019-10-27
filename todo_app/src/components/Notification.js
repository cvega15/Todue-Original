import React from 'react';
import turn_to_12 from '../Tools';
import { UserContext } from '../contexts/UserContext';

class Notification extends React.Component{

    static contextType = UserContext;

    render(){
        
        var le_time = this.props.notification_time;
        if(!this.context.clock_mode){
            le_time = turn_to_12(this.props.notification_time);
        }
        return(
            <div>
                <h3>{ le_time }</h3>
                <button onClick={() => {this.props.delete_notification(this.props.notification_time)}}>delete</button>
            </div>
        );
    };
};

export default Notification;
