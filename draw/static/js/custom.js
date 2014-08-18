$(document).ready(function(){
//    $.ajax({
//        url: "url",
//        type: "GET",
//        dataType: "json",
//        success: function(response) {
//            console.log(response);
//        }
//    });
    $(document).on('click', '.drawing-container', function(){
        imageURL = ($(this).attr('data-img-url'));
        $('.modal-body').children().attr('src', $(this).attr('data-img-url'));
        var drawingTitle = $(this).children('.drawingTitle').text();
        $('.modal-title').text(drawingTitle);
        $('#downloadImage').attr('href', imageURL);
//        $('#editImage').attr('href', 'someeditlink');
//        $('#unFavoriteImage').attr('href', 'method: unfavorite to some url');
//        $('removeAuthor').attr('href', unassociate user from image);
    });
});