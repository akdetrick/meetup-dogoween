$(function() {

    var D = (function($) {
        var $newDog = null,
            $candy = null,
            $treat = null;

        var getNewDog = function(e) {
            e.preventDefault();
            console.warn('getting new dog');
        };

        var giveCandy = function(e) {
            e.preventDefault();
            console.warn('giving candy');

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
                $candy = $('#candy');
                $treat = $('#js-treat');

                setupBindings();
            } 
        };
        return PUBLIC;
    })(jQuery);

    D.init();
});
