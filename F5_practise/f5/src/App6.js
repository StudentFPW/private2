import React from "react";

function logProps(Component) {

    class LogProps extends React.Component {
        componentDidUpdate(prevProps) {
            console.log('old props:', prevProps);
            console.log('new props:', this.props);
        }
        render() {
            const { forwardedRef, ...rest } = this.props;

            // Передаём в качестве рефа проп "forwardedRef"
            return <Component ref={forwardedRef} {...rest} />;
        }
    }

    const WrappedComponent = React.forwardRef(
        function myFunction(props, ref) {
            return <LogProps {...props} forwardedRef={ref} />;
        }
    );

    return WrappedComponent
}