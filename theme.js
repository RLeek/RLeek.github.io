
// Sets up correct theme
function storageAvailable(type) {
    var storage;
    try {
        storage = window[type];
        var x = '__storage_test__';
        storage.setItem(x, x);
        storage.removeItem(x);
        return storage;
    }
    catch(e) {
        return false;
    }
}

var theme = "dark";

if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
    theme = "light";
}

storage = storageAvailable("localStorage");
if (storage) {
    theme = storage.getItem("theme") ? storage.getItem("theme"): theme;
} 


// Now actually use correct theme and make it receptive to clicks
document.getElementById("theme").addEventListener("click", themeToggle);

if (theme == "dark") {
    document.getElementById("theme").setAttribute("src", "moon.svg")
    document.documentElement.style.setProperty("--background-col", "#0C1317");
    document.documentElement.style.setProperty("--focusedText-col", "#CEB591");
    document.documentElement.style.setProperty("--focusedTint-col", "invert(82%) sepia(38%) saturate(248%) hue-rotate(353deg) brightness(83%) contrast(93%)")
    document.documentElement.style.setProperty("--unfocusedText-col", "#8A836B");
} else {
    document.getElementById("theme").setAttribute("src", "sun.svg")
    document.documentElement.style.setProperty("--background-col", "#D4C5A8");
    document.documentElement.style.setProperty("--focusedText-col", "#6B1A40");
    document.documentElement.style.setProperty("--focusedTint-col", "invert(12%) sepia(61%) saturate(2130%) hue-rotate(304deg) brightness(89%) contrast(100%)")
    document.documentElement.style.setProperty("--unfocusedText-col", "#A74D68");
}


// Text colour
// Unselected text Colour
// Background Colour

function themeToggle(event) {
    storage = storageAvailable("localStorage");
    if (theme == "light") {
        theme = "dark";
        if (storage) {
            storage.setItem("theme", "dark");
        }
        // Actually set to dark theme
        document.getElementById("theme").setAttribute("src", "/moon.svg")
        document.documentElement.style.setProperty("--background-col", "#0C1317");
        document.documentElement.style.setProperty("--focusedText-col", "#CEB591");
        document.documentElement.style.setProperty("--focusedTint-col", "invert(82%) sepia(38%) saturate(248%) hue-rotate(353deg) brightness(83%) contrast(93%)")
        document.documentElement.style.setProperty("--unfocusedText-col", "#8A836B");


    } else {
        theme = "light";
        if (storage) {
            storage.setItem("theme", "light");
        }
        // Actually set to light theme
        document.getElementById("theme").setAttribute("src", "/sun.svg")
        document.documentElement.style.setProperty("--background-col", "#D4C5A8");
        document.documentElement.style.setProperty("--focusedText-col", "#6B1A40");
        document.documentElement.style.setProperty("--focusedTint-col", "invert(12%) sepia(61%) saturate(2130%) hue-rotate(304deg) brightness(89%) contrast(100%)")
        document.documentElement.style.setProperty("--unfocusedText-col", "#A74D68");
    }
}