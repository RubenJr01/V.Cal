document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector("[data-nav-toggle]");
  const menu = document.querySelector("[data-nav-menu]");

  if (!toggle || !menu) {
    return;
  }

  const closeMenu = () => menu.classList.remove("is-open");

  toggle.addEventListener("click", () => {
    menu.classList.toggle("is-open");
    toggle.classList.toggle("is-active");
  });

  menu.addEventListener("click", (event) => {
    if (event.target instanceof HTMLElement && event.target.matches("a.nav-link")) {
      closeMenu();
      toggle.classList.remove("is-active");
    }
  });

  document.addEventListener("keyup", (event) => {
    if (event.key === "Escape") {
      closeMenu();
      toggle.classList.remove("is-active");
    }
  });
});
