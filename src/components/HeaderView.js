import React, { Component } from 'react';

class WinLossIndicator extends Component {

  headerBar(){
    return (
      <div className="navbar navbar-default navbar-fixed-top">
        <div className="container">

          <div className="navbar-header">
            <a title="New Game" href="../" className="navbar-brand">Ahorcado UTN </a>
          </div>

          <div className="navbar-collapse collapse" id="navbar-main">
            <ul className="nav navbar-nav navbar-right">
              <li><i className="glyphicon glyphicon-thumbs-up"/> <span title="Games Won" className="badge">{this.props.won}</span></li>
              <li><i className="glyphicon glyphicon-thumbs-down"/> <span title="Games Lost" className="badge">{this.props.lost}</span></li>
            </ul>
          </div>

        </div>
      </div>);
  }

  render() {
    let statusMessage = null;
    if (this.props.gameStatus === -1){
      statusMessage =  <div className="alert alert-danger"> <strong>Lo siento!</strong> Has perdido. <strong>Inténtalo de nuevo, iniciando un nuevo juego. </strong> </div>;
    }
    else if (this.props.gameStatus === 1){
      statusMessage = <div className="alert alert-success"> <strong> Felicitaciones! </strong> Ganaste! </div>;
    }
    else{
      statusMessage = null
    }

    return (

      <div className="WinLossIndicator">
        {this.headerBar()}
        {statusMessage}
      </div>
    );
  }
}

export default WinLossIndicator;
