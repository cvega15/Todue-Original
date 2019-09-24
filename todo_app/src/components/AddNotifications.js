import React from 'react';
import Notification from './Notification';

class AddNotifications extends React.Component{

    constructor(props){

        super(props);
        this.state = {
            notifications: this.props.notifications,
        };
        this.addNotification = this.addNotification.bind(this);
        this.deleteNotification = this.deleteNotification.bind(this);
    };

    addNotification(notification){
        var to_add = notification.value.toString()
        if(!this.state.notifications.includes(to_add)){
            var new_notifications = this.state.notifications;
            new_notifications.push(to_add);
            this.setState({notifications: new_notifications});
            this.props.handleNotifications(this.state.notifications);
        };
    };

    deleteNotification(to_delete){
        var new_notifications = this.state.notifications;
        new_notifications = new_notifications.filter(notification => notification !== to_delete)
        this.setState({notifications: new_notifications}, () => {
            this.props.handleNotifications(this.state.notifications)
        });
    };

    render(){

        const all_notifications = this.state.notifications.map((notification, index) => <Notification 
                key={index}
                notification_time={notification}
                delete_notification={this.deleteNotification}
            />)

        return(
            <div className="page">
                <div className="notifications-header">
                    <div>
                        <input type="time" defaultValue="00:00" id="notification-input"></input>
                        <button onClick={() => {this.addNotification(document.getElementById('notification-input'))}}>Add</button>
                    </div>
                </div>
                <div className="notifications-area">
                    { all_notifications }
                </div>
            </div>
        );
    };
};

export default AddNotifications;
