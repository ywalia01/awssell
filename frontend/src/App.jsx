import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "react-toastify/dist/ReactToastify.css";
import { AppProvider } from "./context/AppProvider.jsx";
import { ToastContainer } from "react-toastify";
import Home from "./Home.jsx";
import Cart from "./Cart.jsx";

function App() {
  return (
    <BrowserRouter>
      <ToastContainer
        position="top-right"
        autoClose={5000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
      />
      <AppProvider>
        <div className="flex-col min-h-screen h-screen min-w-full w-full">
          <Routes>
            <Route exact path="/" element={<Home />} />
            <Route exact path="/cart" element={<Cart />} />
          </Routes>
        </div>
        <ToastContainer />
      </AppProvider>
      <ToastContainer />
    </BrowserRouter>
  );
}

export default App;
