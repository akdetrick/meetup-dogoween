$(function() {

    var D = (function($) {
        var $newDog = null,
            $candy = null;

        var getNewDog = function(e) {
            e.preventDefault();
            console.warn('getting new dog');
        };

        var giveCandy = function(e) {
            e.preventDefault();
            console.warn('giving candy');
        };

        var setupBindings = function() {
            $newDog.bind('click', getNewDog) 
            $candy.bind('click', giveCandy) 
        };

        var PUBLIC = {
            init: function() {

                //set els 
                $newDog = $('#newdog');
                $candy = $('#candy');

                setupBindings();
            } 
        };
        return PUBLIC;
    })(jQuery);

    D.init();
});
