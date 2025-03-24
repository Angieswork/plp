// Event Listener: Toggle Password Visibility
document.getElementById("togglePassword").addEventListener("click", function() {
    let passwordField = document.getElementById("password");
    if (passwordField.type === "password") {
        passwordField.type = "text";
        this.textContent = "Hide";
    } else {
        passwordField.type = "password";
        this.textContent = "Show";
    }
});
// Toggle background color
const toggleBtn = document.getElementById("toggleBtn");
let isDark = false;

toggleBtn.addEventListener("click", () => {
    document.body.style.backgroundColor = isDark ? "white" : "lightgray";
    isDark = !isDark;
});

// Adjust text size with slider
const textSlider = document.getElementById("textSlider");
const text = document.getElementById("text");

textSlider.addEventListener("input", () => {
    text.style.fontSize = textSlider.value + "px";
});

// Modal functionality
const openModal = document.getElementById("openModal");
const closeModal = document.getElementById("closeModal");
const modal = document.getElementById("modal");

openModal.addEventListener("click", () => {
    modal.style.display = "block";
});

closeModal.addEventListener("click", () => {
    modal.style.display = "none";
});

window.addEventListener("click", (event) => {
    if (event.target === modal) {
        modal.style.display = "none";
    }
});

// Form validation
const form = document.getElementById("myForm");

form.addEventListener("submit", (event) => {
    let isValid = true;

    // Name validation
    const nameInput = document.getElementById("name");
    const nameError = document.getElementById("nameError");
    if (nameInput.value.length < 3) {
        nameError.textContent = "Name must be at least 3 characters.";
        isValid = false;
    } else {
        nameError.textContent = "";
    }

    // Email validation
    const emailInput = document.getElementById("email");
    const emailError = document.getElementById("emailError");
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(emailInput.value)) {
        emailError.textContent = "Enter a valid email.";
        isValid = false;
    } else {
        emailError.textContent = "";
    }

    // Password validation
    const passwordInput = document.getElementById("password");
    const passwordError = document.getElementById("passwordError");
    const passwordRegex = /^(?=.*[A-Z])(?=.*\d).{8,}$/;
    if (!passwordRegex.test(passwordInput.value)) {
        passwordError.textContent = "Password must be at least 8 characters, with one uppercase letter and one number.";
        isValid = false;
    } else {
        passwordError.textContent = "";
    }

    // Prevent form submission if validation fails
    if (!isValid) {
        event.preventDefault();
    }
});

// Dropdown menu functionality
const dropdown = document.getElementById("dropdown");
const dropdownMessage = document.getElementById("dropdownMessage");

dropdown.addEventListener("change", () => {
    if (dropdown.value === "option1") {
        dropdownMessage.textContent = "You selected Option 1!";
    } else if (dropdown.value === "option2") {
        dropdownMessage.textContent = "You selected Option 2!";
    } else {
        dropdownMessage.textContent = "";
    }
});
