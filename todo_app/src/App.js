import React from 'react';
import Header from './components/Header';
import TasksArea from './components/TasksArea';
import './AppStyles.css';

class App extends React.Component {

    constructor(){
        super();
        this.state = {
            showing_modal: false
        };
        this.show_modal = this.show_modal.bind(this);
    };

    show_modal(){
        if(this.state.showing_modal === false){
            this.setState({
                showing_modal: true
            });
        }else{
            this.setState({
                showing_modal: false
            });
        };
    };

    render(){
       
        return (
            <div className="everything">
                <Header show_modal={this.show_modal} />
                <TasksArea showing_modal={this.state.showing_modal} show_modal={this.show_modal} />
            </div>
        );
    };
};

export default App;
