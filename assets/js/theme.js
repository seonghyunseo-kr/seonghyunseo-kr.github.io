const STORAGE_KEY = "theme";
const THEME_ATTR  = "data-theme";
const QUERY_KEY   = "(prefers-color-scheme: dark)";

const themes = {
  LIGHT: "light",
  DARK: "dark",
};

initTheme();

function initTheme() {
  const savedTheme = localStorage.getItem(STORAGE_KEY);

  if (savedTheme) {
    // Storage theme
    setTheme(savedTheme);
  } else if (window.matchMedia && window.matchMedia(QUERY_KEY).matches) {
    // system theme
    setTheme(themes.DARK);
  } else {
    // Default theme
    setTheme(themes.LIGHT);
  }

  // Watch for system theme changes
  window.matchMedia(QUERY_KEY).addEventListener("change", (e) => {
    const newTheme = e.matches ? themes.DARK : themes.LIGHT;
    setTheme(newTheme);
  });
}

function toggleTheme() {
  const theme = getTheme();
  const newTheme = theme === themes.DARK ? themes.LIGHT : themes.DARK;
  setTheme(newTheme);
  localStorage.setItem(STORAGE_KEY, newTheme);
}

function getTheme() {
  return document.documentElement.getAttribute(THEME_ATTR);
}

function setTheme(value) {
  document.documentElement.setAttribute(THEME_ATTR, value);
}

const LANG_STORAGE_KEY = "lang";
const LANG_ATTR        = "data-lang";

const langs = {
  EN: "en",
  KR: "kr",
};

document.addEventListener("DOMContentLoaded", initLang);
document.addEventListener("DOMContentLoaded", initTimelineScroll);

function initTimelineScroll() {
  const track = document.querySelector(".home-ht-track");
  if (track) {
    track.scrollLeft = track.scrollWidth;
  }
}

function initLang() {
  const savedLang = localStorage.getItem(LANG_STORAGE_KEY);
  setLang(savedLang === langs.KR ? langs.KR : langs.EN);
}

function setLang(lang) {
  document.documentElement.setAttribute(LANG_ATTR, lang);
  localStorage.setItem(LANG_STORAGE_KEY, lang);

  document.querySelectorAll("[data-en]").forEach((el) => {
    const en = el.getAttribute("data-en");
    const kr = el.getAttribute("data-kr");
    el.textContent = lang === langs.KR && kr && kr.trim() !== "" ? kr : en;
  });

  document.querySelectorAll(".lang-option").forEach((el) => {
    el.classList.toggle("active", el.getAttribute("data-lang-option") === lang);
  });
}

function getLang() {
  return document.documentElement.getAttribute(LANG_ATTR);
}
