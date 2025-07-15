// Function to add or remove quantity and update localStorage
function changeQuantity(name, price, delta) {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];

  // Find item in cart
  let index = cart.findIndex(item => item.name === name);
  if (index !== -1) {
    cart[index].quantity += delta;
    if (cart[index].quantity <= 0) {
      cart.splice(index, 1); // remove item if quantity is zero or less
    }
  } else if (delta > 0) {
    cart.push({ name: name, price: price, quantity: 1 });
  }

  localStorage.setItem("cart", JSON.stringify(cart));
  updateQtyDisplay(name);
}

// Function to show the quantity on the screen
function updateQtyDisplay(name) {
  const cart = JSON.parse(localStorage.getItem("cart")) || [];
  const item = cart.find(i => i.name === name);
  const qty = item ? item.quantity : 0;

  const elem = document.getElementById("qty-" + name);
  if (elem) {
    elem.innerText = qty;
  }
}

// On page load, restore quantities for all items on the page
window.onload = function () {
  const cart = JSON.parse(localStorage.getItem("cart")) || [];
  for (const item of cart) {
    updateQtyDisplay(item.name);
  }
};
