import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

function PaginaNotas({ match }) {
  let params = useParams();
  let [nota, setNotas] = useState(null);

  useEffect(() => {
    obtenerNota();
  },[params]);

  let obtenerNota = async () => {
    let r = await fetch(`/nota/${params.id}/`);
    let datos = await r.json();
    setNotas(datos);
  };

  return (
    <div>
      <p>{nota?.body}</p>
    </div>
  );
}

export default PaginaNotas;
