    <script type="text/javascript">
        $(document).ready(function(){
      
            $('[data-toggle="popover"]').popover({
                placement : 'top'
            });
        });
    </script>

    <script type="text/javascript" charset="utf-8">
        jQuery(document).ready(function() {
        jQuery('.tabs .tab-links a').on('click', function(e)  {
            var currentAttrValue = jQuery(this).attr('href');
     
            // Show/Hide Tabs
            jQuery('.tabs ' + currentAttrValue).show().siblings().hide();
     
            // 
            jQuery('.tabs ' + currentAttrValue).children().show();

            // Change/remove current tab to active
            jQuery(this).parent('li').addClass('active').siblings().removeClass('active');
     
            e.preventDefault();
            });
    });
    </script>
    

    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile, .music-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });

    </script>
    
    //<script type="text/javascript" charset="utf-8">
        //// Pause the video when the modal is closed
        //$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            //// Remove the src so the player itself gets removed, as this is the only
            //// reliable way to ensure the video stops playing in IE
            //$("#trailer-video-container").empty();
        //});
        //// Start playing the video whenever the trailer modal is opened
        //$(document).on('click', '.music-tile', function (event) {
            //var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            //var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            //$("#trailer-video-container").empty().append($("<iframe></iframe>", {
              //'id': 'trailer-video',
              //'type': 'text-html',
              //'src': sourceUrl,
              //'frameborder': 0
            //}));
        //});

    //</script>
