const initState = {
    showing: false
};

const modalReducer = (state = initState, action) => {
    if(action.type === SHOW_MODAL){
        state.showing = true;
    }
    return state;
};

export default modalReducer;
