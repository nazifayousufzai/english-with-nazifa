// English with Nazifa
// Website interactions

document.addEventListener("DOMContentLoaded", function () {

    // Contact form
    const form = document.querySelector(".contact-form");

    if (form) {
        form.addEventListener("submit", function (event) {
            event.preventDefault();

            alert("Thank you for contacting English with Nazifa! 🌸");

            form.reset();
        });
    }

    // Course buttons
    const courseButtons = document.querySelectorAll(".course-card a");

    courseButtons.forEach(function (button) {
        button.addEventListener("click", function (event) {
            event.preventDefault();

            alert("Course details will be available soon. 📚");
        });
    });

});
/* Mobile Menu */

.menu-toggle {
    display: none;
    background: #4f6df5;
    color: white;
    border: none;
    font-size: 24px;
    width: 45px;
    height: 45px;
    border-radius: 10px;
    cursor: pointer;
}

@media (max-width: 900px) {

    .navbar {
        position: relative;
    }

    .menu-toggle {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .nav-links {
        position: absolute;
        top: 76px;
        left: 20px;
        right: 20px;
        background: white;
        flex-direction: column;
        gap: 0;
        padding: 10px 0;
        border-radius: 15px;
        box-shadow: 0 15px 40px rgba(30, 50, 80, 0.15);
        display: none;
    }

    .nav-links.active {
        display: flex;
    }

    .nav-links li a {
        display: block;
        padding: 15px 20px;
    }

    .nav-button {
        display: none;
    }
}