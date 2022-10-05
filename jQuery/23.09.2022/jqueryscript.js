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
})