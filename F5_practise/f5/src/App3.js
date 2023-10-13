import React from 'react';

class App3 extends React.Component {
    constructor() {
        super();
        this.animateRef = React.createRef();
        this.triggerAnimation = this.triggerAnimation.bind(this);
    }

    triggerAnimation() {
        this.animateRef.current.classList.add('animation_trigger');
    }

    render() {
        return (
            <div>
                <div className="animatedElementStyle" ref={this.animateRef}>
                    I am rendered !
                </div>
                <button onClick={this.triggerAnimation}>trigger animation</button>
            </div>
        );
    }
}

export default App3;