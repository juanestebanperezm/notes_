import "./App.css";
import Cabecera from "./components/Cabecera";
import PaginaListaNotas from "./pages/PaginaListaNotas";
import PaginaNotas from "./pages/PaginaNotas";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
function App() {
  return (
    <div className="App">
      <Cabecera />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<PaginaListaNotas />} />
          <Route path="/:id" element={<PaginaNotas />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
