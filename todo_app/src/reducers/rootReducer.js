import modalReducer from './modalReducer';
import taskReducer from './taskReducer';
import { combineReducers } from 'redux';

const rootReducer = combineReducers({
    modal: modalReducer,
    task: taskReducer
});

export default rootReducer;
