import React from 'react';
import Navbar from './components/Navbar';
import Settings from './components/Settings';
import Home from './components/Home';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

class App extends React.Component {

    render(){
       
        return (
            <BrowserRouter> 
                <div className="App">
                    <Switch>
                        <Route exact path='/' component={Home} />
                        <Route exact path='/settings' component={Settings} />
                    </Switch>
                    <Navbar />
                </div>
            </BrowserRouter>
        );
    };
};

export default App; 
