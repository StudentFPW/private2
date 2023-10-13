import React from 'react';
import '../styles/Main.css';

function Main(props) {
    let [count, setNewCount] = React.useState(0);

    const handleClick = () => {
        setNewCount(count++)
    };

    return (
        <main>
            <h1>Hello World!</h1>
            <button className={ 'btn' } onClick={ handleClick }>
                { props.buttonName } = { count }
            </button>
        </main>
    );
};
export default Main;
