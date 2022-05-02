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

function setTheme(theme) {
    storage = storageAvailable("localStorage");
    if(storage) storage.setItem("theme", theme);

    if (theme == "dark") {
        document.getElementById("theme").setAttribute("src", "moon.svg")
        document.documentElement.classList.remove("light");
    } else {
        document.getElementById("theme").setAttribute("src", "sun.svg")
        document.documentElement.classList.add("light");
    }
}

var theme = window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches
    ? "dark"
    : "light";

storage = storageAvailable("localStorage");
if (storage) {
    theme = storage.getItem("theme") ?? theme;
} 

// Initialize theme
setTheme(theme);

document.getElementById("theme").addEventListener("click", () => {
    theme = theme === "light" ? "dark" : "light";
    setTheme(theme);
});
