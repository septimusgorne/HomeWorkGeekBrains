

function showMessage(){
    let name = prompt("Как Вас зовут?");
    if(name === "" || name === null) {
        alert("Здравствуй Аноним!")
    } else
    alert(`Приятных подсчетов! ${name}`);
    }

showMessage();


const myCalc = document.querySelector(".my__calculator");
const result = document.querySelector("#res")

myCalc.addEventListener("click", function (event) {
    if(!event.target.classList.contains("calc__btn")) return;

    const value = event.target.innerText;

    switch(value){
        case "AC":
            result.innerText = "";
            break;
        case "=":
            if(result.innerText.search(/[^0-9*/+-.]/mi) !== -1) return;

            let intResult = eval(result.innerText)
            if(intResult === Infinity) {
                result.innerText = "Ошибка"
            } else {
                result.innerText = intResult.toFixed(2)
            }
            break;
        default:
            result.innerText += value;
    }
});
