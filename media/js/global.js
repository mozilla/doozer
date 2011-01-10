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

$.fn.vtruncate = function(opts) {
    opts = opts || {};
    var showTitle = opts.showTitle || false,
        truncText = opts.truncText || "&hellip;",
        split = [" ",""];
    this.each(function() {
        var $el = $(this),
            oldtext = $el.attr("oldtext") || $el.text(),
            txt, cutoff;
        if ($el.attr("oldtext")) {
            $el.text(oldtext);
        }
        $el.attr("oldtext", oldtext);
        for (var i in split) {
            delim = split[i];
            txt = oldtext.split(delim);
            cutoff = txt.length;
            var done = (this.scrollHeight - this.offsetHeight) < 2,
                chunk = Math.ceil(txt.length/2), oc=0, wid, delim;
            while (!done) {
                $el.html(txt.slice(0,cutoff).join(delim)+truncText);
                wid = (this.scrollHeight - this.offsetHeight);
                if (wid < 2 && chunk == oc) {
                   done = true;
                } else if (wid > 1) {
                   cutoff -= chunk;
                } else {
                   cutoff += chunk;
                }
                oc = chunk;
                chunk = Math.ceil(chunk/2);
            }
        }
        if (showTitle) {
            $el.attr("title", oldtext);
        }
    });
    return this;
};

// initializes a particle effect on the raygun, if supported.
$(document).ready(function() {
    if (!!document.createElement('canvas').getContext && //checks for canvas capability
        $('body').hasClass('home')) { //we're on the homepage
            
        var $c = $('<canvas></canvas>');
        var raygun = $('.header-right').offset();
        $(document.body).append($c);
        var smoke = {
          respawn: true,
          initNum: 1,
          num: 100,
          origin: [raygun.left+13,raygun.top+80],
          canvas: $c[0],
          particle: {
            life: [2000,3000],
            init: function() {
              var r = rand([0,2*PI]),
                  m = rand([5,30]);
              this.vars.goal = vsafe([m*.5*Math.cos(r), m*Math.sin(r)-90]);
              this.rad = 10;
            },
            tick: function(age) {
              this.pos = vsafe(vplus(vtimes(this.vars.goal, this.age), this.initPos));
              this.rad = this.age*8+2;
            },
            draw: function(ctx) {
              ctx.fillStyle = "rgba(160,160,160,"+Math.max((1-this.age)/4,0)+")";
              var r = this.rad;
              ctx.fillRect(-r, -r, r*2, r*2);
            }
          }
        };
        p = new ParticleEffect(smoke);
        p.go();

        function positionSmoke() {
            var raygun = $('.header-right').offset();
            p.origin = [raygun.left+13,raygun.top+80];
        }

        $(window).resize(positionSmoke);
        setTimeout(positionSmoke, 100);
    }
});