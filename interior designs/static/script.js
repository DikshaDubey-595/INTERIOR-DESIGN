// Smooth page load
document.addEventListener("DOMContentLoaded", () => {
    document.body.style.opacity = "0";
    document.body.style.transition = "1s";
    setTimeout(() => {
        document.body.style.opacity = "1";
    }, 100);
});

// Button click effect
document.querySelectorAll("button").forEach(btn => {
    btn.addEventListener("click", () => {
        btn.style.transform = "scale(0.95)";
        setTimeout(() => {
            btn.style.transform = "scale(1)";
        }, 150);
    });
});

// Form submit alert
document.querySelectorAll("form").forEach(form => {
    form.addEventListener("submit", function(e){
        e.preventDefault();
        alert("✅ Message sent successfully!");
        form.reset();
    });
});

// Gallery lightbox
document.querySelectorAll(".gallery img, .item img").forEach(img => {
    img.addEventListener("click", () => {

        let popup = document.createElement("div");
        popup.style.position = "fixed";
        popup.style.top = "0";
        popup.style.left = "0";
        popup.style.width = "100%";
        popup.style.height = "100%";
        popup.style.background = "rgba(0,0,0,0.9)";
        popup.style.display = "flex";
        popup.style.justifyContent = "center";
        popup.style.alignItems = "center";
        popup.style.zIndex = "9999";

        let newImg = document.createElement("img");
        newImg.src = img.src;
        newImg.style.maxWidth = "90%";
        newImg.style.maxHeight = "90%";
        newImg.style.borderRadius = "10px";

        popup.appendChild(newImg);
        document.body.appendChild(popup);

        popup.addEventListener("click", () => {
            popup.remove();
        });

    });
});

// Scroll animation
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if(entry.isIntersecting){
            entry.target.style.opacity = 1;
            entry.target.style.transform = "translateY(0)";
        }
    });
});

document.querySelectorAll(".card, .item, .info-card").forEach(el => {
    el.style.opacity = 0;
    el.style.transform = "translateY(40px)";
    el.style.transition = "0.6s";
    observer.observe(el);
});

document.addEventListener("DOMContentLoaded", function () {

    const burger = document.getElementById("burger");
    const navLinks = document.getElementById("navLinks");

    burger.addEventListener("click", function () {
        navLinks.classList.toggle("active");
    });

});

document.querySelectorAll(".nav-links a").forEach(link => {
    link.addEventListener("click", () => {
        navLinks.classList.remove("active");
    });
});