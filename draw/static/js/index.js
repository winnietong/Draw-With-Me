$(document).ready(function() {


var width = 1;
//BUILD BRUSH WIDTH SLIDER
$(function() {
    $( "#slider" ).slider({
        value: width,
        min:1,
        max:100,
        orientation: "horizontal",
        range: "min",
        animate: true,
        slide: function( event, ui ) {
            width = $( "#slider" ).slider( "value" );
//            console.log("w"+width);
            $('#brushWidth').val(width);
        }
    });
});

//SET BRUSH COLOR
var strokeColor = "black";
$('.colorbox').on('click', function() {
    strokeColor = $(this).data("bcolor");
});


function findPos(obj) {
    var curleft = 0, curtop = 0;
    if (obj.offsetParent) {
        do {
            curleft += obj.offsetLeft;
            curtop += obj.offsetTop;
        } while (obj = obj.offsetParent);
        return { x: curleft, y: curtop };
    }
    return undefined;
}

function getWidthSlider() {
	width = $( "#slider" ).slider( "option", "value");
	return width;
}

var c=document.getElementById("DrawCanvas");
var ctx=c.getContext("2d");
ctx.lineWidth=3;

var xCur;
var yCur;
var xStart;
var yStart;
var startNewLine = true;
    

$("#DrawCanvas").on("mousemove", function(e) {
	ctx.lineWidth=getWidthSlider();
	ctx.lineCap="round";

    var pos = findPos(this);
    var x = e.pageX - pos.x;
    var y = e.pageY - pos.y;

	if (startNewLine) {
        xStart = x;
		yStart = y;
	}
    ctx.beginPath();
    ctx.strokeStyle=strokeColor;

    if (e.which == 1) {
        xEnd = x;
		yEnd = y;
		ctx.moveTo(xStart,yStart);
		ctx.lineTo(xEnd,yEnd);
		xStart = xEnd;
		yStart = yEnd;
    }
	ctx.stroke();
	ctx.save();
});


$('#undo').on('click', function() {
	     ctx.restore();
});

$(c).on("mouseup", function(){
	startNewLine = true;
});

$(c).on("mousedown", function(){
	startNewLine = false;
});



//$(document).on('click', '#saveImage', function(c) {
///* var c = document.getElementById("sketch"); */
//    var dataString = c.toDataURL();
//    document.getElementById('canvasImg').src = dataString;
//    /* window.open(dataString); */
//});


$("#bt_draw").on('click', function() {
    document.getElementById("theimage").src = c.toDataURL();
});

//DOWNLOAD IMAGE TO COMPUTER
function downloadCanvas(link, canvasId, filename) {
    link.href = document.getElementById(canvasId).toDataURL();
    link.download = filename;
}

document.getElementById('bt_download').addEventListener('click', function() {
    downloadCanvas(this, 'DrawCanvas', 'draw_with_me.png');
}, false);


//SAVE IMAGE TO SERVER
$("#bt_saveLocal").on('click', function() {
	var image = c.toDataURL("image/png").replace("image/png", "image/octet-stream");
    // save canvas image as data url (default is png)
    var dataURL = c.toDataURL();
    // set canvasImg image src to dataURL
    // so it can be saved as an image
    document.getElementById('canvasImg').src = dataURL;

    var title = "Draw With Me";
    title = $("#imgTitle").val();

    // Added origin path because I'm using from another page
    url = window.location.origin + '/save_image/';
    console.log(title);
    $.ajax({
        type: "POST",
        url: url,
        dataType: 'text',
        data: {
            base64data : dataURL,
            title: title
        }
    });

});


$('#clearCanvas').on('click', function() {
    ctx.clearRect(0, 0, c.width, c.height);
});



});
