import React from 'react';
import GoogleLogin from 'react-google-login';
import { GoogleLogout } from 'react-google-login';
import { UserContext } from '../contexts/UserContext';
import { TasksContext } from '../contexts/TasksContext';

class SignIn extends React.Component {

    static contextType = UserContext;

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
                                    this.context.toggleLogin();
                                    localStorage.clear();
                                    TasksContext.clearEverything();
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
                                    theme="dark"
                                    accessType="offline"
                                    responseType="code"
                                    isSignedIn="true"
                                    prompt="none"
                                    redirectUri="http://localhost:3000/settings"
                                    onSuccess={(response) => {
                                        console.log(response)
                                        var authorization_code = response.code;
                                        localStorage.setItem('auth_code', authorization_code)
                                        fetch("http://34.67.56.249/sign-up-in", {
                                            method: 'POST',
                                            body: authorization_code
                                        }).then(response => {
                                            return response.json()
                                        }).then(data => {
                                            console.log(data)
                                            this.context.toggleLogin();

                                            console.log(typeof data.refresh_token);
                                            localStorage.setItem('refresh_token', data.refresh_token);
                                            localStorage.setItem('id_token', data.id_token);
                                            TasksContext.getTasks();
                                            this.context.getSettings();

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
