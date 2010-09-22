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

// initializes a particle effect on the raygun, if supported.
$(document).ready(function() {
    if (!!document.createElement('canvas').getContext &&
        $('body').hasClass('home')) { //checks for canvas capability
            
        var $c = $('<canvas></canvas>');
        var raygun = $('.header-right').position();
        $('#content').append($c);
        var smoke = {
          respawn: true,
          initNum: 5,
          origin: [raygun.left+12,raygun.top+59],
          canvas: $c[0],
          particle: {
            life: [2000,3000],
            init: function() {
              var r = rand([0,2*PI]),
                  m = rand([5,30]);
              this.vars.goal = vsafe([m*.5*Math.cos(r), m*Math.sin(r)-100]);
              this.rad = 10;
            },
            tick: function(age) {
              this.pos = vsafe(vplus(vtimes(this.vars.goal, this.age), this.initPos));
              this.rad = this.age*8+2;
            },
            draw: function(ctx) {
              ctx.fillStyle = "rgba(160,160,160,"+Math.max((.9-this.age)/5,0)+")";
              var r = this.rad;
              ctx.fillRect(-r, -r, r*2, r*2);
            }
          }
        };
        p = new ParticleEffect(smoke);
        p.go();
    }
});
