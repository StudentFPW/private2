const initialState = ["Redux", "React-redux"]

function changeLibrary(state = initialState, action) {
    switch (action.type) {
        case "ADD_LIBRARY":
            return [
                ...state,
                action.payload
            ]
        case "DELETE_LIBRARY":
            return state
        default:
            return state;
    }
};

export default changeLibrary;