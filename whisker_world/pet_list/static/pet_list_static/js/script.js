let mobileNav = document.querySelector(".hamburger");
let navbar = document.querySelector(".menubar");

let toggleNav = () => {
  navbar.classList.toggle("active");
  mobileNav.classList.toggle("hamburger-active");
};

mobileNav.addEventListener("click", () => toggleNav());