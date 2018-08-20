import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
function Encrypt(str) {
    let converted = str.toLowerCase();
    converted = str.replace(/[a-z]/gi, function(char) {
        if (char === "z") {
            return "c"
        } else if (char === "y") {
            return "b"
        } else if(char === "x") {
            return "a"
        } else {
            return String.fromCharCode(char.charCodeAt() +3)
        }
    });
    let vowelchange = converted.replace(/[a|e|i|o|u]/gi,function(vowel) {
        if(vowel === "A"||vowel=== "a") {
            return 1
        } else if(vowel === "E"||vowel === "e") {
            return 2
        } else if (vowel === "I"||vowel === "i") {
            return 3
        } else if (vowel === "O" || vowel === "o") {
            return 4
        } else if (vowel === "U" || vowel === "u") {
            return 5
        }

    });
return vowelchange;
}
class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            data: 'Initial data...'
        }
        this.updateState = this.updateState.bind(this);
    };
    updateState(e) {
        this.setState({data: e.target.value});
    }
    render() {
        return (
            <div><div id="input">
                <input id="input1" type = "text" value = {this.state.data}
                       onChange = {this.updateState} />  </div>
<div id="text">
                <h4 id="reversed">{Encrypt(this.state.data.split("").reverse().join(""))}</h4></div>
            </div>
        );
    }
}
export default App;


