// table of contents generator! takes all <h2> elements with ids in .copy and
// makes a menu of them.
$(document).ready(function () {
    var $els = $(".copy h2");
    if ($els.length) {
        $toc = $("<nav class='toc'></nav>");
        $els.each(function (i,v) {
            var $h2 = $(v),
                id = $h2.attr("id");
            if (id && $h2.length) {
                $toc.append($("<a href='#" + id + "'>" + $h2.text() + "</a>"));
            }
        });
        if ($toc.children().length) {
            $toplink = $("<a href='#'>back to top</a>");
            $toplink.css({'float': 'left'});
            $toplink.click(function (e) {
                $toplink.detach();
            });
            $("#content").prepend($toc);
            $toc.delegate("a", "click", function(e) {
                $toplink.detach();
                $($(this).attr("href")).closest("section").append($toplink);
            });
        }
    }
});
