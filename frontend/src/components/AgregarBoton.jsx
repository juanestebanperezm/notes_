import React from "react";
import { Link } from "react-router-dom";
import { ReactComponent as AddIcon } from "../assets/add.svg";

function AgregarBoton() {
  return (
    <Link to="/api/notas/new" className="floating-button">
      <AddIcon />
    </Link>
  );
}

export default AgregarBoton;
