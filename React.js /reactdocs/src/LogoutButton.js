import React from 'react';
export default class LogoutButton extends React.Component{
    constructor(props) {
        super(props)
    }
    render() {
        return (
            <button onClick={this.props.onClick}>
                Logout
            </button>
        );
    }
}