$(document).ready(function () {
    "use strict";

    // pre-loader
    $(window).load(function() {
        $('#preloader-center').fadeOut();
        $('#preloader').delay(200).fadeOut('slow').remove();
    });

    // full screen home section
    if ($(window).width() > 739) {
        var slideHeight = $(window).height();
        //Add your javascript for large screens here
        $('.section-home-area').css('height', slideHeight);

        $(window).resize(function () {
            $('.section-home-area').css('height', slideHeight);
        });
    }
    else {
        //Add your javascript for small screens here
        $('.section-home-area').css('height', 'auto');

        $(window).resize(function () {
            $('.section-home-area').css('height', 'auto');
        });
    }


    // click menu
    $('.show-menu-1').on('click',function () {
        $(".sub-menu-1").toggle();
    });
    $('.show-menu-2').on('click',function () {
        $(".sub-menu-2").toggle();
    });

    //gallery carousel
    $('.gl-carousel').owlCarousel({
        items: 4,
        navigation: true,
        navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        autoPlay: true,
        pagination: false,
        transitionStyle: "fade"
    });

    //post carousel
    $('.post-carousel').owlCarousel({
        singleItem: true,
        navigation: false,
        autoPlay: true,
        pagination: true
    });

    /* === Magnific Popup js === */
    (function () {
        $('.image-popup').magnificPopup({
            delegate: 'a',
            type: 'image',
            // other options
            closeOnContentClick: false,
            closeBtnInside: false,
            mainClass: 'mfp-with-zoom mfp-img-mobile',
            gallery: {
                enabled: true
            },
            zoom: {
                enabled: true,
                duration: 300, // don't foget to change the duration also in CSS
                opener: function (element) {
                    return element.find('img');
                }
            }
        });
    }());

    // Off Canvas nice scroll
    $(".site-nav").niceScroll(".off-canvas-inner", {
        cursorcolor: "#929292",
        cursoropacitymax: .7,
        cursorwidth: "6px",
        cursorborder: "none",
        boxzoom: false,
        gesturezoom: false,
        grabcursorenabled: false,
        bouncescroll: false,
        smoothscroll: true
    });

    $(".st-top").on('click', function (e) {
        e.preventDefault();
        $(".site-nav").getNiceScroll(0).doScrollTop(0);
    });

    // jQuery for page scrolling feature - requires jQuery Easing plugin
    $('.scroll-top').on('click', function (event) {
        var $anchor = $(this);
        $('html, body')
            .stop()
            .animate({
                scrollTop: $($anchor.attr('href')).offset().top - 0
            }, {
                duration: 1000,
                easing: "linear"
            });
        event.preventDefault();
    });

    // Share this
    var body = $('body');
    $('.navbar-toggle').on('click', function () {
        body.addClass('canvas-show');
    });

    $('.close-btn').on('click', function () {
        body.removeClass('canvas-show');
    });
    $('.mask').on('click', function () {
        body.removeClass('canvas-show');
    });
    $('.st-content-wrap').on('click', function () {
        body.removeClass('canvas-show');
    });

    // COUNTER UP
    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });


}());