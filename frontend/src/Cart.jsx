import React, { useState, useEffect } from "react";
import useAppContext from "./hooks/useAppContext.jsx";

const Cart = () => {
  const { cart, setCart, isLoading } = useAppContext();

  const handleRemoveFromCart = (index) => {
    const updatedCart = [...cart];
    updatedCart.splice(index, 1);
    setCart(updatedCart);
  };

  const handleCheckout = async () => {
    try {
      const response = await fetch("/receipt", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ cart }),
      });

      if (response.ok) {
        setShowToast(true);
        setTimeout(() => setShowToast(false), 3000);
        setCart([]);
      } else {
        // Handle error
      }
    } catch (error) {
      console.error("Error sending receipt:", error);
    }
  };

  return (
    <>
      <h1 className="text-3xl font-bold mb-20">Cart Summary</h1>
      {isLoading ? (
        <div className="flex justify-center">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900"></div>
        </div>
      ) : (
        <div className="flex flex-col">
          {cart &&
            cart.length !== 0 &&
            cart.map((item, index) => (
              <div
                className="flex flex-row justify-between mb-12 w-full"
                key={index}
              >
                <div className="w-16 h-16">
                  <img
                    src={item.productImage}
                    className="h-full w-full object-cover rounded mr-8"
                  ></img>
                </div>
                <div className="flex flex-col items-end">
                  <h1 className="text-lg">{item.productTitle}</h1>
                  <p>{item.productPrice}</p>
                </div>
              </div>
            ))}
        </div>
      )}
    </>
  );
};

export default Cart;
