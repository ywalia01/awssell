import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AppProvider } from "./context/AppProvider.jsx";
import Home from "./Home.jsx";
import Cart from "./Cart.jsx";

function App() {
  return (
    <BrowserRouter>
      <AppProvider>
        <div className="flex-col min-h-screen h-screen min-w-full">
          <Routes>
            <Route exact path="/" element={<Home />} />
            <Route exact path="/cart" element={<Cart />} />
          </Routes>
        </div>
      </AppProvider>
    </BrowserRouter>
  );
}

export default App;
