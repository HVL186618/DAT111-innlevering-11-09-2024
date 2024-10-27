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

    // de skulle aldri gitt oss makten til å erstatte alle punktum med små ender
    function replacePeriodsWithImage(node) {
        // for alle nodes
        if (node.nodeType === Node.TEXT_NODE) {
            // hvis text node, lag nytt element hvor punktum er erstatta
            let newText = node.textContent.replace(
                /\./g, // Erstatt "."
                '<img src="period.png" alt="." style="width:10px;height:10px;">' // erstatt med bildeelement 
            ).replace(
                /\@/g, // Erstatt "@"
                '<img src="alphaduck.png" alt="@" style="margin-bottom:-5px;width:20px;height:20px;">' // erstatt med bildeelement 
            );

            // element til å ta den nye koden i
            const span = document.createElement('span');
            span.innerHTML = newText; // erstatt koden til ny span med nye koden vår

            // erstatt original node med nytt element
            node.replaceWith(span);
        } else {
            // hvis ikke text node, recur for å sjekke child nodes
            node.childNodes.forEach(replacePeriodsWithImage);
        }
    }

    // nå blir det party her
    document.body.childNodes.forEach(replacePeriodsWithImage);
});
