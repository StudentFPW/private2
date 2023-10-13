import React from 'react';

class Clock extends React.Component {
    constructor(props) {
        super(props);
        this.state = { date: new Date() };
    }

    // в методе componentDidMount (т. е. при монтировании компонента) устанавливает таймер,
    // который раз в секунду будет вызывать метод tick;
    componentDidMount() {
        this.timerID = setInterval(
            () => this.tick(),
            1000
        );
    }

    // в методе componentWillUnmount сбрасывает таймер с помощью стандартной функции
    // clearInterval (это нужно делать, чтобы случайно не потратить пул таймеров браузера);
    componentWillUnmount() {
        clearInterval(this.timerID);
    }

    // в методе tick обновляет время в состоянии компонента;
    tick() {
        this.setState({
            date: new Date()
        });
    }

    render() {
        return (
            <div>
                <h1>Hello, world!</h1>
                <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
            </div>
        );
    }
}

export default Clock;