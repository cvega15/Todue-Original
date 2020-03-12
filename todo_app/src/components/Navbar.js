import React from 'react';
import { NavLink } from 'react-router-dom';

class Navbar extends React.Component {

    render(){
        return(
            <div className='navbar' >
                <NavLink to='/home' className='navlink'>
                    <svg className="icon" xmlns="http://www.w3.org/2000/svg" width="6.5vh" height="6.5vh" viewBox="0 0 24 24"><path fill="none" d="M0 0h24v24H0V0z"/><path d="M12 5.69l5 4.5V18h-2v-6H9v6H7v-7.81l5-4.5M12 3L2 12h3v8h6v-6h2v6h6v-8h3L12 3z"/></svg>
                </NavLink>

                <NavLink to='/settings' className='navlink' >
                    <svg className="icon" xmlns="http://www.w3.org/2000/svg" width="6.5vh" height="6.5vh" viewBox="0 0 24 24"><path fill="none" d="M0 0h24v24H0V0z"/><path d="M12 6c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2m0 9c2.7 0 5.8 1.29 6 2v1H6v-.99c.2-.72 3.3-2.01 6-2.01m0-11C9.79 4 8 5.79 8 8s1.79 4 4 4 4-1.79 4-4-1.79-4-4-4zm0 9c-2.67 0-8 1.34-8 4v3h16v-3c0-2.66-5.33-4-8-4z"/></svg>
                </NavLink>
            </div>
        );
    };
};

export default Navbar