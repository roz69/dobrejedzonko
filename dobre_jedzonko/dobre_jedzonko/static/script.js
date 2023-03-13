const container = document.querySelector(".grid")
const navBTN = document.querySelector(".sidebarIconToggle")

function contenerScale(){
    container.classList.toggle("active_navbar")
}

navBTN.addEventListener("click", contenerScale)


