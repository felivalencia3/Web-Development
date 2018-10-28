import React from 'react';
import "./index.css";
import axios from 'axios';
export default class App1 extends React.Component {
    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.input = React.createRef();
    }

    handleSubmit(event) {
        axios.get("http://192.168.0.3:8081/select?id="+this.input.current.value)
            .then(res => {
                const person = res.data;
                this.setState({person});
                console.log(this.state);

            });

        event.preventDefault();
    }

    render() {
        return (
            <div>
            <form onSubmit={this.handleSubmit}>
                <label id="label">
                    ID:
                    <input type="text" ref={this.input} />
                </label>
                <input id="input" type="submit" value="Submit" />
                <b>{this.state ? (<h1>Name: {this.state.person.name}</h1>) : (<p style={{display: 'none'}}>Waiting...</p>)}</b>
                <b>{this.state ? (<h1>Age: {this.state.person.age}</h1>) : (<p style={{display: 'none'}}>Waiting...</p>)}</b>
                <b>{this.state ? (<h1>City: {this.state.person.city}</h1>) : (<p style={{display: 'none'}}>Waiting...</p>)}</b>
            </form>
            </div>

        );
    }
}