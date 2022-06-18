import React, { useState, useEffect } from "react";
import ListaInterna from "../components/ListaInterna";

function PaginaListaNotas() {
  let [notas, setNotas] = useState([]);

  useEffect(() => {
    obtenerNotas();
  }, []);

  let obtenerNotas = async () => {
    let r = await fetch("/notas/");
    let datos = await r.json();
    console.log(datos)
    setNotas(datos);
  };

  return (
    <div>
      {!notas?<h1>No hay notas disponibles</h1>:notas.map(  (nota,index) => (  
        <ListaInterna  key={index} nota={nota} />
       ) )}
    </div>
  );
}

export default PaginaListaNotas;
