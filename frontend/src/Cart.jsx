import React, { useState, useEffect } from "react";
import axios from "axios";
import useAppContext from "./hooks/useAppContext.jsx";
import { toast, Bounce } from "react-toastify";

const Cart = () => {
  const { cart, setCart, isLoading, setIsLoading } = useAppContext();
  const [receiptObj, setReceiptObj] = useState({});
  const [custEmail, setCustEmail] = useState("");

  const handleRemoveFromCart = (index) => {
    const updatedCart = [...cart];
    updatedCart.splice(index, 1);
    setCart(updatedCart);
  };

  const handleCheckout = async () => {
    setIsLoading(true);
    const finalReceipt = {
      customerEmail: custEmail,
      orderPlacedDate: "2024-04-08",
      orderPlacedTime: "20:56",
      discountRate: 10,
      taxPercentage: 15,
      products: cart,
    };
    setReceiptObj(finalReceipt);
    await axios
      .post(
        "https://ni7nmnnbw9.execute-api.us-east-1.amazonaws.com/prod/receipt",
        finalReceipt
      )
      .then((res) => {
        console.log(res);
        toast.success("Checkout Succesful, Email Sent!", {
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
        setCart([]);
      })
      .catch((err) => console.log(err))
      .finally(setIsLoading(false));
  };

  const handleQuantityChange = (index, delta) => {
    const updatedCart = [...cart];
    const item = updatedCart[index];
    item.quantity = (item.quantity || 1) + delta; // Ensure quantity is never less than 1
    if (item.quantity < 1) item.quantity = 1;
    setCart(updatedCart);
  };

  useEffect(() => {
    console.log("Cart changed: ", cart);
  }, [cart]);

  useEffect(() => {
    console.log("Final Receipt Object being sent: ", receiptObj);
  }, [receiptObj]);

  return (
    <div className="max-w-screen">
      <h1 className="text-3xl font-bold mb-20">Cart Summary</h1>
      {isLoading ? (
        <div className="flex justify-center">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900"></div>
        </div>
      ) : (
        <div className="flex flex-col">
          <div>
            {cart &&
              cart.length !== 0 &&
              cart.map((item, index) => (
                <div
                  className="flex flex-row justify-between items-center mb-6 min-w-full"
                  key={index}
                >
                  <div className="flex flex-row items-center justify-center w-24 h-24 mr-4 ">
                    <img
                      src={item.productImage}
                      className="h-24 object-cover rounded mr-8"
                    ></img>
                  </div>
                  <div className="flex flex-row mr-6 items-end justify-end">
                    <div className="flex flex-col justify-end justify-self-end">
                      <div className="flex flex-row justify-end items-end justify-self-end">
                        <h1 className="text-lg">{item.productTitle}</h1>
                      </div>
                      <div className="flex flex-row justify-end items-end">
                        <h2>
                          {"$ "}
                          {item.productPrice}
                        </h2>
                      </div>
                    </div>
                  </div>
                  <div className="flex items-center justify-end">
                    <button
                      className="btn"
                      onClick={() => handleQuantityChange(index, -1)}
                    >
                      -
                    </button>
                    <span className="mx-4">{item.quantity || 1}</span>{" "}
                    {/* Default quantity to 1 if undefined */}
                    <button
                      className="btn"
                      onClick={() => handleQuantityChange(index, +1)}
                    >
                      +
                    </button>
                  </div>
                </div>
              ))}
          </div>
          <div className="mb-8">
            <h1 className="text-lg">Discount Applied: 10%</h1>
          </div>
          <div className="mb-6">
            <input
              type="text"
              placeholder="johndoe@example.com"
              className="input input-bordered w-full max-w-xs"
              value={custEmail}
              onChange={(e) => setCustEmail(e.target.value)}
            />
          </div>
          <div>
            <button className="btn" onClick={handleCheckout}>
              Checkout
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Cart;
