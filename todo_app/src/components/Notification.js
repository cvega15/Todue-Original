import React from 'react';

class Notification extends React.Component{

    render(){

        return(
            <div>
                <h3>{ this.props.notification_time }</h3>
                <button onClick={() => {this.props.delete_notification(this.props.notification_time)}}>delete</button>
            </div>
        );
    };
};

export default Notification;
