import React, { Component } from 'react';
import ReactModal from 'react-modal';

class InfoWindowModal extends Component {
  constructor(props) {
    super(props);

    this.state = {
      showModal: false,
    };

    this.handleOpenModal = this.handleOpenModal.bind(this);
    this.handleCloseModal = this.handleCloseModal.bind(this);
    this.onConfirm = this.onConfirm.bind(this);

  }

  handleOpenModal () {
    this.setState({ showModal: true });
  }

  handleCloseModal () {
    this.setState({ showModal: false });
  }

  onConfirm(){
    this.props.onConfirm();
    this.handleCloseModal();
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
                       <h4 className="modal-title" id="myModalLabel">Confirmar nuevo juego</h4>
                   </div>

                   <div className="modal-body">
                       <p>Iniciar un nuevo juego mientras un juego está en progreso, hará que el juego actual resulte en una pérdida.</p>
                       <p>¿Desea continuar?</p>
                   </div>

                   <div className="modal-footer">
                       <button type="button" className="btn btn-default" data-dismiss="modal" onClick={this.handleCloseModal}>Ir Atrás</button>
                       <a className="btn btn-danger btn-ok" data-dismiss="modal" onClick={this.onConfirm}>Si, admito la derrota</a>
                   </div>
               </div>
           </div>

        </ReactModal>
    );
  }
}

export default InfoWindowModal;
