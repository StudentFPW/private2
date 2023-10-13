import React, { Component } from "react";
import { connect } from "react-redux";
import "./App-redux.css"

class ReduxApp extends Component {
    addLib = () => {
        if (this.inputLibrary.value.length === 0) {
            return;
        } else {
            this.props.addLibrary(this.inputLibrary.value);
            this.inputLibrary.value = "";
        }
    }
    addFrame = () => {
        if (this.inputFramework.value.length === 0) {
            return;
        } else {
            this.props.addFramework(this.inputFramework.value);
            this.inputFramework.value = "";
        }
    }
    render() {
        console.log(this.props);
        return (
            <div>
                <input type="text" ref={(input) => { this.inputLibrary = input }} />
                <button onClick={this.addLib.bind(this)}>Button Library</button>

                <input type="text" ref={(input) => { this.inputFramework = input }} />
                <button onClick={this.addFrame.bind(this)}>Button Framework</button>

                <ul>
                    {this.props.library.map(item => {
                        return <li key={item}>{item}</li>
                    })}
                </ul>
                <ul>
                    {this.props.framework.map(item => {
                        return <li key={item}>{item}</li>
                    })}
                </ul>
            </div>
        )
    }
}

export default connect(
    // mapStateToProps
    state => ({
        library: state.changeLibrary,
        framework: state.changeFramework,
    }),

    // mapDispatchToProps
    dispatch => ({
        addLibrary: (elem) => {
            dispatch({
                type: "ADD_LIBRARY",
                payload: elem
            })
        },
        addFramework: (elem) => {
            dispatch({
                type: "ADD_FRAMEWORK",
                payload: elem
            })
        }
    })
)(ReduxApp);