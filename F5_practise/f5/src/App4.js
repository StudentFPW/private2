import React, { Component } from "react";

class App4 extends Component {
    constructor() {
        super();
        this.domNodeRef = React.createRef();
    }
    componentDidMount() {
        console.log(this.domNodeRef);
    }
    render() {
        return <div ref={this.domNodeRef}>Hello World</div>;
    }
}

export default App4;