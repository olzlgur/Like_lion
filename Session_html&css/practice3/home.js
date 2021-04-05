//alert("Hello world");

message = confirm("hello world");
if(message) {
  
}

const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
const currentTheme = localStorage.getItem('theme');

if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);
    if (currentTheme === 'dark') {
        toggleSwitch.checked = true;
        document.querySelector('.menu').src = 'https://icongr.am/feather/menu.svg?size=24&color=ffffff';
        document.querySelector('.switch').src = 'https://icongr.am/material/alarm-light-outline.svg?size=128&color=ffffff';
    }
}

function switchTheme(e) {
    if (e.target.checked) {
    document.documentElement.setAttribute('data-theme', 'dark');
    localStorage.setItem('theme', 'dark');
    document.querySelector('.menu').src = 'https://icongr.am/feather/menu.svg?size=24&color=ffffff';
    document.querySelector('.switch').src = 'https://icongr.am/material/alarm-light-outline.svg?size=128&color=ffffff';
    }
    else {        
    document.documentElement.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
    document.querySelector('.menu').src = 'https://icongr.am/feather/menu.svg?size=24&color=000000';
    document.querySelector('.switch').src = 'https://icongr.am/material/alarm-light-outline.svg?size=128&color=000000';
    }    
}

toggleSwitch.addEventListener('change', switchTheme, false);

function onClickSubscribe() {
    document.querySelector('.profile-desc .action-wrapper .action-button').style.display = 'none';
    document.querySelector('.profile-desc .action-wrapper .action-button-wrapper').style.display = 'flex';
}

function onClickCancelSubscribe() {
    const message = confirm('구독취소 하시겠습니까?');
    if(message) {
    document.querySelector('.profile-desc .action-wrapper .action-button').style.display = 'flex';
    document.querySelector('.profile-desc .action-wrapper .action-button-wrapper').style.display = 'none';
    }
}