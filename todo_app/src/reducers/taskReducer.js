const initState = {
    todos: [
        { task_name: 'feed fish', due_date: '10/23/2019', id: 1 },
        { task_name: 'take out trash', due_date: '12/06/2019', id: 2 },
        { task_name: 'get milk', due_date: '13/07/2019', id: 3 },
    ],
};

const taskReducer = (state = initState, action) => {
    return state;
};

export default taskReducer;

