import React from 'react';
import turn_to_12 from '../Tools';
import { UserContext } from '../contexts/UserContext';

class Notification extends React.Component{

    static contextType = UserContext;

    render(){
        
        var notification = this.props.notification_time;
        if(!this.context.clock_mode){
            notification = turn_to_12(this.props.notification_time);
        }
        return(
            <div className="notification">
                <h3 style={{marginLeft: "1.7vh"}}>{ notification }</h3>
                <button onClick={() => {this.props.delete_notification(this.props.notification_time)}} className="delete-notification-button">delete</button>
            </div>
        );
    };
};

export default Notification;
