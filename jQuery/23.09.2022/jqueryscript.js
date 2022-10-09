$(document).ready(() => {
    $(".tictac").hide()
    $("#info").hide()
//---------------OPCJE--------------------
    $("#opcje").change(function(){
        $(".tictac").show()
        $("#opcje").hide()
        $("#labelel").hide()
        mode = $("#opcje").val() //ustawianie trybu gry
        if (mode=="pvp") { //wyświetlanie innych informacji w zależności od trybu gry
            $("#info").show()
            $("#info").text("PLAYER 1 - X | PLAYER 2 - O")
        }
        else if(mode=="pc")
        {
            $("#info").show()
            $("#info").text("PLAYER 1 - X | COMPUTER - O")
        }
    })
//---------------RESTART GAME--------------------
    $("#reset").click(function() {
        location.reload()
    })
//---------------SPRAWDZANIE JAKI ZNAK TERAZ GRA--------------------
    function jakiZnak(num) {
        if(num==2) {
            return "O"
        }
        else if(num==1) {
            return "X"
        }
    }
//---------------SPRAWDZANIE WYGRANYCH (Trochę spaghetti)--------------------
    function WinCheck(znak) {
        if (
            $(".id1").text()==znak && //sprawdzanie jakie znaki stoją w danych kombinacjach
            $(".id2").text()==znak &&
            $(".id3").text()==znak
        ) {
            $(".id1").css("background-color", "green") //Jeśli wygrał zmień wygrane pola na zielony
            $(".id2").css("background-color", "green")
            $(".id3").css("background-color", "green")
            return true
        }
        else if (
            $(".id4").text()==znak && 
            $(".id5").text()==znak &&
            $(".id6").text()==znak
        ) {
            $(".id4").css("background-color", "green")
            $(".id5").css("background-color", "green")
            $(".id6").css("background-color", "green")
            return true
        }
        else if (
            $(".id7").text()==znak && 
            $(".id8").text()==znak &&
            $(".id9").text()==znak
        ) {
            $(".id7").css("background-color", "green")
            $(".id8").css("background-color", "green")
            $(".id9").css("background-color", "green")
            return true
        }
        else if (
            $(".id1").text()==znak && 
            $(".id4").text()==znak &&
            $(".id7").text()==znak
        ) {
            $(".id1").css("background-color", "green")
            $(".id4").css("background-color", "green")
            $(".id7").css("background-color", "green")
            return true
        }
        else if (
            $(".id2").text()==znak && 
            $(".id5").text()==znak &&
            $(".id8").text()==znak
        ) {
            $(".id2").css("background-color", "green")
            $(".id5").css("background-color", "green")
            $(".id8").css("background-color", "green")
            return true
        }
        else if (
            $(".id3").text()==znak && 
            $(".id6").text()==znak &&
            $(".id9").text()==znak
        ) {
            $(".id3").css("background-color", "green")
            $(".id6").css("background-color", "green")
            $(".id9").css("background-color", "green")
            return true
        }
        else if (
            $(".id1").text()==znak && 
            $(".id5").text()==znak &&
            $(".id9").text()==znak
        ) {
            $(".id1").css("background-color", "green")
            $(".id5").css("background-color", "green")
            $(".id9").css("background-color", "green")
            return true
        }
        else if (
            $(".id3").text()==znak && 
            $(".id5").text()==znak &&
            $(".id7").text()==znak
        ) {
            $(".id3").css("background-color", "green")
            $(".id5").css("background-color", "green")
            $(".id7").css("background-color", "green")
            return true
        }
    }
//---------------WSTAWIANIE ZNAKÓW NA PLANSZE--------------------
    let znak = 1;
    function random_choice(array) {
        return array[Math.floor(Math.random() * array.length)]
      }
    let pola = ["id1","id2","id3","id4","id5", "id6", "id7", "id8", "id9"] //dostępne pola
    $("td").click(function() {
        
        if(mode=="pvp") { //jeśli tryb gry to PVP
            if($(this).text()=='') { //jeśli puste pole
                $(this).text(jakiZnak(znak)) //wstawianie znaku
                if(WinCheck(jakiZnak(znak))) {
                    mode="endgame" //ustawianie trybu na endgame aby nikt nie mógł nic wstawić
                }
                if (znak%2==0) { //zmiana znaku
                    znak=1
                }
                else {
                    znak=2
                }
            }
            else { //animacja zajętego pola
                $(this).css("animation", "nope .5s")
                setTimeout(() => {
                    $(this).css("animation", "none")
                },500)
            }
        }
        else if(mode=="pc") { //jeśli tryb gry to gracz vs computer
            if($(this).text()=='') { //jeśli puste pole
                $(this).text("X") //wstawianie znaku
                pola = pola.filter(function removeItem(item) { //funkcja która miała usuwać pola zajęte ale nie działa nie wiem czemu:(
                    return item != $(this).attr('class')
                })
                if(WinCheck(jakiZnak(znak))) { //sprawdzanie czy wygrał po ruchu
                    mode="endgame" //ustawianie trybu na endgame aby nikt nie mógł nic wstawić
                }

                if(mode=="pc") { //sprawdzanie czy poprzedni ruch nie zakończył gry
                    $(`.${random_choice(pola)}`).text("O") //wstawianie przez computer w losowe pole
                }
                if(WinCheck("O")) { //sprawdzanie czy wygrał po ruchu
                    mode="endgame" //ustawianie trybu na endgame aby nikt nie mógł nic wstawić
                }
            }
            else { //animacja zajętego pola
                $(this).css("animation", "nope .5s")
                setTimeout(() => {
                    $(this).css("animation", "none")
                },500)
            }
        }

    })
})