import React from 'react';
import Header from './Header';
import { UserContext } from '../contexts/UserContext';
import SignIn from './SignIn';
import Navbar from './Navbar';

class Settings extends React.Component {

    static contextType = UserContext;

    render(){
        let is_synced
        if(this.context.logged_in && !this.context.ticket.length){
            is_synced = <h3 style={{color: 'green'}}>synced with database!</h3>
        }else{
            is_synced = <h3 style={{color: 'red'}}>not synced with database</h3>
        };

        return (
            <div className="settings">
                <Header title="settings"/>
                    <div className="settings area">
                        <h3>account</h3>
                        <SignIn getSettings={this.getSettings}/>
                        <h3>light mode</h3>
                        <input type="checkbox" checked={this.context.light_mode} onChange={this.context.toggleDarkMode} />
                        <h3>24 hour clock</h3>
                        <input type="checkbox" checked={this.context.clock_mode} onChange={this.context.toggleClockMode} />
                        {is_synced}
                    </div>
                <Navbar />
            </div>
        );
    };
};

export default Settings;
