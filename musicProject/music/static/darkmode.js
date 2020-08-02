let darkMode = localStorage.getItem('Darkmode');
let root = document.documentElement
const darkModeToggle = document.querySelector('#Nightmode');

const enableDarkmode = () => {
    localStorage.setItem('Darkmode', 'enable');
    root.style.setProperty('--main-background-color', '#000000');
    root.style.setProperty('--main-text-color', '#fefff9');
    root.style.setProperty('--sub-title-color', '#cecece');
    root.style.setProperty('--background-color', '2e504a'); 
    root.style.setProperty('--sidebar-color', '#1f1f1f');
    root.style.setProperty('--button-hover-color', '#706e6e');
    root.style.setProperty('--form-hover-color', 'gray');
    brd = document.querySelectorAll('.song-template');

    for (var i = 0; i < brd.length; i++){
        brd[i].style.border = '2pt solid #4e4e9a';
    }

};

const disableDarkmode = () => {
    localStorage.setItem('Darkmode', null);
    root.style.setProperty('--main-background-color', 'alicebliue');
    root.style.setProperty('--main-text-color', 'rgb(31, 34, 31)');
    root.style.setProperty('--sub-title-color', 'gray');
    root.style.setProperty('--background-color', 'rgb(92, 125, 175)');
    root.style.setProperty('--sidebar-color', 'rgb(62, 159, 177)');
    root.style.setProperty('--button-hover-color', 'rgba(5, 80, 114, 0,753)');
    root.style.setProperty('--form-hover-color', 'gray');
};

darkModeToggle.addEventListener("click", () => {
    darkMode = localStorage.getItem('Darkmode');
    console.log(darkMode)
    if (darkMode !== 'enable') {
        enableDarkmode();
    }

    else {
        disableDarkmode();
    }
});
