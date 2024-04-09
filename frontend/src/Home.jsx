import React, { useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import useAppContext from "./hooks/useAppContext";
import { toast, Bounce } from "react-toastify";

const Home = () => {
  const { products, setProducts, isLoading, setIsLoading, cart, setCart } =
    useAppContext();
  const navigate = useNavigate();

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    setIsLoading(true);
    const headers = {
      "Content-Type": "application/json",
    };

    await axios
      .get(
        "https://ni7nmnnbw9.execute-api.us-east-1.amazonaws.com/prod/list",
        headers
      )
      .then((res) => {
        console.log(res);
        setProducts(res.data.products);
      })
      .catch((err) => console.log(err))
      .finally(setIsLoading(false));
  };

  const handleAddToCart = (product) => {
    const updatedCart = [...cart, { ...product, quantity: 1 }];
    setCart(updatedCart);
    toast.success("Product Added to Cart", {
      position: "top-center",
      autoClose: 1000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
      theme: "light",
      transition: Bounce,
    });
  };

  const handleViewCartClick = () => {
    navigate("/cart");
  };

  useEffect(() => {
    if (cart) {
      console.log(cart);
    }
  }, [cart]);

  return (
    <div className="container mx-auto pt-8 pb-24 mb-24 h-full w-full">
      <div className="flex align-center items-center justify-between mb-8">
        <h1 className="text-3xl font-bold">Products</h1>
        <h1 className="text-3xl font-bold">AWSSell</h1>
        <button
          onClick={handleViewCartClick}
          className="btn text-lg font-bold cursor-pointer text-white text-center bg-slate-800"
        >
          View Cart
        </button>
      </div>
      {isLoading ? (
        <div className="flex justify-center text-white">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900"></div>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 mt-20 pb-20">
          {products.map((product, index) => (
            <div
              className="flex flex-col justify-between relative w-72 rounded-xl bg-white bg-clip-border text-gray-700 shadow-md"
              key={index}
            >
              <div className="relative mx-4 mt-4 h-56 overflow-hidden rounded-xl bg-white bg-clip-border text-gray-700">
                <img
                  src={product.productImage}
                  className="h-full w-full object-cover"
                />
              </div>
              <div className="flex flex-col justify-betwen py-6 px-2 w-full">
                <div className="flex flex-row mb-2 items-center justify-center w-full">
                  <p className="block font-sans text-base font-medium leading-relaxed text-blue-gray-900 antialiased">
                    {product.productTitle}
                  </p>
                </div>
                <div className="flex flex-row items-center justify-center mb-2">
                  <p className="block font-sans text-base font-medium leading-relaxed text-blue-gray-900 antialiased">
                    $ {product.productPrice}
                  </p>
                </div>
                <p className="block font-sans text-sm font-normal leading-normal text-gray-700 antialiased opacity-75">
                  {product.productDescription}
                </p>
              </div>
              <div className="flex flex-col justify-between p-6 pt-0">
                <button
                  className="block w-full select-none rounded-lg bg-blue-gray-900/10 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-blue-gray-900 transition-all hover:scale-105 focus:scale-105 focus:opacity-[0.85] active:scale-100 active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none text-white"
                  type="button"
                  onClick={() => handleAddToCart(product)}
                >
                  Add to Cart
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Home;
