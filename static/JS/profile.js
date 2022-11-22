const subMenu = document.getElementById("subMenu");
const profileBtn = document.getElementsByClassName("profile-image-btn");


profileBtn[0].addEventListener("click", ()=>{
    subMenu.classList.toggle("open-menu")
})
