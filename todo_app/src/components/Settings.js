import React from 'react';
import Header from './Header';

class Settings extends React.Component {

    render(){
       
        return (
            <div className="settings">
                <Header title="settings"/>
                <div className="settings area">
                    <h3>log in</h3>
                    <h3>change theme</h3>
                    <h3>change timezone</h3>
                    <h3>change clock mode</h3>
                </div>
            </div>
        );
    };
};

export default Settings;
