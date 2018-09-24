import React from 'react';
import {UserGreet} from "./UserGreet";
import GuestGreet from "./GuestGreet";
export default class Greeting extends React.Component {
    render() {
        const isLoggedIn = this.props.isLoggedIn;
        if(isLoggedIn) {
            return <UserGreet/>
        } else {
            return <GuestGreet/>
        }
    }
}