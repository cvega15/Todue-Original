import React, { createContext, Component } from 'react';

export const ModalContext = createContext();

class ModalContextProvider extends Component {
    state = {
        isShowing: false,
        task_data: null,
    };

    toggleModal = (task_data) => {
        this.setState({ task_data: task_data });
        if(this.state.isShowing === false){
            this.setState({ isShowing: true });
        }else{
            this.setState({ isShowing: false });
        }; 
    };

    render() {
        return ( 
            <ModalContext.Provider value={{...this.state, toggleModal: this.toggleModal}}>
                {this.props.children}
            </ModalContext.Provider>
        );
    };
};

export default ModalContextProvider;