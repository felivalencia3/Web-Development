import React from 'react';
import Clock from "./Clock";
import Greeting from "./Greeting";
import LoginControl from "./LoginControl";

export default class App extends React.Component {

    render() {
        const app = <div><Clock/><LoginControl/></div>
        return app
    }
}