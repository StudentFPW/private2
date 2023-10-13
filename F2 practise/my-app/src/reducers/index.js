import { combineReducers } from "redux";
import changeFramework from "./frameworks";
import changeLibrary from "./libraries";

export default combineReducers({
    changeFramework,
    changeLibrary
});