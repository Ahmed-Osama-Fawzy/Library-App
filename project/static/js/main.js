// Load Data to Local Storge from show books page
let Buttons = Array.from(document.getElementsByClassName("ShowBook"))
console.log(Buttons)
Buttons.forEach((button)=>{
    button.addEventListener("click",(e)=>{
        let Container = button.parentElement.parentElement
        let Headers = Container.children
        let Title = Headers.item(1).children[0].innerHTML
        let Author = Headers.item(2).children[0].innerHTML
        let Category = Headers.item(3).children[0].innerHTML
        let Available = Headers.item(4).children[0].innerHTML
        let Description = Headers.item(5).children[0].innerHTML
        let Cover = Container.parentElement.children[0].children[0].getAttribute("src")
        
        localStorage.clear()
        localStorage.setItem("Title",Title)
        localStorage.setItem("Author",Author)
        localStorage.setItem("Category",Category)
        localStorage.setItem("Available",Available)
        localStorage.setItem("Description",Description)
        localStorage.setItem("Cover",Cover)
    })
} )

// Load Data From Local Storge to Show Book Page
window.addEventListener("load",()=>{
    document.getElementById("Cover").setAttribute("src",localStorage.getItem("Cover"))
    document.getElementById("Title").innerHTML = localStorage.getItem("Title")
    document.getElementById("Author").innerHTML = localStorage.getItem("Author")
    document.getElementById("Category").innerHTML = localStorage.getItem("Category")
    document.getElementById("Available").innerHTML = localStorage.getItem("Available")
    document.getElementById("Description").innerHTML = localStorage.getItem("Description")
})

window.addEventListener("cancel",()=>{
    localStorage.clear()
})

// Fitering Function
function filterItems(arr, query) {
    return ;
}
document.getElementById("Search").addEventListener("keyup",(e)=>{
    let ConTitles = Array.from(document.getElementsByClassName("BookTitle"))
    let Value = document.getElementById("Search").value
    let Titles = []
    if(Value){
        ConTitles.forEach((Title)=>{
            Title.parentElement.parentElement.parentElement.style.display = 'none'
        })
        for(i = 0 ; i < ConTitles.length;i++){
            let Obj = {
                x:[i,ConTitles[i].innerHTML,ConTitles[i]]
            }
            Titles[i] = Obj
        }
        const Filtered = Titles.filter((el) => el.x[1].toLowerCase().includes(Value.toLowerCase()))
        Filtered.forEach(item => {
            item.x[2].parentElement.parentElement.parentElement.style.display = 'block'
        })
    }else{
        ConTitles.forEach((Title)=>{
            Title.parentElement.parentElement.parentElement.style.display = 'block'
        })
    }
})