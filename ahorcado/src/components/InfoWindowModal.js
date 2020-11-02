import React, { Component } from 'react';
import ReactModal from 'react-modal';

class InfoWindowModal extends Component {

  constructor () {
    super();

    this.state = {
      showModal: false
    };

    this.handleOpenModal = this.handleOpenModal.bind(this);
    this.handleCloseModal = this.handleCloseModal.bind(this);
  }

  handleOpenModal () {
    this.setState({ showModal: true });
  }

  handleCloseModal () {
    this.setState({ showModal: false });
  }

  render () {
    return (
        <ReactModal
           isOpen={this.state.showModal}
           contentLabel="Info"
           closeTimeoutMS={200}>

            <div className="modal-dialog">
              <div className="modal-content">

                <div className="modal-header">
                  <h4 className="modal-title">Hangman</h4>
                </div>

                <div className="modal-body">
                  <p>La palabra a adivinar está representada por una fila de guiones, 
                    que representan cada letra de la palabra. Si el jugador que va a adivinar, 
                    sugiere una letra que aparece en la palabra, ésta aparecerá en todas sus posiciones 
                    correctas. Si la letra sugerida no aparece en la palabra, se dibujará un elemento 
                    de una figura de palo de hombre colgado como marca de recuento.</p>
                   
                  <p>Si despues de 10 intentos la palabra está incompleta, el juego se da como perdido. En caso
                    contrario, el juego se dará como ganado.</p>

                  <p> P.D. <strong> El teclado también puede ser utilizado como un método de entrada válido </strong> </p>
                </div>
                <div className="modal-footer">
                  <button type="button" className="btn btn-default" onClick={this.handleCloseModal}>Volver al juego</button>
                </div>
              </div>
            </div>

        </ReactModal>
    );
  }
}

export default InfoWindowModal;
