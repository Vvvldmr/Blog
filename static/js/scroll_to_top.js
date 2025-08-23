const ScrollBtn = document.getElementById("scrollToTopBtn");

ScrollBtn.addEventListener("click", () => {
    window.scrollTo({
        top: 0
    })
})

window.addEventListener("scroll", () => {
    if (window.scrollY > 300) {
        ScrollBtn.classList.add("show");
    }   else {
        ScrollBtn.classList.remove("show");
    }
})