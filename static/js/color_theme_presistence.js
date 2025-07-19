function restoreColorSchemePreference() {
  const colorScheme = localStorage.getItem(colorSchemeStorageItemName);
  console.log(colorScheme)

  if (!colorScheme) {
    return;
  }

  const ui = colorSchemeTogglerEl.classList.contains("light-theme") ? "light" : "dark";

  if (colorScheme != ui) {
    colorSchemeLiEl.classList.toggle("light-theme");
    return;
  }
}

function storeColorThemePreference() {
  colorSchemeLiEl.classList.toggle("light-theme");

  const colorScheme =  colorSchemeLiEl.classList.contains("light-theme") ? "light" : "dark";
  localStorage.setItem(colorSchemeStorageItemName, colorScheme);
}

const colorSchemeStorageItemName = "preferredColorScheme";
const colorSchemeTogglerEl = document.getElementById("change-theme");
const colorSchemeLiEl = document.getElementById("change-theme-li");

if (colorSchemeTogglerEl && colorSchemeLiEl) {
  restoreColorSchemePreference();

  colorSchemeTogglerEl.addEventListener("click", storeColorThemePreference);
}
