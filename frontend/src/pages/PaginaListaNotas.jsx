import React, { useState, useEffect } from "react";
import ListaInterna from "../components/ListaInterna";
import AgregarBoton from "../components/AgregarBoton";
function PaginaListaNotas() {
  let [notes, setNotes] = useState([]);

  useEffect(() => {
    getNotes();
  }, []);

  let getNotes = async () => {
    let response = await fetch("/api/notas/");
    let data = await response.json();
    setNotes(data);
  };

  return (
    <div className="notes">
      <div className="notes-header">
        <h2 className="notes-title">&#9782; Notas</h2>
        <p className="notes-count">{notes.length}</p>
      </div>

      <div className="notes-list">
        {notes.map((note, index) => (
          <ListaInterna key={index} note={note} />
        ))}
      </div>
      <AgregarBoton />
    </div>
  );
}

export default PaginaListaNotas;
