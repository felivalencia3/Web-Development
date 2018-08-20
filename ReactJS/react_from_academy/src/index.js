import React from 'react'
import ReactDOM from 'react-dom';

class ReactCompo extends React.Component {
    render() {
        return(
            <blockquote>
                <p>
                    What is important now is to recover our senses.
                </p>
                <cite>
                    <a target="_blank"
                       href="https://en.wikipedia.org/wiki/Susan_Sontag">
                        Susan Sontag
                    </a>
                </cite>
            </blockquote>
        );
    }
}
ReactDOM.render(<ReactCompo/>, document.getElementById('app'));