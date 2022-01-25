/*!
    * Start Bootstrap - SB Admin v7.0.4 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2021 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    // 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {
    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});

function services(){
    let ajax = new XMLHttpRequest();
    ajax.onreadystatechange = ()=>{
       if(ajax.readyState == 4 && ajax.status == 200){
            $('main').html(ajax.responseText);
       }
    }
    ajax.open('GET', "/services", true);
    ajax.send()
}

// view services
$(document).ready(()=>{
    let ajax = new XMLHttpRequest();
    const facility = document.body.querySelector('#patient');
    let facility_name = facility.name;
    ajax.onreadystatechange = ()=>{
        if(ajax.readyState == 4 && ajax.status == 200){
            $('#services').html(ajax.responseText);
        }
    }
    ajax.open('GET', `/services-view?facility_name=${facility_name}`, true);
    ajax.send()
});

// carousel facility
$(document).ready(()=>{
    let ajax = new XMLHttpRequest();
    ajax.onreadystatechange = ()=>{
        if(ajax.readyState === 4 && ajax.status === 200){
            $('#hospitals').html(ajax.responseText);
        }
    }
    ajax.open('GET', `/facility-carousel`, true);
    ajax.send()
});


 