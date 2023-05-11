function toggleCollapsible() {
    console.log("jesam ga")
  var collapsibleElement = document.getElementById("collapsible_week_description");
  if (collapsibleElement.style.display === "none") {
    collapsibleElement.style.display = "table-row";
  } else {
    collapsibleElement.style.display = "none";
  }
}

document.getElementById("collapsable_week_description_toggle_td").addEventListener("click", toggleCollapsible);
