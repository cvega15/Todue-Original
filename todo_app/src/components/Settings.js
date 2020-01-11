import React from 'react';
import Header from './Header';
import { UserContext } from '../contexts/UserContext';
import SignIn from './SignIn';
import Navbar from './Navbar';

class Settings extends React.Component {

    static contextType = UserContext;

    render(){
        //console.log('settings rendering, logged in is: ' + this.context.logged_in.toString())
        //console.log('is logged in: ' + this.context.logged_in.toString())
        //console.log('ticket length: ' + this.context.ticket.length.toString())
        //console.log('is synced: ' + this.context.is_synced.toString())
        let is_synced
        
        console.log('sync status: ' + this.context.is_synced.toString())
        if(this.context.is_synced && !this.context.ticket.length && this.context.logged_in){
            is_synced = <h3 className="is-synced">synced with database!</h3>
        }else{
            is_synced = <h3 className="not-synced">not synced with database</h3>
        };

        return (
            <div className="settings">
                <Header title="settings"/>
                    <div className='settings-area'>
                        <br></br>
                        {is_synced}
                        <br></br>
                        <div className='setting'>
                            <label className='toggle-switch'>
                                <input className='setting-box' type="checkbox" checked={this.context.light_mode} onChange={this.context.toggleDarkMode} />
                                <div className='slider'></div>
                            </label>
                            <h3 className='setting-text'>light mode</h3>
                        </div>
                        <br></br>
                        <div className='setting'>
                            <label className='toggle-switch'>
                                <input className='setting-box' type="checkbox" checked={this.context.clock_mode} onChange={this.context.toggleClockMode} />
                                <div className='slider'></div>
                            </label>
                            <h3 className='setting-text'>24 hr clock mode</h3>
                        </div>
                        <br></br>
                        <SignIn getSettings={this.getSettings}/>
                    </div>
                <Navbar />
            </div>
        );
    };
};

export default Settings;
