$(document).ready(()=>{

    console.log("ready")

    function drawImage(){
      console.log("draw")
    }

    let width= $(window).innerWidth(),height=$(window).innerHeight();
    let canvas=$('canvas')
    // canvas[0].width=width;
    canvas[0].height=height;

    context=canvas[0].getContext('2d')
    console.dir(canvas[0])
    // canvas[0].style.backgroundImage=


})
