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