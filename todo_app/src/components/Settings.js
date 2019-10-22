import React from 'react';
import Header from './Header';
import { UserContext } from '../contexts/UserContext';
import SignIn from './SignIn';

class Settings extends React.Component {

    static contextType = UserContext;

    render(){

        return (
            <div className="settings">
                <Header title="settings"/>
                <div className="settings area">
                    <h3>account</h3>
                    <SignIn />
                    <h3>light mode</h3>
                    <input type="checkbox" defaultChecked={this.context.light_mode} onChange={this.context.toggleDarkMode} />
                    <h3>24 hour clock</h3>
                    <input type="checkbox" defaultChecked={this.context.clock_mode} onChange={this.context.toggleClockMode} />
                    <h3>is synced?</h3>
                </div>
            </div>
        );
    };
};

export default Settings;
