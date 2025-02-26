document.querySelector(".hamburger").addEventListener("click", function(event) {
    event.stopPropagation();
    document.querySelector(".menu").classList.toggle("open");
});

document.addEventListener("click", function(event) {
    const menu = document.querySelector(".menu");
    if (!menu.contains(event.target)) {
        menu.classList.remove("open");
    }
});