document.addEventListener("DOMContentLoaded", function() {
    function toggleCollapsible() {
        var collapsible = document.getElementById("collapsible_week_description");
        if (window.getComputedStyle(collapsible).display === "none") {
            collapsible.style.display = "table-row";
        } else {
            collapsible.style.display = "none";
        }
    }

    function toggleCalculations() {
        var collapsible = document.getElementById("collapsable-pace-calculations");
        if (window.getComputedStyle(collapsible).display === "none") {
            collapsible.style.display = "block";
        } else {
            collapsible.style.display = "none";
        }
    }

    document.getElementById("person_week_in_training_td").addEventListener("click", toggleCollapsible);
    document.getElementById("calculator-icon").addEventListener("click", toggleCalculations);

});
