import React from "react";

export default class App2 extends React.Component {
    constructor(props) {
        super(props);
        this.myRef = React.createRef();
        this.focusInput = this.focusInput.bind(this);
    }
    focusInput() {
        this.myRef.current.focus();
    }
    render() {
        return (
            <div>
                <input type="text" ref={this.myRef} />
                <button onClick={this.focusInput}>Focus the input</button>
            </div>
        )
    }
}