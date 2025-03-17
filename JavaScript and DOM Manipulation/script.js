// Function to change text dynamically
function changeText() {
    document.getElementById("text").textContent = "The text has been changed!";
}

// Function to toggle highlight class
function toggleStyle() {
    document.getElementById("text").classList.toggle("highlight");
}

// Function to add a new element
function addElement() {
    let newElement = document.createElement("p");
    newElement.textContent = "This is a new dynamically added element.";
    newElement.classList.add("highlight");
    document.getElementById("element-container").appendChild(newElement);
}

// Function to remove the last added element
function removeElement() {
    let container = document.getElementById("element-container");
    if (container.lastChild) {
        container.removeChild(container.lastChild);
    }
}
