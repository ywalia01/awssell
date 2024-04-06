import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import useAppContext from "./hooks/useAppContext";

const Home = () => {
  const { products, setProducts, isLoading, setIsLoading, cart, setCart } =
    useAppContext();
  const navigate = useNavigate();

  // useEffect(() => {
  //   fetchProducts();
  // }, []);

  const fetchProducts = async () => {
    try {
      const response = await fetch("/listproducts");
      const data = await response.json();
      setProducts(data);
      setIsLoading(false);
    } catch (error) {
      console.error("Error fetching products:", error);
      setIsLoading(false);
    }
  };

  const handleAddToCart = (product) => {
    const updatedCart = [...cart, { ...product }];
    setCart(updatedCart);
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
    <div className="container mx-auto py-8 h-full w-full">
      <div className="flex justify-between px-4">
        <h1 className="text-3xl font-bold mb-4">Products</h1>
        <h1 onClick={handleViewCartClick} className="text-3xl font-bold mb-4">
          View Cart
        </h1>
      </div>
      {isLoading ? (
        <div className="flex justify-center">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900"></div>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 mt-20">
          {products.map((product, index) => (
            <div
              className="relative flex w-72 flex-col rounded-xl bg-white bg-clip-border text-gray-700 shadow-md"
              key={index}
            >
              <div className="relative mx-4 mt-4 h-80 overflow-hidden rounded-xl bg-white bg-clip-border text-gray-700">
                <img
                  src={product.productImage}
                  className="h-full w-full object-cover"
                />
              </div>
              <div className="p-6">
                <div className="mb-2 flex items-center justify-between">
                  <p className="block font-sans text-base font-medium leading-relaxed text-blue-gray-900 antialiased">
                    {product.productTitle}
                  </p>
                  <p className="block font-sans text-base font-medium leading-relaxed text-blue-gray-900 antialiased">
                    ${product.productPrice}
                  </p>
                </div>
                <p className="block font-sans text-sm font-normal leading-normal text-gray-700 antialiased opacity-75">
                  {product.productDescription}
                </p>
              </div>
              <div className="p-6 pt-0">
                <button
                  className="block w-full select-none rounded-lg bg-blue-gray-900/10 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-blue-gray-900 transition-all hover:scale-105 focus:scale-105 focus:opacity-[0.85] active:scale-100 active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
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
