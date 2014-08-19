$(document).ready(function() {


    // HIDE 'SAVE AS' BUTTON ON HOME PAGE
    if(location.pathname == '/'){
        $("#bt_saveAs").hide();
    }

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

    // DRAWING STARS //
    function drawStar(options) {
      var length = 15;
      ctx.save();
      ctx.translate(options.x, options.y);
      ctx.beginPath();
      ctx.globalAlpha = options.opacity;
      ctx.rotate(Math.PI / 180 * options.angle);
      ctx.scale(options.scale, options.scale);
      ctx.strokeStyle = options.color;
      ctx.lineWidth = options.width;
      for (var i = 5; i--;) {
        ctx.lineTo(0, length);
        ctx.translate(0, length);
        ctx.rotate((Math.PI * 2 / 10));
        ctx.lineTo(0, -length);
        ctx.translate(0, -length);
        ctx.rotate(-(Math.PI * 6 / 10));
      }
      ctx.lineTo(0, length);
      ctx.closePath();
      ctx.stroke();
      ctx.restore();
    }
    function getRandomInt(min, max) {
      return Math.floor(Math.random() * (max - min + 1)) + min;
    }
    // END OF DRAWING STARS FUNCTION //


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

            if (strokeColor == 'stars') {
                ctx.lineWidth = 1;
                drawStar({x: xEnd,
                    y: yEnd,
                    angle: getRandomInt(0, 180),
                    width: getRandomInt(1, 10),
                    opacity: Math.random(),
                    scale: getRandomInt(1, 20) / 10,
                    color: ('rgb(' + getRandomInt(0, 255) + ',' + getRandomInt(0, 255) + ',' + getRandomInt(0, 255) + ')')
                });
            }

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
