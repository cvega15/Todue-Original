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

        const all_notifications = (this.state.notifications.sort()).map((notification, index) => <Notification 
                key={index}
                notification_time={notification}
                delete_notification={this.deleteNotification}
            />)

        return(
            <div className="page" id="page-2">
                <div id="new-form">
                    <div className="notifications-header">
                        <h2 className="form-label">daily recurring notifications</h2>
                        <div style={{display: "flex"}}>
                            <input className="text-input" style={{height: "8vh", borderRadius: "15px 0px 0px 15px"}} type="time" defaultValue="00:00" id="notification-input" required></input>
                            <button className="add-notification-button" onClick={() => {this.addNotification(document.getElementById('notification-input'))}}>+</button>
                        </div>
                    </div>
                    <br></br>
                    <div className="notifications-area">
                        { all_notifications }
                    </div>
                </div>
            </div>
        );
    };
};

export default AddNotifications;
