// Site header
const siteHeaderToggleMenuButton = document.querySelector(
  ".site-header-toggle-menu-button"
);
const siteHeaderMenu = document.querySelector(".site-header-menu");
siteHeaderToggleMenuButton.addEventListener("click", () => {
  siteHeaderMenu.classList.toggle("is-active");
});

// Subscription form
const subscriptionForm = document.querySelector(".subscription-form");

function foodSetValidation(event) {
  const checkedFoodSet = document.querySelectorAll(
    'input[name="food_set"]:checked'
  );
  if (checkedFoodSet.length === 0) {
    event.preventDefault();
    alert("Choose at least 1 menu");
  }
}

if (!!subscriptionForm) {
  subscriptionForm.addEventListener("submit", foodSetValidation);
}
