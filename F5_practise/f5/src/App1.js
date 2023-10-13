import React from 'react';

export default class App1 extends React.Component {
    constructor(props) {
        super(props);
        this.myRef = React.createRef();
    }
    componentDidMount() {
        // console.log(this.myRef)
        this.myRef.current.innerHTML = 'Hello refs'
    }
    render() {
        return <div ref={this.myRef}>Hello world</div>;
    }
}
