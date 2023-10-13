import React, { Component } from "react";

import App2 from "./App2";

class App5 extends Component {
    constructor() {
        super();
        this.classComponentRef = React.createRef();
    }
    componentDidMount() {
        console.log(this.classComponentRef);
    }
    render() {
        return <App2 ref={this.classComponentRef} />;
    }
}

export default App5;