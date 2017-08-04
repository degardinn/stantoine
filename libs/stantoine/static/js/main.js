var parallax = function () {
    $("#mission .image").parallax("center", 0.2, true);
    $("#services .image").parallax("center", 0.5, true);
    $("#who .image").parallax("center", 0.5, true);
};

var initMap = function () {
    var point = { lat: 45.487742, lng: -73.57794 };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: point
    });

    var geocoder = new google.maps.Geocoder();
    geocoder.geocode({ 'address': "St-Antoine Communautaire Montreal" }, function (results, status) {
        if (status === google.maps.GeocoderStatus.OK) {
            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location
            });
        }
    });
}

$(window).on('resize', parallax);
$(document).ready(parallax);
$(document).ready(initMap);

$(window).scroll(function () {
    $(".scaleanim").each(function () {
        var pos = $(this).offset().top;

        var winTop = $(window).scrollTop();
        if (pos < winTop + 600) {
            $(this).addClass("scale");
        }
    });
});

/*
<!--Google Analytics: change UA- XXXXX - X to be your site's ID. -->
    < !--script >
    (function (b, o, i, l, e, r) {
        b.GoogleAnalyticsObject = l;
        b[l] || (b[l] =
            function () {
                (b[l].q = b[l].q || []).push(arguments)
            });
        b[l].l = +new Date;
        e = o.createElement(i);
        r = o.getElementsByTagName(i)[0];
        e.src = '//www.google-analytics.com/analytics.js';
        r.parentNode.insertBefore(e, r)
    }(window, document, 'script', 'ga'));
ga('create', 'UA-XXXXX-X', 'auto');
ga('send', 'pageview');
</script-- >
*/
