import React, {Component} from 'react';

const myHeaders = new Headers();
myHeaders.append("Content-Type", "text/plain");

myHeaders.append(
  "X-Mashape-Key",
  "l8lYKhEqKMmshGwKXzi1ElRhojGwp1Dn8YQjsnQRkDZQyPMIdV"
);

const myInit = {
  method: "GET",
  header: myHeaders,
  mode: "cors",
  cache: "default"
};
const myRequest = new Request("https://omgvamp-hearthstone-v1.p.mashape.com", myInit);

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      cardImg: []
    };
  }

  componentWillMount() {
    fetch(myRequest)
      .then(data => data.json())
      .then(data => {
        let card = data.results;
        console.log(card);
        this.setState({
          cardImg: card
        });
      });
  }

  render() {
    return (
      <div className="App">
      </div>
    );
  }
}