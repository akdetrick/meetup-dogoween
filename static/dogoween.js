$(function() {

    var D = (function($) {
        var $newDog = null,
            $candy = null,
            $dogFrame = null,
            $dogImg = null,
            $treat = null;

    var getNewDog = function(e) {
            e.preventDefault();
            
            $dogFrame.addClass('transitionable');
            $dogFrame.addClass('loading');
            $dogImg.hide();

            $.ajax({ url: "/_get_new_photo" }).done(function(data) {
                currentUrl = data.url;
               $('#candycount').text(data.candycount);
                //window.location.hash = data.photoindex;
                $dogImg.attr('src', data.url).load(function() {
                    $dogFrame.find('a').attr('href', data.url);
                    $dogFrame.removeClass('transitionable');
                    $dogFrame.removeClass('loading');
                    $dogImg.show();
                });
            })
        };

        var giveCandy = function(e) {
            e.preventDefault();

            $.ajax({
                type: "POST",
                url: "/_record_candy",
                data: {
                    imgurl: $dogImg.attr('src')
                },
                success: function(data) {
                   $('#candycount').text(data.candycount);
                }
            }); 

            $treat.show();
            $treat.addClass('transitionable');
            $treat.addClass('given');
        };

        var setupBindings = function() {
            $newDog.bind('click', getNewDog) 
            $candy.bind('click', giveCandy) 
            
            $('.treat').live('webkitTransitionEnd', function(e) {
                $(this).removeClass('given');
                $(this).removeClass('transitionable');
            });
        };

        var PUBLIC = {
            init: function() {

                //set els 
                $newDog = $('#newdog');
                $dogFrame = $('#dog');
                $dogImg = $dogFrame.find('img');
                $candy = $('#candy');
                $treat = $('#js-treat');

                setupBindings();
            } 
        };
        return PUBLIC;
    })(jQuery);

    D.init();
});
