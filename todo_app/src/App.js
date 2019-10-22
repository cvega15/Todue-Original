import React from 'react';
import Navbar from './components/Navbar';
import Settings from './components/Settings';
import Home from './components/Home';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import ModalContextProvider from './contexts/ModalContext';
import TasksContextProvider from './contexts/TasksContext';
import UserContext from './contexts/UserContext';

class App extends React.Component {
    
    render(){
       
        return (
            <UserContext>
                <ModalContextProvider>
                    <TasksContextProvider>
                        <BrowserRouter>
                            <div className="app">
                                <Switch>
                                    <Route exact path='/' component={Home} />
                                    <Route exact path='/settings' component={Settings} />
                                </Switch>
                                <Navbar />
                            </div>
                        </BrowserRouter>
                    </TasksContextProvider>
                </ModalContextProvider>
            </UserContext>
        );
    };
};

export default App; 
