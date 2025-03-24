// Form Submission Handling
document.getElementById("yogaForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent actual submission

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let classType = document.getElementById("classType").value;

    document.getElementById("formMessage").textContent = 
        `Thank you, ${name}! You've booked a ${classType} yoga class.`;
});

// Function to toggle modal visibility
const modal = document.getElementById("modal");
const showModal = document.getElementById("showModal");
const closeModal = document.getElementById("closeModal");

showModal.addEventListener("click", () => {
    modal.classList.remove("hidden");
});

closeModal.addEventListener("click", () => {
    modal.classList.add("hidden");
});

// Function to trigger breathing animation
const animateBoxBtn = document.getElementById("animateBoxBtn");
const animatedBox = document.getElementById("animatedBox");

animateBoxBtn.addEventListener("click", () => {
    if (animatedBox.style.display === "none" || animatedBox.style.display === "") {
        animatedBox.style.display = "block";
        animatedBox.classList.add("breathe-animation");

        // Hide animation after 5 seconds
        setTimeout(() => {
            animatedBox.classList.remove("breathe-animation");
            animatedBox.style.display = "none";
        }, 5000);
    }
});

// Save user details in local storage on form submission
document.getElementById("yogaForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let classType = document.getElementById("classType").value;

    // Save data
    localStorage.setItem("yogaName", name);
    localStorage.setItem("yogaEmail", email);
    localStorage.setItem("yogaClass", classType);

    document.getElementById("formMessage").textContent = 
        `Thank you, ${name}! You've booked a ${classType} yoga class.`;
});

// Auto-fill form from local storage
window.onload = function () {
    if (localStorage.getItem("yogaName")) {
        document.getElementById("name").value = localStorage.getItem("yogaName");
        document.getElementById("email").value = localStorage.getItem("yogaEmail");
        document.getElementById("classType").value = localStorage.getItem("yogaClass");
    }
};
