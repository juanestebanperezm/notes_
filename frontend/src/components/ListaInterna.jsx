import React from 'react'
import {Link} from "react-router-dom"

function ListaInterna({nota}) {
  return (
    <div>
        {nota.body}
    </div>
  )
}

export default ListaInterna