import React from 'react';
import { ModalContext } from '../contexts/ModalContext';

class Header extends React.Component {

    static contextType = ModalContext;

    render(){
        const { toggleModal } = this.context;
        var title = this.props.title;
        if(title === 'users tasks'){
            return(
                <div className='header'>
                    <h2>{ title }</h2>
                    <div className="add-button">
                        <svg xmlns="http://www.w3.org/2000/svg" className="icon" color="white" onClick={ () => toggleModal(null) } width="7.8vh" height="7.8vh" viewBox="0 0 24 24"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/><path d="M0 0h24v24H0z" fill="none"/></svg>         

                    </div>
                </div>
            );
        }else{
            return(
                <div className='header'>
                    
                    <h2>{ title }</h2>
                </div>
            );
        }
    };
};

export default Header;
