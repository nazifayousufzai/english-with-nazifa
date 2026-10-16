<<<<<<< HEAD
// English with Nazifa
// Website JavaScript

document.addEventListener("DOMContentLoaded", function () {

    // =========================
    // Contact Form
    // =========================

    const contactForm = document.querySelector(".contact-form");

    if (contactForm) {

        contactForm.addEventListener("submit", function (event) {

            event.preventDefault();

            alert("Thank you for contacting English with Nazifa! 🌸");

            contactForm.reset();

        });

    }


    // =========================
    // Course Buttons
    // =========================

    const courseButtons = document.querySelectorAll(".course-card a");

    courseButtons.forEach(function (button) {

        button.addEventListener("click", function (event) {

            event.preventDefault();

            alert("Course details will be available soon. 📚");

        });

    });


    // =========================
    // Mobile Menu
    // =========================

    const menuToggle = document.querySelector(".menu-toggle");
    const navLinks = document.querySelector(".nav-links");

    if (menuToggle && navLinks) {

        menuToggle.addEventListener("click", function () {

            navLinks.classList.toggle("active");

        });

    }


    // =========================
    // Registration Form
    // =========================

    const registrationForm = document.querySelector(".registration-form");
    const registrationMessage = document.querySelector("#registration-message");

    if (registrationForm) {

        registrationForm.addEventListener("submit", async function (event) {

            event.preventDefault();

            const submitButton = registrationForm.querySelector("button[type='submit']");

            submitButton.disabled = true;
            submitButton.textContent = "Sending...";

            try {

                const response = await fetch(registrationForm.action, {
                    method: "POST",
                    body: new FormData(registrationForm),
                    headers: {
                        "Accept": "application/json"
                    }
                });

                if (response.ok) {

                    registrationForm.reset();

                    registrationMessage.style.display = "block";

                    submitButton.textContent = "Registration Sent ✓";

                    registrationMessage.scrollIntoView({
                        behavior: "smooth",
                        block: "center"
                    });

                } else {

                    alert("Something went wrong. Please try again.");

                    submitButton.disabled = false;
                    submitButton.textContent = "Register Now";

                }

            } catch (error) {

                alert("Please check your internet connection and try again.");

                submitButton.disabled = false;
                submitButton.textContent = "Register Now";

            }

        });

    }

});
=======
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
>>>>>>> 2a3b2ddaa96304e1f82bce9a27d90ed767779574
