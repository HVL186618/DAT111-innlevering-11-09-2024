// toggle visibility av dropdowns
document.addEventListener("DOMContentLoaded", function() {
    const dropdownToggles = document.querySelectorAll(".dropdown-toggle");
    const dropdownContents = document.querySelectorAll(".dropdown-content");

    dropdownToggles.forEach((toggle, index) => {
        toggle.addEventListener("click", function() {
            // toggle display av korresponderende dropdown content
            const dropdownContent = dropdownContents[index];
            if (dropdownContent.style.display === "block") {
                dropdownContent.style.display = "none";
            } else {
                dropdownContent.style.display = "block";
            }
        });
    });
});
