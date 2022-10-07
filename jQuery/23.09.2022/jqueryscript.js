$(document).ready(() => {
    $(".tictac").hide()

    $("#opcje").change(function(){
        $(".tictac").show()
        $("#opcje").hide()
        $("#labelel").hide()
        mode = $("#opcje").val()
        console.log(mode)
    })

    $("#reset").click(function() {
        location.reload()
    })

    function jakiZnak(num) {
        if(num==2) {
            return "O"
        }
        else if(num==1) {
            return "X"
        }
    }


    let znak = 1;
    $("td").click(function() {
        
        if(mode=="pvp") {
            if($(this).text()=='') {
                $(this).text(jakiZnak(znak))
                if (znak%2==0) {
                    znak=1
                }
                else {
                    znak=2
                }
            }
            else {
                $(this).css("animation", "nope .5s")
                setTimeout(() => {
                    $(this).css("animation", "none")
                },500)
            }
        }
        else if(mode=="pc") {
            
        }
        else {
            window.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        }

    })
})