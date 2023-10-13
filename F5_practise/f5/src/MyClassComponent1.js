import React from "react";

class MyClassComponent1 extends React.Component {
    constructor(props) {
        super(props);
        this.myRef = React.createRef();
    }

    render() {
        return <div ref={this.myRef} />;
    }
}

export default MyClassComponent1;