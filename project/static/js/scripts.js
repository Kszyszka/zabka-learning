document.addEventListener("DOMContentLoaded", function () {
    const loginButton = document.getElementById("login-button");
    const registerButton = document.getElementById("register-button");
    const loginForm = document.getElementById("login-form");
    const registerForm = document.getElementById("register-form");

    loginButton.addEventListener("click", function (event) {
        event.preventDefault();
        toggleForm(loginForm);
    });

    registerButton.addEventListener("click", function (event) {
        event.preventDefault();
        toggleForm(registerForm);
    });

    function toggleForm(form) {
        if (form.classList.contains("show")) {
            form.classList.remove("show");
        } else {
            hideAllForms();
            form.classList.add("show");
        }
    }

    function hideAllForms() {
        loginForm.classList.remove("show");
        registerForm.classList.remove("show");
    }
});

