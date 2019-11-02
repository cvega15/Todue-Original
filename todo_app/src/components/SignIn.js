import React from 'react';
import GoogleLogin from 'react-google-login';
import { GoogleLogout } from 'react-google-login';
import { UserContext } from '../contexts/UserContext';
import { TasksContext } from '../contexts/TasksContext';

class SignIn extends React.Component {

    static contextType = UserContext;

    constructor(props){
        super(props)
    }

    signOut = () => {
        this.context.toggleLogin()
        this.context.destroyId()
    }

    render(){
        if(this.context.logged_in){
            return (
                <TasksContext.Consumer>{(TasksContext) => {
                    return(
                        <div>
                            <GoogleLogout
                                clientId = "195081855240-jjsqpn2t0oucb8ets7li98p8vodja8jd.apps.googleusercontent.com"
                                buttonText = "logout"
                                onLogoutSuccess = {(response) => {
                                    this.signOut()
                                    TasksContext.clearEverything()
                                }}
                            ></GoogleLogout>
                        </div>
                    )
                }}</TasksContext.Consumer>
            );
        }else{
            return(
                <TasksContext.Consumer>{(TasksContext) => {
                    return(
                        <div>
                            <div id="googleButton"></div>
                            {
                                <GoogleLogin
                                    clientId="195081855240-jjsqpn2t0oucb8ets7li98p8vodja8jd.apps.googleusercontent.com"
                                    buttonText="Login with google"
                                    onSuccess={(response) => {
                                        var id_token = response.getAuthResponse().id_token;
                                        
                                        this.context.setId(id_token);
                                        this.context.toggleLogin();
                                        TasksContext.getTasks();
                                        this.context.getSettings();
                                    
                                        fetch('http://34.67.56.249:5000/sign-up-in', {
                                            method: 'POST',
                                            body: JSON.stringify(id_token)
                                        }).then(() => {
                                            TasksContext.sendAllTasks();
                                        })
                                    }}
                                    onFailure={() => {console.log('couldnt sign in')}}
                                    cookiePolicy={'single_host_origin'}
                                />
                            }
                        </div>
                    )
                }}</TasksContext.Consumer>
            );
        };
    };
};

export default SignIn;
