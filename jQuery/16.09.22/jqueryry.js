let s = 10;

$(document).ready(() => {
    $(".tak").mouseenter(() => {
        console.log("heh")
    })
    $(".tak").dblclick(() => {
        alert("dblclick()")
    })

    $(".nie").hover(() => {
        s += 10;
        $("p").css("font-size", `${s}px`);
    },
        () => {
            $("p").css("font-size", "10px");
        }
    );
    $("#uno").click(function() {
        $(this).hide();
    })
    $("#dos").click(function() {
        $(this).hide();
    })
    $("#tres").click(function() {
        $(this).hide();
    })
    
    $("#obojetniejakie").click(show_all);

})


function show_all() {
    $("#uno").show(10);
    $("#dos").show(100);
    $("#tres").show(1000);
}
function toggle_all() {
    $("#kontener").toggle();
}